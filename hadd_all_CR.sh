#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/DYJetsToLL_M-10to50.root /cmsuf/data/store/user/nimenend/NanoAOD/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/210521_152619/0000/*.root
#
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/DYJetsToLL_M-50.root /cmsuf/data/store/user/nimenend/NanoAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/210521_152422/0000/*.root
#
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/TTJets_DiLept.root /cmsuf/data/store/user/nimenend/NanoAOD/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/210521_152839/0000/*.root
#
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/WZTo3LNu.root /cmsuf/data/store/user/nimenend/NanoAOD/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/210521_152223/0000/*.root
#
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/ZZTo4L.root /cmsuf/data/store/user/nimenend/NanoAOD/ZZTo4L_TuneCP5_13TeV-amcatnloFXFX-pythia8/ZZTo4L_TuneCP5_13TeV-amcatnloFXFX-pythia8/210521_153047/0000/*.root
#
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/WJetsToLNu.root /cmsuf/data/store/user/nimenend/NanoAOD/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/210521_153254/0000/*.root

#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/NanoAOD/WWTo2L2Nu.root /cmsuf/data/store/user/nimenend/NanoAOD/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/210526_094240/0000/*.root

#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/testing/old_SingleElectron.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/SingleElectron/*/2105*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/testing/old_SingleMuon.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/SingleMuon/*/2105*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/testing/old_DoubleEG.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleEG/*/2105*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/DoubleMuon.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleMuon/*/210529*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/testing/old_MuonEG.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/MuonEG/*/2105*/*/*.root

rm /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/WTo3l_M*.root
hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/WTo3l_M4.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/W*To3l_M4.root
hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/WTo3l_M5.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/W*To3l_M5.root
hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/WTo3l_M10.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/W*To3l_M10.root
hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/WTo3l_M15.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/W*To3l_M15.root
hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/WTo3l_M30.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/W*To3l_M30.root
hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/WTo3l_M60.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/control_sel/W*To3l_M60.root

#rm /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/WTo3l_M*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/WTo3l_M4.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/W*To3l_M4.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/WTo3l_M5.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/W*To3l_M5.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/WTo3l_M10.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/W*To3l_M10.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/WTo3l_M15.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/W*To3l_M15.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/WTo3l_M30.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/W*To3l_M30.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/WTo3l_M60.root /cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/W*To3l_M60.root

#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/DoubleMuon_B.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleMuon/*B/210529*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/DoubleMuon_C.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleMuon/*C/210529*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/DoubleMuon_D.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleMuon/*D/210529*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/DoubleMuon_E.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleMuon/*E/210529*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/DoubleMuon_F.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleMuon/*F/210529*/*/*.root
#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/testing/separated_DoubleMuon.root /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/testing/DoubleMuon_*.root
