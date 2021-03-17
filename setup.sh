#!/bin/bash

export PYTHONPATH=${PYTHONPATH}:${PWD}/

cd /cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_2_15/src/
eval `scramv1 runtime -sh`
cd -
