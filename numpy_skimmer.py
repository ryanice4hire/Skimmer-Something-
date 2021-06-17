from __future__ import division
import numpy as np
import uproot
import sys
from ROOT import TLorentzVector
import output_tree as ot
from tqdm import tqdm
from Utils.DeltaR import deltaR

dataset = str(sys.argv[1])
isMC = sys.argv[2]
sort_by = str(sys.argv[3])
isSignal = 0
if "To3l_M" in sys.argv[1] or "to3l_M" in sys.argv[1]:
	isSignal = 1
in_file = ""
out_file = ""
if isSignal==1:
	in_file = "/cmsuf/data/store/user/t2/users/nikmenendez/signal/NanoAOD/"+dataset+".root"
	out_file = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/"+sort_by+"/"+dataset+".root"
	sumW_file = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/"+sort_by+"/"+dataset+".txt"
elif isMC=="1":
	in_file = "/cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/"+dataset+".root"
	out_file = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/"+sort_by+"/"+dataset+".root"
	sumW_file = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/"+sort_by+"/"+dataset+".txt"
else:
	in_file = "/cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/"+dataset+".root"
	out_file = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/data/signal_sel/"+sort_by+"/"+dataset+".root"

print("Skimming file %s"%(in_file))

file = uproot.open(in_file)

events = file["Events"]
runs = file["Runs"]

if isMC=="1":
	#Get SumWeight
	sumW = 0
	SumWeights = runs["genEventSumw"].array()
	sumW = np.sum(SumWeights)

#Define cuts
cut0, cut1, cut2, cut3, cut4 = 0, 0, 0, 0, 0
leadingPtCut, subleadingPtCut, trailingPtCut = 20.0, 10.0, 5.0
iso_cut = 0.20
sip_cut = 50

#Import tree from ROOT
Run = events["run"].array()
Event = events["event"].array()
LumiSect = events["luminosityBlock"].array()
if isMC=="1": genWeight = events["genWeight"].array()

nMuon = events["nMuon"].array()
lep_pt = events["Muon_pt"].array()
lep_id = events["Muon_pdgId"].array()
lep_eta = events["Muon_eta"].array()
lep_phi = events["Muon_phi"].array()
lep_mass = events["Muon_mass"].array()
lep_iso = events["Muon_miniPFRelIso_all"].array()
lep_tight = events["Muon_tightId"].array()
lep_med = events["Muon_mediumId"].array()
lep_ip = events["Muon_ip3d"].array()
lep_sip = events["Muon_sip3d"].array()

MET = events["MET_pt"].array()
MET_phi = events["MET_phi"].array()

passedDiMu = events["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8"].array()
passedTriMu = events["HLT_TripleMu_10_5_5_DZ"].array() | events["HLT_TripleMu_12_10_5"].array()
passedTrig = passedDiMu | passedTriMu

if isSignal==1:
	gen_id = events["GenPart_pdgId"].array()
	gen_eta = events["GenPart_eta"].array()
	gen_pt = events["GenPart_pt"].array()

nEntries = len(nMuon)

if isMC=="1":
	print("Skimming %i events. SumWeight = %i"%(nEntries,sumW))
else:
	print("Skimming %i events."%(nEntries))

#Find acceptance of signal
left0 = nEntries
selection = nMuon >= 0
if isSignal==1:
	for ev in tqdm(range(len(gen_id))):
		m_found = 0
		gen = np.unique(np.array([gen_id[ev],gen_eta[ev],gen_pt[ev]]), axis=1)
		for i in range(len(gen[0])):
			if abs(gen[0][i])==13 and abs(gen[1][i])<=2.4 and gen[2][i]>=2.5: 
				#if i>0 and gen_id[ev][i]==gen_id[ev][i-1] and gen_eta[ev][i]==gen_eta[ev][i-1] and gen_pt[ev][i]==gen_pt[ev][i-1]: continue
				m_found+=1
		if m_found<3: selection[ev] = False
		#if selection[ev] and nMuon[ev] < 3:
		#	for i in range(len(gen_id[ev])):
		#		if abs(gen_id[ev][i])==13:
		#			print("id= %i, eta= %.3f, pt= %.3f"%(gen_id[ev][i],gen_eta[ev][i],gen_pt[ev][i]))
		#	print("Found %i muons in acceptance"%(m_found))
		#	print("Found %i muons in event"%(nMuon[ev]))
		#	print("***************************")
	left0 = np.count_nonzero(selection)

#Begin selection
selection *= nMuon >= 3
left1 = np.count_nonzero(selection)
selection *= passedTrig
left2 = np.count_nonzero(selection)
for ev in tqdm(range(len(nMuon))):
	if not selection[ev]: continue
	
	# Check different charged muon
	nmp, nmm = 0, 0
	for j in range(len(lep_id[ev])):
		if lep_id[ev][j] == 13: nmp+=1
		if lep_id[ev][j] == -13: nmm+=1
	if not (nmp>=1 and nmm>=1): selection[ev] = False
	if not selection[ev]: continue

	#Define needed variables
	index1, index2, index3 = 0, 0, 0
	foundZ1LCandidate = False

	Wmass = 81
	mZ1Low = 4.0
	mZ1High = 81.0

	#Find Z' candidate
	n_Zs=0
	Z_Z1L_lepindex1 = []
	Z_Z1L_lepindex2 = []
	for i in range(nMuon[ev]):
		for j in range(i+1,nMuon[ev]):
			if not lep_id[ev][i] + lep_id[ev][j] == 0: continue
			li = TLorentzVector()
			lj = TLorentzVector()
			li.SetPtEtaPhiM(lep_pt[ev][i],lep_eta[ev][i],lep_phi[ev][i],lep_mass[ev][i])
			lj.SetPtEtaPhiM(lep_pt[ev][j],lep_eta[ev][j],lep_phi[ev][j],lep_mass[ev][j])
			Z = li + lj
			
			if Z.M() > 0.0 :
				n_Zs+=1
				Z_Z1L_lepindex1.append(i)
				Z_Z1L_lepindex2.append(j)

	#Find best Z' candidate
	minZ1Mass = 999.9
	for i in range(n_Zs):
		i1, i2 = Z_Z1L_lepindex1[i], Z_Z1L_lepindex2[i]

		if abs(lep_id[ev][i1]) != 13: continue
		
		lep_i1 = TLorentzVector()
		lep_i2 = TLorentzVector()
		lep_i1.SetPtEtaPhiM(lep_pt[ev][i1],lep_eta[ev][i1],lep_phi[ev][i1],lep_mass[ev][i1])
		lep_i2.SetPtEtaPhiM(lep_pt[ev][i2],lep_eta[ev][i2],lep_phi[ev][i2],lep_mass[ev][i2])
		Z1 = lep_i1 + lep_i2
		
		Z1Mass = Z1.M()
		Z1_lepindex = [0,0]
		if lep_pt[ev][i1]>lep_pt[ev][i2]: Z1_lepindex = [i1,i2]
		else: Z1_lepindex = [i2,i1]

		#if lep_pt[ev][Z1_lepindex[0]] < leadingPtCut or lep_pt[ev][Z1_lepindex[1]] < subleadingPtCut: continue
		if lep_iso[ev][i1] > iso_cut or lep_iso[ev][i2] > iso_cut: continue
		if lep_med[ev][i1] != 1 or lep_med[ev][i2] != 1: continue
		if Z1Mass < mZ1Low or Z1Mass > mZ1High: continue

		if (Z1Mass > minZ1Mass): continue
		for lep in range(nMuon[ev]):
			if(lep==i1 or lep==i2): continue
			if abs(lep_id[ev][lep])!=13: continue
			tempIdx = lep

			#if lep_pt[ev][tempIdx] < leadingPtCut: continue
			if lep_iso[ev][tempIdx] > iso_cut: continue
			if lep_med[ev][tempIdx] != 1: continue

			temp = TLorentzVector()
			temp.SetPtEtaPhiM(lep_pt[ev][tempIdx],lep_eta[ev][tempIdx],lep_phi[ev][tempIdx],lep_mass[ev][tempIdx])

			Leps3 = lep_i1 + lep_i2 + temp
			Leps3_M = Leps3.M()
			if (Leps3_M > Wmass): continue

			leading, subleading, trailing = Z1_lepindex[0], Z1_lepindex[1], lep
			if lep_pt[ev][Z1_lepindex[0]] < lep_pt[ev][lep]:
				leading = lep
				subleading = Z1_lepindex[0]
				trailing = Z1_lepindex[1]
			elif lep_pt[ev][Z1_lepindex[1]] < lep_pt[ev][lep]:
				subleading = lep
				trailing = Z1_lepindex[1]
			if (lep_pt[ev][leading] < leadingPtCut or lep_pt[ev][subleading] < subleadingPtCut or lep_pt[ev][trailing] < trailingPtCut): continue

			minZ1Mass = Z1Mass
			index1 = Z1_lepindex[0]
			index2 = Z1_lepindex[1]
			index3 = lep
			foundZ1LCandidate=True
			break

	if not foundZ1LCandidate: selection[ev]=False
	if not selection[ev]: continue

	lep1 = TLorentzVector()
	lep2 = TLorentzVector()
	lep3 = TLorentzVector()

	indexes = [index1,index2,index3]
	sorter = np.array([0,0,0])
	if sort_by=="pt":
		sorter = np.array([lep_pt[ev][index1],lep_pt[ev][index2],lep_pt[ev][index3]])
	elif sort_by=="iso":
		sorter = np.array([lep_iso[ev][index1],lep_iso[ev][index2],lep_iso[ev][index3]])
	elif sort_by=="ip":
		sorter = np.array([lep_ip[ev][index1],lep_ip[ev][index2],lep_ip[ev][index3]])
	elif sort_by=="sip":
		sorter = np.array([lep_sip[ev][index1],lep_sip[ev][index2],lep_sip[ev][index3]])

	done_sort = np.argsort(sorter)
	index1 = indexes[done_sort[2]]
	index2 = indexes[done_sort[1]]
	index3 = indexes[done_sort[0]]

	#Order muons by pT
	#leading = index1
	#subleading = index2
	#trailing = index3
	#if lep_pt[ev][index1] < lep_pt[ev][index3]:
	#	leading = index3
	#	subleading = index1
	#	trailing = index2
	#elif lep_pt[ev][index2] < lep_pt[ev][index3]:
	#	subleading = index3
	#	trailing = index2
	#index1 = leading
	#index2 = subleading
	#index3 = trailing

	#Create lepton vectors
	lep1.SetPtEtaPhiM(lep_pt[ev][index1],lep_eta[ev][index1],lep_phi[ev][index1],lep_mass[ev][index1])
	lep2.SetPtEtaPhiM(lep_pt[ev][index2],lep_eta[ev][index2],lep_phi[ev][index2],lep_mass[ev][index2])
	lep3.SetPtEtaPhiM(lep_pt[ev][index3],lep_eta[ev][index3],lep_phi[ev][index3],lep_mass[ev][index3])
	
	threeleps = lep1+lep2+lep3
	Met = TLorentzVector()
	Met.SetPtEtaPhiM(MET[ev],0,MET_phi[ev],0)
	
	ot.idL1[0], ot.idL2[0], ot.idL3[0] = lep_id[ev][index1], lep_id[ev][index2], lep_id[ev][index3]
	ot.pTL1[0], ot.pTL2[0], ot.pTL3[0] = lep1.Pt(), lep2.Pt(), lep3.Pt()
	ot.etaL1[0], ot.etaL2[0], ot.etaL3[0] = lep1.Eta(), lep2.Eta(), lep3.Eta()
	ot.phiL1[0], ot.phiL2[0], ot.phiL3[0] = lep1.Phi(), lep2.Phi(), lep3.Phi()
	ot.IsoL1[0], ot.IsoL2[0], ot.IsoL3[0] = lep_iso[ev][index1], lep_iso[ev][index2], lep_iso[ev][index3]
	ot.ip3dL1[0], ot.ip3dL2[0], ot.ip3dL3[0] = lep_ip[ev][index1], lep_ip[ev][index2], lep_ip[ev][index3]
	ot.sip3dL1[0], ot.sip3dL2[0], ot.sip3dL3[0] = lep_sip[ev][index1], lep_sip[ev][index2], lep_sip[ev][index3]
	ot.massL1[0], ot.massL2[0], ot.massL3[0] = lep1.M(), lep2.M(), lep3.M()
	ot.tightIdL1[0], ot.tightIdL2[0], ot.tightIdL3[0] = lep_tight[ev][index1], lep_tight[ev][index2], lep_tight[ev][index3]
	ot.medIdL1[0], ot.medIdL2[0], ot.medIdL3[0] = lep_med[ev][index1], lep_med[ev][index2], lep_med[ev][index3]
	ot.dR12[0] = deltaR(lep1.Eta(),lep1.Phi(),lep2.Eta(),lep2.Phi())
	ot.dR13[0] = deltaR(lep1.Eta(),lep1.Phi(),lep3.Eta(),lep3.Phi())
	ot.dR23[0] = deltaR(lep2.Eta(),lep2.Phi(),lep3.Eta(),lep3.Phi())
	ot.met[0], ot.met_phi[0] = MET[ev], MET_phi[ev]
	
	#ot.nLep[0] = nLep
	#ot.nElectrons[0] = t.nElectron
	ot.nMuons[0] = nMuon[ev]
	#ot.trueL3[0] = trueL3
	ot.m3l[0] = threeleps.M()
	ot.mt[0] = (threeleps+Met).M()
	
	ot.Run[0] = Run[ev]
	ot.Event[0] = Event[ev]
	ot.LumiSect[0] = LumiSect[ev]
	
	if isMC=="1": ot.genWeight[0] = genWeight[ev]
	
	ot.passedDiMu[0] = passedDiMu[ev]
	ot.passedTriMu[0] = passedTriMu[ev]
	
	ot.out_tree.Fill()

ot.f_out.Write()
ot.f_out.Close()
	
left3 = np.count_nonzero(selection)
#print(np.count_nonzero(selection)/len(selection)*100)

print("Efficiencies for each cut")
print("=====================================================")
print("Total events before cuts: %i"%(nEntries))
if isSignal==1: print("In acceptance: %i. Efficiency = %.2f%%"%(left0,left0/nEntries))
print("Pass 3 muon cut: %i. Efficiency = %.2f%%"%(left1,left1/left0*100))
print("Pass Trigger: %i. Efficiency = %.2f%%"%(left2,left2/left1*100))
print("Found Z candidate: %i. Efficiency = %.2f%%"%(left3,left3/left2*100))
print("=====================================================")
print("Total Efficiency = %.2f%%"%(left3/nEntries*100))
print("Wrote to file %s"%(out_file))
print("")

