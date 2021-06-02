#srun --ntasks=1 --cpus-per-task=8 --mem=16gb -t 600 --pty bash -i

dataset_list=()
isMC=()

#dataset_list+=( "DYJetsToLL_M10To50" )
#dataset_list+=( "DYJetsToLL_M50" )
#dataset_list+=( "TTJets_DiLept" )
#dataset_list+=( "WZTo3LNu" )
#dataset_list+=( "ZZTo4L" )
#dataset_list+=( "WJetsToLNu" )
#dataset_list+=( "WWTo2L2Nu" )
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#
##dataset_list+=( "SingleElectron" )
##dataset_list+=( "SingleMuon" )
##dataset_list+=( "DoubleEG" )
##dataset_list+=( "DoubleMuon" )
##dataset_list+=( "MuonEG" )
##isMC+=("0")
##isMC+=("0")
##isMC+=("0")
##isMC+=("0")
##isMC+=("0")
#
#dataset_list+=( "WmTo3l_M4" )
#dataset_list+=( "WmTo3l_M5" )
#dataset_list+=( "WmTo3l_M10" )
#dataset_list+=( "WmTo3l_M15" )
#dataset_list+=( "WmTo3l_M30" )
#dataset_list+=( "WmTo3l_M60" )
#dataset_list+=( "WpTo3l_M4" )
#dataset_list+=( "WpTo3l_M5" )
#dataset_list+=( "WpTo3l_M10" )
#dataset_list+=( "WpTo3l_M15" )
#dataset_list+=( "WpTo3l_M30" )
#dataset_list+=( "WpTo3l_M60" )
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#isMC+=("1")
#
#dataset_list+=( "DoubleMuon_B" )
#dataset_list+=( "DoubleMuon_C" )
#dataset_list+=( "DoubleMuon_D" )
#dataset_list+=( "DoubleMuon_E" )
dataset_list+=( "DoubleMuon_F" )
isMC+=("0")
#isMC+=("0")
#isMC+=("0")
#isMC+=("0")
#isMC+=("0")

#hadd -fk /cmsuf/data/store/user/t2/users/nikmenendez/data_wto3l/2017/DoubleMuon.root /cmsuf/data/store/user/nimenend/NanoAOD/Data/DoubleMuon/*/210529*/*/*.root

for i in ${!dataset_list[@]}; do
	python numpy_skimmer_CR.py ${dataset_list[i]} ${isMC[i]}
done

source hadd_all_CR.sh
source removeDuplicates_CR.sh
