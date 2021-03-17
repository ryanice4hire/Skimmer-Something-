# Wto3l_NanoAOD_Skimmer

# Skimmer.py

skimmer.py is the main file. Add path to unskimmed MC and data files to input_path under isMC and else. Also add output path.

Modify the logic of the skimmer in this file.

# Output_tree.py

In output_tree.py, choose what branches want to be saved in the skimmed ntuple.

# run_skimmer.sh

Add the names of the datasets you want to skim to dataset_list. Also add it it is MC ("1") or not ("0") to isMC. Then run run_skimmer.sh to run.
