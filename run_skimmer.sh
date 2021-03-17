dataset_list=( "DYJetsToLL_M-10to50" )
dataset_list+=( "DYJetsToLL_M-50" )
dataset_list+=( "TTJets_DiLept" )
dataset_list+=( "WZTo3LNu" )
dataset_list+=( "ZZTo4L" )
dataset_list+=( "WJetsToLNu" )
isMC=("1")
isMC+=("1")
isMC+=("1")
isMC+=("1")
isMC+=("1")
isMC+=("1")

dataset_list+=( "SingleElectron" )
dataset_list+=( "SingleMuon" )
dataset_list+=( "DoubleEG" )
dataset_list+=( "DoubleMuon" )
dataset_list+=( "MuonEG" )
isMC+=("0")
isMC+=("0")
isMC+=("0")
isMC+=("0")
isMC+=("0")


for i in ${!dataset_list[@]}; do
	python skimmer.py ${dataset_list[i]} ${isMC[i]}
done
