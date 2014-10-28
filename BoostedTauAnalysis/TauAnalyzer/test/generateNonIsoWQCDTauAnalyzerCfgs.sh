#!/bin/bash

if [ $# -gt 3 ]
    then
    echo "Usage: ./generateNonIsoWQCDTauAnalyzerCfgs.sh <version> <template cfg> [reweightOnly]"
    exit 0
fi

####STUFF TO CONFIGURE####

#version
version=$1
templateCfg=$2
infoTag=""
reweightOnly=0
if [ "$3" == "reweightOnly" ]
    then
    reweightOnly=1
fi
dir=$version

#number of samples
nSamples=11
iBeg=0
iEnd=`expr $nSamples - 1`

#input file prefix
inputFilePrefix="root://eoscms//eos/cms/store/user/friccita/"
inputFileSuffix="_MuEnrichedPt5_TuneZ2star_8TeV_pythia6-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_nonIsoW/"

#CleanJets output file prefix
#cleanJetsOutputFilePrefix="`pwd`/${dir}/"
cleanJetsOutputFilePrefix=""

#TauAnalyzer output file prefix
#tauAnalyzerOutputFilePrefix="/data1/yohay/ZZ/analysis/"
tauAnalyzerOutputFilePrefix=""

#EDM output file prefix
EDMOutputFilePrefix="/data1/`whoami`/nonIsoWQCD/EDM_files/"

####VECTORS OF QUANTITIES FOR EACH SAMPLE####

#vector of input file blocks for each sample
#"readFiles.extend([\n    ])"
#    ])" "readFiles.extend([\n
inputFileBlocks=( "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_10_1_SQu.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_11_1_pMT.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_12_1_oD9.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_13_1_0WW.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_14_1_eDI.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_15_1_Y3G.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_16_1_iQD.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_17_1_E6S.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_18_1_AR5.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_19_1_A9n.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_1_1_ugq.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_20_1_fsN.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_21_1_Yl6.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_22_1_99r.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_23_1_uHS.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_24_1_9mx.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_25_1_065.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_26_1_2gm.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_27_1_a8D.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_28_1_jtB.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_29_1_Urw.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_2_1_QGq.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_30_1_GpM.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_31_1_Yom.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_32_1_nlg.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_33_1_eYM.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_34_1_pLp.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_35_1_eNo.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_36_1_OAG.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_3_1_wOt.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_4_1_MJj.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_5_1_T6w.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_6_1_brP.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_7_1_yiG.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_8_1_Mpm.root',\n    '${inputFilePrefix}QCD_Pt-20to30${inputFileSuffix}data_no_selection_9_1_abb.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_10_1_SVX.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_11_1_An9.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_12_1_ctC.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_13_1_acS.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_14_1_A1F.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_15_1_8sr.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_16_1_asx.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_17_1_j7w.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_18_1_BF4.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_19_1_GEi.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_1_1_qM6.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_20_1_bQI.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_21_1_DJs.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_22_1_Xw0.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_23_1_QRb.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_24_1_qHr.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_25_1_Jq5.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_26_1_BB4.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_27_1_0Vr.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_28_1_g9q.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_29_1_UvK.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_2_1_jZ8.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_30_1_1eo.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_31_1_mgB.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_32_1_i3s.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_33_1_4mh.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_34_1_QX0.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_35_1_yD4.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_36_1_kfv.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_37_1_4jC.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_38_1_KvX.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_39_1_5o3.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_3_1_SGn.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_40_1_dXt.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_4_1_Qlb.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_5_1_c6W.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_6_1_X7I.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_7_1_HkK.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_8_1_FE4.root',\n    '${inputFilePrefix}QCD_Pt-30to50${inputFileSuffix}data_no_selection_9_1_67m.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_10_1_tJJ.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_11_1_mfD.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_12_1_Ewy.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_13_1_Kda.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_14_1_fkP.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_15_1_0Aq.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_16_1_iB7.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_17_1_rDu.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_18_1_Bce.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_19_1_251.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_1_1_M5A.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_20_1_15P.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_21_1_HqI.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_22_1_sxZ.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_23_1_ZEG.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_24_1_Jeq.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_25_1_mv8.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_26_1_yWs.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_27_1_n8k.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_28_1_biN.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_29_1_kJu.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_2_1_SEr.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_30_1_HbA.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_31_1_xQt.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_32_1_0Bm.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_33_1_Fde.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_34_1_dvX.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_35_1_mvs.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_36_1_0v7.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_37_1_o3x.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_38_1_0oO.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_39_1_gFo.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_3_1_L9Q.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_40_1_wE3.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_41_1_ACU.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_42_1_HuH.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_43_1_igj.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_4_1_H9Y.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_5_1_3i6.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_6_1_f9V.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_7_1_mye.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_8_1_BTQ.root',\n    '${inputFilePrefix}QCD_Pt-50to80${inputFileSuffix}data_no_selection_9_1_KXb.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_10_1_Z6G.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_11_1_RNW.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_12_1_VSp.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_13_1_Cek.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_14_2_y2c.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_15_1_zZX.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_16_2_jxz.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_17_2_xQg.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_18_1_3Ns.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_19_1_az4.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_1_1_wNo.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_20_1_HGw.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_21_1_8Jb.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_22_1_fCq.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_23_1_Dkh.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_24_1_ByO.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_25_3_oue.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_26_1_IgV.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_27_1_eqj.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_28_1_GJh.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_29_1_2jx.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_2_1_1Vg.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_30_3_Ng3.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_31_1_hZ1.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_32_1_SXd.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_33_1_K94.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_34_1_HnN.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_35_1_3G9.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_36_2_m0M.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_37_2_hM8.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_38_1_Tua.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_39_1_hha.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_3_2_aPi.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_4_1_Gzk.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_5_1_QjA.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_6_1_Goi.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_7_1_poS.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_8_1_5lE.root',\n    '${inputFilePrefix}QCD_Pt-80to120${inputFileSuffix}data_no_selection_9_1_3gF.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_10_1_NtF.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_11_1_Iij.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_12_1_lMi.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_13_1_zCz.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_14_1_Pab.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_15_1_IO5.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_16_1_W6I.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_17_1_QJr.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_18_1_sNw.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_19_1_oeU.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_1_1_amQ.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_20_1_aNL.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_21_1_OCx.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_22_1_gua.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_23_1_qKF.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_24_1_Bda.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_25_1_6GW.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_26_1_Ipb.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_27_1_arW.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_28_1_kXh.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_29_1_NJa.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_2_1_rKw.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_30_1_5zm.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_31_1_aj1.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_32_1_DEO.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_33_1_A8v.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_34_1_Cnu.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_35_1_i5E.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_3_1_cbo.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_4_1_2wK.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_5_1_eY7.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_6_1_r6g.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_7_4_jZi.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_8_1_5FU.root',\n    '${inputFilePrefix}QCD_Pt-120to170${inputFileSuffix}data_no_selection_9_1_SOw.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_10_1_Wa8.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_11_1_w4K.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_12_1_JXT.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_13_1_YfJ.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_14_1_g2d.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_15_1_1WF.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_16_1_odZ.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_17_1_7KZ.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_18_1_S1D.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_19_1_0t4.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_1_1_Ot1.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_20_1_Ddf.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_21_1_Wo2.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_22_1_k5t.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_23_1_fV9.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_24_1_PcN.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_25_1_90e.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_26_1_Xwg.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_27_1_Ler.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_28_1_isz.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_29_1_LGU.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_2_1_UKr.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_30_1_Tay.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_31_1_mEq.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_32_1_1tq.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_3_1_BoK.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_4_1_vQH.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_5_1_iUF.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_6_1_MaV.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_7_1_o95.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_8_1_MIM.root',\n    '${inputFilePrefix}QCD_Pt-170to300${inputFileSuffix}data_no_selection_9_1_EWN.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_10_1_BL7.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_11_1_llL.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_12_1_wHb.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_13_1_tJ2.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_14_1_pke.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_15_1_NNe.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_16_1_aqU.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_17_1_Jy9.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_18_1_iFX.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_19_1_6Pc.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_1_1_bQu.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_20_1_4z9.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_21_1_oSU.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_22_1_4Av.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_23_1_8oI.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_24_1_Di3.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_25_1_3IG.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_26_1_Wdp.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_27_1_prh.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_28_1_BE1.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_29_1_byn.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_2_1_mGU.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_30_1_03P.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_31_1_I8c.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_32_1_1v5.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_33_1_Vef.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_3_1_a4S.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_4_1_72f.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_5_1_wwU.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_6_1_wQl.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_7_1_o2a.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_8_1_f0g.root',\n    '${inputFilePrefix}QCD_Pt-300to470${inputFileSuffix}data_no_selection_9_1_sqW.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_10_1_U6A.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_11_1_IQJ.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_12_1_wZu.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_13_1_CGD.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_14_1_CnA.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_15_1_0NF.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_16_1_XRQ.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_17_1_2Rh.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_1_1_67M.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_2_1_l0D.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_3_1_v6k.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_4_1_ja7.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_5_1_3HR.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_6_1_0nD.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_7_1_BK5.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_8_1_tl3.root',\n    '${inputFilePrefix}QCD_Pt-470to600${inputFileSuffix}data_no_selection_9_1_FBD.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_10_2_3Tr.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_11_1_67q.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_12_1_nD4.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_13_2_DPY.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_14_1_X0e.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_15_1_A9T.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_16_1_a46.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_17_1_sh1.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_18_1_yYJ.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_19_1_HOJ.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_1_1_ZXR.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_20_1_HHY.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_2_1_NJl.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_3_1_KUO.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_4_1_BG6.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_5_1_8CS.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_6_1_Gfh.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_7_2_A2u.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_8_1_rVv.root',\n    '${inputFilePrefix}QCD_Pt-600to800${inputFileSuffix}data_no_selection_9_1_PlG.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_10_1_lNK.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_11_1_92l.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_12_1_c72.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_13_1_129.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_14_1_Egw.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_15_1_7UU.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_16_1_5yB.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_17_1_ADa.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_1_1_KKn.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_2_1_6Ky.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_3_1_N6c.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_4_1_uB6.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_5_1_2zS.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_6_1_qnP.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_7_1_Hbv.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_8_1_xp8.root',\n    '${inputFilePrefix}QCD_Pt-800to1000${inputFileSuffix}data_no_selection_9_1_Eq4.root',\n    ])" "readFiles.extend([\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_10_1_Vc0.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_11_1_hKl.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_12_1_aeh.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_13_1_gRG.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_14_1_DlR.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_15_1_COJ.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_16_1_EJy.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_17_1_8Oo.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_18_1_mQt.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_1_1_ioF.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_2_1_oFa.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_3_1_ca0.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_4_1_T30.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_5_1_iXx.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_6_1_Otg.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_7_1_nAq.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_8_1_RM8.root',\n    '${inputFilePrefix}QCD_Pt-1000${inputFileSuffix}data_no_selection_9_1_8cW.root',\n    ])" )

#CleanJets output file
cleanJetsOutFiles=( "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_NonIsoWQCD.root" )

#TauAnalyzer output files
highMTIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_NonIsoWQCD_${version}.root" )
lowMTIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_NonIsoWQCD_${version}.root" )
highMTNonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_NonIsoWQCD_${version}.root" )
lowMTNonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_NonIsoWQCD_${version}.root" )
nonIsoReweightTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_NonIsoWQCD_${version}.root" )
highMTAllTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_NonIsoWQCD_${version}.root" )
lowMTAllTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_NonIsoWQCD_${version}.root" )

#EDM output files
EDMOutputFiles=( "${EDMOutputFilePrefix}NonIsoWQCD${infoTag}_${version}.root" )

#samples
#samples=( "NonIsoWQCD" )

#samples
samples=( "QCD_Pt-20to30" "QCD_Pt-30to50" "QCD_Pt-50to80" "QCD_Pt-80to120" "QCD_Pt-120to170" "QCD_Pt-170to300" "QCD_Pt-300to470" "QCD_Pt-470to600" "QCD_Pt-600to800" "QCD_Pt-800to1000" "QCD_Pt-1000" )

####GENERATION LOOP####

#change to working directory
mkdir -p $dir
cd $dir

#loop over number of samples
for i in `seq $iBeg $iEnd`
  do

  #generate cfg file for the isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTIsoTauAnalysisSequence%" -e "s%REWEIGHT%False%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_iso_cfg.py

  #generate cfg file for the non-isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTNonIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTNonIsoTauAnalysisSequence%" -e "s%REWEIGHT%False%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIso_cfg.py

  #generate cfg file for the non-isolated, reweighted sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${nonIsoReweightTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTNonIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTNonIsoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIsoReweight_cfg.py

  #generate cfg file for the sample with no isolation cut
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTTauAnalysisSequence%" -e "s%REWEIGHT%False%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_all_cfg.py

  #generate iso+nonIso+reweight job submission script for LSF
  cat <<EOF > tauanalyzer_${samples[${i}]}_cfg.sh
#!/bin/bash

jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

cd \$jobDir
eval \`scramv1 runtime -sh\`
cd -
cp \$jobDir/\${fileNamePrefix}_iso_cfg.py \$jobDir/\${fileNamePrefix}_nonIso_cfg.py \$jobDir/\${fileNamePrefix}_nonIsoReweight_cfg.py .
cmsRun \${fileNamePrefix}_iso_cfg.py
if [ $reweightOnly -eq 0 ]
    then
    cmsRun \${fileNamePrefix}_nonIso_cfg.py
    cmsStage -f ${highMTNonIsoTauAnalyzerOutputFiles[${i}]} /store/user/`whoami`/
    cmsStage -f ${lowMTNonIsoTauAnalyzerOutputFiles[${i}]} /store/user/`whoami`/
    rm ${highMTNonIsoTauAnalyzerOutputFiles[${i}]} ${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}
fi
#cmsRun \${fileNamePrefix}_nonIsoReweight_cfg.py
cmsStage -f ${highMTIsoTauAnalyzerOutputFiles[${i}]} /store/user/`whoami`/
cmsStage -f ${lowMTIsoTauAnalyzerOutputFiles[${i}]} /store/user/`whoami`/
#cmsStage -f ${nonIsoReweightTauAnalyzerOutputFiles[${i}]} /store/user/`whoami`/
rm ${highMTIsoTauAnalyzerOutputFiles[${i}]} ${lowMTIsoTauAnalyzerOutputFiles[${i}]}
#rm ${nonIsoReweightTauAnalyzerOutputFiles[${i}]} 

exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_cfg.sh

  #generate noIsoCut job submission script for LSF
  cat <<EOF > tauanalyzer_${samples[${i}]}_all_cfg.sh
#!/bin/bash

jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

cd \$jobDir
eval \`scramv1 runtime -sh\`
cd -
cp \$jobDir/\${fileNamePrefix}_all_cfg.py .
cmsRun \${fileNamePrefix}_all_cfg.py
cmsStage -f ${highMTAllTauAnalyzerOutputFiles[${i}]} /store/user/`whoami`/
cmsStage -f ${lowMTAllTauAnalyzerOutputFiles[${i}]} /store/user/`whoami`/
rm ${highMTAllTauAnalyzerOutputFiles[${i}]} ${lowMTAllTauAnalyzerOutputFiles[${i}]}

exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_all_cfg.sh
done

#generate run cfg that runs all files in the directory
cat <<EOF > runNonIsoWQCDTauAnalyzerCfgs.sh
#!/bin/bash

for file in \`ls -alh *NonIsoWQCD_*.py | awk '{ print \$9 }'\`
  do
  outFile=\`echo \$file | sed -e "s%\.py%.txt%"\`
  cmsRun \$file > \$outFile
done

exit 0
EOF
chmod a+x runNonIsoWQCDTauAnalyzerCfgs.sh

#generate script that submits all iso+nonIso+reweight jobs to LSF
cat <<EOF > submitNonIsoWQCDTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*NonIsoWQCD_*.sh | grep -v all | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  bsub -q 8nh -J \$jobName < \$file
done

exit 0
EOF
chmod a+x submitNonIsoWQCDTauAnalyzerJobs.sh

#generate script that submits all noIsoCut jobs to LSF
cat <<EOF > submitNonIsoWQCDAllTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*NonIsoWQCD_*all*.sh | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  bsub -q 8nh -J \$jobName < \$file
done

exit 0
EOF
chmod a+x submitNonIsoWQCDAllTauAnalyzerJobs.sh

#generate script that copies all iso+nonIso+reweight files locally from EOS
cat <<EOF > copyNonIsoWQCDFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in \`seq `expr $iBeg + 1` `expr $iEnd + 1`\`
  do
  #for cut in Iso NonIso NonIsoReweight
  for cut in Iso NonIso
    do
    for MTBin in high low
      do
      if [ "\$cut" != "NonIso" ] || [ $reweightOnly -eq 0 ]
          then
          cmsStage -f /store/user/`whoami`/muHad\${cut}Analysis_\${MTBin}MT_NonIsoWQCD_${version}.root /data1/`whoami`/nonIsoWQCD/analysis/
          cmsRm /store/user/`whoami`/muHad\${cut}Analysis_\${MTBin}MT_NonIsoWQCD_${version}.root
      fi
    done
  done
done

exit 0
EOF
chmod a+x copyNonIsoWQCDFromEOS.sh

#generate script that copies all noIsoCut files locally from EOS
cat <<EOF > copyAllNonIsoWQCDFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in \`seq `expr $iBeg + 1` `expr $iEnd + 1`\`
  do
  for MTBin in high low
    do
    cmsStage -f /store/user/`whoami`/muHadAnalysis_\${MTBin}MT_NonIsoWQCD_${version}.root /data1/`whoami`/nonIsoWQCD/analysis/
    cmsRm /store/user/`whoami`/muHadAnalysis_\${MTBin}MT_NonIsoWQCD_${version}.root
  done
done

exit 0
EOF
chmod a+x copyAllNonIsoWQCDFromEOS.sh

exit 0
