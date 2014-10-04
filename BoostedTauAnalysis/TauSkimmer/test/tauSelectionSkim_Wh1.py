import FWCore.ParameterSet.Config as cms
from subprocess import *

process = cms.Process("SKIM")

#user
USER = Popen("whoami", stdout=PIPE, shell=True).stdout.read().strip('\n')

#PDG IDs
A_PDGID = 36
Z_PDGID = 23
W_PDGID = 24
TAU_PDGID = 15
MU_PDGID = 13
NUMU_PDGID = 14
D_PDGID = 1
U_PDGID = 2
S_PDGID = 3
C_PDGID = 4
B_PDGID = 5
T_PDGID = 6
G_PDGID = 21
ANY_PDGID = 0

#tau decay types
TAU_HAD = 0
TAU_MU = 1
TAU_E = 2
TAU_ALL = 3

#tau hadronic decay types
TAU_ALL_HAD = -1
TAU_1PRONG_0NEUTRAL = 0
TAU_1PRONG_1NEUTRAL = 1
TAU_1PRONG_2NEUTRAL = 2
TAU_1PRONG_3NEUTRAL = 3
TAU_1PRONG_NNEUTRAL = 4
TAU_2PRONG_0NEUTRAL = 5
TAU_2PRONG_1NEUTRAL = 6
TAU_2PRONG_2NEUTRAL = 7
TAU_2PRONG_3NEUTRAL = 8
TAU_2PRONG_NNEUTRAL = 9
TAU_3PRONG_0NEUTRAL = 10
TAU_3PRONG_1NEUTRAL = 11
TAU_3PRONG_2NEUTRAL = 12
TAU_3PRONG_3NEUTRAL = 13
TAU_3PRONG_NNEUTRAL = 14
TAU_RARE = 15

#no consideration of pT rank
ANY_PT_RANK = -1

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10000)

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

readFiles = cms.untracked.vstring()
process.source = cms.Source(
    "PoolSource",
    fileNames = readFiles,
    skipEvents = cms.untracked.uint32(0)
    )
readFiles.extend([
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_1.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_10.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_100.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_1000.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_101.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_102.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_103.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_104.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_105.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_106.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_107.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_108.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_109.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_11.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_110.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_111.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_112.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_113.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_114.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_115.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_116.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_117.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_118.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_119.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_12.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_120.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_121.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_122.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_123.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_124.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_125.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_126.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_127.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_128.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_129.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_13.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_130.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_131.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_132.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_133.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_134.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_135.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_136.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_137.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_138.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_139.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_14.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_140.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_141.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_142.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_143.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_144.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_145.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_146.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_147.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_148.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_149.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_15.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_150.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_151.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_152.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_153.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_154.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_155.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_156.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_157.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_158.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_159.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_16.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_160.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_161.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_162.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_163.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_164.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_165.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_166.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_167.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_168.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_169.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_17.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_170.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_171.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_172.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_173.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_174.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_175.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_176.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_177.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_178.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_179.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_18.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_180.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_181.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_182.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_183.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_184.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_185.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_186.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_187.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_188.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_189.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_19.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_190.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_191.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_192.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_193.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_194.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_195.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_196.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_197.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_198.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_199.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_2.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_20.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_200.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_201.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_202.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_203.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_204.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_205.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_206.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_207.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_208.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_209.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_21.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_210.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_211.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_212.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_213.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_214.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_215.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_216.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_217.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_218.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_219.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_22.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_220.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_221.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_222.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_223.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_224.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_225.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_226.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_227.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_228.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_229.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_23.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_230.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_231.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_232.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_233.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_234.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_235.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_236.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_237.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_238.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_239.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_24.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_240.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_241.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_242.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_243.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_244.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_245.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_246.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_247.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_248.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_249.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_25.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_250.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_251.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_252.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_253.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_254.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_255.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_256.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_257.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_258.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_259.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_26.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_260.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_261.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_262.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_263.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_264.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_265.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_266.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_267.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_268.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_269.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_27.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_270.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_271.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_272.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_273.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_274.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_275.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_276.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_277.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_278.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_279.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_28.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_280.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_281.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_282.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_283.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_284.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_285.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_286.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_287.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_288.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_289.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_29.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_290.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_291.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_292.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_293.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_294.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_295.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_296.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_297.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_298.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_299.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_3.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_30.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_300.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_301.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_302.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_303.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_304.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_305.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_306.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_307.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_308.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_309.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_31.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_310.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_311.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_312.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_313.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_314.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_315.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_316.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_317.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_318.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_319.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_32.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_320.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_321.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_322.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_323.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_324.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_325.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_326.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_327.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_328.root'
    ])
readFiles.extend([
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_329.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_33.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_330.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_331.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_332.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_333.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_334.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_335.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_336.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_337.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_338.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_339.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_34.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_340.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_341.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_342.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_343.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_344.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_345.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_346.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_347.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_348.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_349.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_35.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_350.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_351.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_352.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_353.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_354.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_355.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_356.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_357.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_358.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_359.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_36.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_360.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_361.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_362.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_363.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_364.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_365.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_366.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_367.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_368.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_369.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_37.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_370.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_371.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_372.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_373.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_374.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_375.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_376.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_377.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_378.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_379.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_38.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_380.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_381.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_382.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_383.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_384.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_385.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_386.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_387.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_388.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_389.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_39.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_390.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_391.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_392.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_393.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_394.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_395.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_396.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_397.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_398.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_399.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_4.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_40.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_400.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_401.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_402.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_403.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_404.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_405.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_406.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_407.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_408.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_409.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_41.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_410.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_411.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_412.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_413.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_414.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_415.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_416.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_417.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_418.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_419.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_42.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_420.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_421.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_422.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_423.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_424.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_425.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_426.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_427.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_428.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_429.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_43.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_430.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_431.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_432.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_433.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_434.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_435.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_436.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_437.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_438.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_439.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_44.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_440.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_441.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_442.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_443.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_444.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_445.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_446.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_447.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_448.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_449.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_45.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_450.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_451.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_452.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_453.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_454.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_455.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_456.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_457.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_458.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_459.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_46.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_460.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_461.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_462.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_463.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_464.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_465.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_466.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_467.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_468.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_469.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_47.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_470.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_471.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_472.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_473.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_474.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_475.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_476.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_477.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_478.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_479.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_48.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_480.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_481.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_482.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_483.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_484.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_485.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_486.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_487.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_488.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_489.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_49.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_490.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_491.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_492.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_493.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_494.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_495.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_496.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_497.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_498.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_499.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_5.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_50.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_500.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_501.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_502.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_503.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_504.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_505.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_506.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_507.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_508.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_509.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_51.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_510.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_511.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_512.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_513.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_514.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_515.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_516.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_517.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_518.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_519.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_52.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_520.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_521.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_522.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_523.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_524.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_525.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_526.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_527.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_528.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_529.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_53.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_530.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_531.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_532.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_533.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_534.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_535.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_536.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_537.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_538.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_539.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_54.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_540.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_541.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_542.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_543.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_544.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_545.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_546.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_547.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_548.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_549.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_55.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_550.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_551.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_552.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_553.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_554.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_555.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_556.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_557.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_558.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_559.root'
    ])
readFiles.extend([
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_56.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_560.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_561.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_562.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_563.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_564.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_565.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_566.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_567.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_568.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_569.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_57.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_570.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_571.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_572.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_573.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_574.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_575.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_576.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_577.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_578.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_579.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_58.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_580.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_581.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_582.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_583.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_584.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_585.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_586.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_587.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_588.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_589.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_59.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_590.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_591.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_592.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_593.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_594.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_595.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_596.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_597.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_598.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_599.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_6.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_60.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_600.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_601.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_602.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_603.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_604.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_605.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_606.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_607.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_608.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_609.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_61.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_610.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_611.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_612.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_613.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_614.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_615.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_616.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_617.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_618.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_619.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_62.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_620.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_621.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_622.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_623.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_624.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_625.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_626.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_627.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_628.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_629.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_63.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_630.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_631.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_632.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_633.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_634.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_635.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_636.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_637.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_638.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_639.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_64.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_640.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_641.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_642.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_643.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_644.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_645.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_646.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_647.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_648.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_649.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_65.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_650.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_651.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_652.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_653.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_654.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_655.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_656.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_657.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_658.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_659.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_66.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_660.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_661.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_662.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_663.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_664.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_665.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_666.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_667.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_668.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_669.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_67.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_670.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_671.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_672.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_673.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_674.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_675.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_676.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_677.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_678.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_679.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_68.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_680.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_681.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_682.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_683.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_684.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_685.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_686.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_687.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_688.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_689.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_69.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_690.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_691.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_692.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_693.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_694.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_695.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_696.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_697.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_698.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_699.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_7.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_70.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_700.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_701.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_702.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_703.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_704.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_705.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_706.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_707.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_708.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_709.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_71.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_710.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_711.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_712.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_713.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_714.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_715.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_716.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_717.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_718.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_719.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_72.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_720.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_721.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_722.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_723.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_724.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_725.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_726.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_727.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_728.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_729.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_73.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_730.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_731.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_732.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_733.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_734.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_735.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_736.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_737.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_738.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_739.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_74.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_740.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_741.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_742.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_743.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_744.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_745.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_746.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_747.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_748.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_749.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_75.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_750.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_751.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_752.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_753.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_754.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_755.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_756.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_757.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_758.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_759.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_76.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_760.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_761.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_762.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_763.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_764.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_765.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_766.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_767.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_768.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_769.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_77.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_770.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_771.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_772.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_773.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_774.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_775.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_776.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_777.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_778.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_779.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_78.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_780.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_781.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_782.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_783.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_784.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_785.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_786.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_787.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_788.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_789.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_79.root'
    ])
readFiles.extend([
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_790.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_791.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_792.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_793.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_794.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_795.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_796.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_797.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_798.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_799.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_8.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_80.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_800.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_801.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_802.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_803.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_804.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_805.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_806.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_807.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_808.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_809.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_81.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_810.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_811.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_812.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_813.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_814.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_815.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_816.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_817.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_818.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_819.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_82.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_820.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_821.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_822.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_823.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_824.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_825.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_826.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_827.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_828.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_829.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_83.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_830.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_831.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_832.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_833.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_834.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_835.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_836.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_837.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_838.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_839.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_84.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_840.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_841.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_842.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_843.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_844.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_845.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_846.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_847.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_848.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_849.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_85.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_850.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_851.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_852.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_853.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_854.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_855.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_856.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_857.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_858.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_859.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_86.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_860.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_861.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_862.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_863.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_864.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_865.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_866.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_867.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_868.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_869.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_87.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_870.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_871.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_872.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_873.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_874.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_875.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_876.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_877.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_878.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_879.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_88.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_880.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_881.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_882.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_883.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_884.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_885.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_886.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_887.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_888.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_889.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_89.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_890.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_891.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_892.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_893.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_894.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_895.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_896.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_897.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_898.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_899.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_9.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_90.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_900.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_901.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_902.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_903.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_904.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_905.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_906.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_907.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_908.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_909.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_91.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_910.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_911.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_912.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_913.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_914.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_915.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_916.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_917.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_918.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_919.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_92.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_920.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_921.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_922.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_923.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_924.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_925.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_926.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_927.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_928.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_929.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_93.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_930.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_931.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_932.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_933.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_934.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_935.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_936.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_937.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_938.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_939.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_94.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_940.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_941.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_942.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_943.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_944.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_945.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_946.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_947.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_948.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_949.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_95.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_950.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_951.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_952.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_953.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_954.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_955.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_956.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_957.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_958.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_959.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_96.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_960.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_961.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_962.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_963.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_964.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_965.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_966.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_967.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_968.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_969.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_97.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_970.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_971.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_972.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_973.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_974.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_975.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_976.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_977.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_978.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_979.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_98.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_980.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_981.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_982.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_983.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_984.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_985.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_986.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_987.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_988.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_989.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_99.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_990.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_991.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_992.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_993.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_994.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_995.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_996.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_997.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_998.root',
    'root://eoscms//eos/cms/store/user/yohay/NMSSM_Higgs_a9_H1125_H2500_H3500_WH/Summer12_DR53X_NMSSMHiggs_999.root'
    ])

process.source.inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")

#for L1GtStableParametersRcd
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('START53_V7F::All')

#for HLT selection
process.load('HLTrigger/HLTfilters/hltHighLevel_cfi')

#for mu-less jets
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
process.load("RecoTauTag.RecoTau.RecoTauPiZeroProducer_cfi")
process.load('BoostedTauAnalysis/CleanJets/cleanjets_cfi')

#define a parameter set to be passed to all modules that utilize GenTauDecayID for signal taus
commonGenTauDecayIDPSet = cms.PSet(momPDGID = cms.vint32(A_PDGID),
                                   chargedHadronPTMin = cms.double(0.0),
                                   neutralHadronPTMin = cms.double(0.0),
                                   chargedLeptonPTMin = cms.double(0.0),
                                   totalPTMin = cms.double(0.0))

#define a parameter set for the W-->munu selector
WMuNuPSet = commonGenTauDecayIDPSet.clone()
WMuNuPSet.momPDGID = cms.vint32(W_PDGID)

#define a parameter set for background W+jet jet-parton matching
WRecoilJetPSet = commonGenTauDecayIDPSet.clone()
WRecoilJetPSet.momPDGID = cms.vint32(ANY_PDGID)

# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")

# Configure PAT to use PF2PAT instead of AOD sources
# this function will modify the PAT sequences. 
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.metTools import *

PF2PATPostfix = "PFlow"
jetAlgo="AK5"
#addPfMET(process, postfixLabel=postfix)

usePF2PAT(process,runPF2PAT=True,jetAlgo=jetAlgo,runOnMC=True,postfix=PF2PATPostfix,jetCorrections=('AK5PF',['L1FastJet','L2Relative','L3Absolute']),typeIMetCorrections=True,outputModules=[])

# to use tau-cleaned jet collection uncomment the following: 
#getattr(process,"pfNoTau"+postfix).enable = True

# to switch default tau to HPS tau uncomment the following: 
#adaptPFTaus(process,"hpsPFTau",postfix=postfix)

from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties
from JetMETCorrections.Type1MET.pfMETCorrectionType0_cfi import *
runMEtUncertainties(process, electronCollection='selectedPatElectronsPFlow', muonCollection='selectedPatMuonsPFlow', tauCollection='selectedPatTausPFlow', jetCollection='selectedPatJetsPFlow',doApplyType0corr=True, doSmearJets=False, postfix='NotSmeared')

process.patPFMETtype0CorrNotSmeared=process.patPFMETtype0Corr.clone()
process.PF2PAT = cms.Sequence(
#    process.patDefaultSequence +
    getattr(process,"patPF2PATSequence"+PF2PATPostfix) +
    process.type0PFMEtCorrection + 
    process.patPFMETtype0CorrNotSmeared + 
    process.metUncertaintySequenceNotSmeared
    )

#output commands
skimEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
    "keep *",
    "drop *_*ak7*_*_*",
    "drop *_*kt4*_*_*",
    "drop *_kt6GenJets_*_*",
    "drop *_kt6CaloJets*_*_*",
    "drop *_kt6PFJetsCentral*_*_*",
    "drop *_kt6PFJets_sigma*_*",
    "drop *_kt6JetID_*_*",
    "drop *_kt6PFJets_rhos_*",
    "drop recoPFJets_kt6PFJets_*_*",
    "drop *_fixedGridRho*_*_*",
    "drop *_hfEMClusters_*_*",
    "drop *_eid*_*_*",
    "drop *_muonMETValueMapProducer_muCorrData_*",
    "drop *_muons_muonShowerInformation_*",
    "drop *_muons_combined_*",
    "drop *_muons_csc_*",
    "drop *_muons_dt_*",
    "drop l1extraL1HFRingss_*_*_*",
    "drop *_muonsFromCosmics*_*_*",
    "drop recoCaloClusters_*_*_*",
    "drop recoPreshowerCluster*_*_*_*",
    "drop *_hfRecoEcalCandidate_*_*",
    "drop *_generalV0Candidates_*_*",
    "drop *_selectDigi_*_*",
    "drop *_*BJetTags*_*_RECO",
    "drop *_*BJetTags*_*_HLT",
    "drop *_castorreco_*_*",
    "drop *_reduced*RecHits*_*_*",
    "drop *_PhotonIDProd_*_*",
    "drop *_*_*photons*_*",
    "drop *_dedx*_*_*",
    "drop *_*_cosmicsVeto_*",
    "drop *_muonTCMETValueMapProducer_*_*",
    "drop *_BeamHaloSummary_*_*",
    "drop *_caloRecoTau*_*_*",
    "drop *_GlobalHaloData_*_*",
    "drop *_hpsTancTau*_*_*",
    "drop *_shrinkingConePFTau*_*_*",
    "drop *_ak5CaloJets_*_*",
    "drop *_ak5TrackJets_*_*",
    "drop *_*_uncleanOnly*_*",
    "drop recoCaloMETs_*_*_*",
    "drop recoConversions_*_*_*",
    "drop *_CastorTowerReco_*_*",
    "drop *_uncleanedOnlyGsfElectron*_*_*",
    "drop recoJPTJets_*_*_*",
    "drop recoMETs_*_*_*",
##     "drop *_photons_*_*",
##     "drop *_photonCore_*_*",
    "drop *_ak5PFJetsRecoTauPiZeros_*_RECO",
    "drop *_ak5PFJetsRecoTauPiZeros_*_HLT",
    "drop *_hpsPFTauDiscrimination*_*_RECO",
    "drop *_hpsPFTauDiscrimination*_*_HLT",
    "drop *_hpsPFTauProducer_*_RECO",
    "drop *_hpsPFTauProducer_*_HLT",
    "drop *_recoTauAK5PFJets08Region_*_SKIM",
    "drop *_ak5PFJetTracksAssociatorAtVertex_*_SKIM",
    "drop *_ak5PFJetsLegacyHPSPiZeros_*_SKIM",
    "drop *_combinatoricRecoTausDiscriminationByLeadingPionPtCut_*_SKIM",
    "drop *_combinatoricRecoTausHPSSelector_*_SKIM",
    "drop *_hpsSelectionDiscriminator_*_SKIM",
    "drop *_combinatoricRecoTaus_*_SKIM",
    "drop *_hpsPFTauProducerSansRefs_*_SKIM",
    "drop *_pfRecoTauTagInfoProducer_*_SKIM",
    "drop *_recoTauPileUpVertices_*_SKIM",
    "drop *_towerMaker_*_*",
    "drop *_particleFlowClusterHF*_*_*",
    "drop *_pfPhotonTranslator_*_*",
    "drop *_pfElectronTranslator_*_*",
    "drop *_correctedHybridSuperClusters_*_*",
    "drop *_correctedMulti5x5SuperClustersWithPreshower_*_*",
    "drop *_*Voronoi*_*_*",
    "drop *_*phPFIsoValue*04PFIdPFIso_*_*",
    "drop *_phPFIsoDeposit*_*_*",
    "drop *_pfAll*_*_*",
    "drop *_pf*PileUp*_*_*",
    "drop *_*TagInfos*_*_*",
    "drop *_ghostTrackBJetTags_*_SKIM",
    "drop *_jet*ProbabilityBJetTags_*_SKIM",
    "drop *_simpleSecondaryVertexHigh*BJetTags_*_SKIM",
    "drop *_trackCountingHigh*BJetTags_*_SKIM",
    "drop CorrMETData_*_*_SKIM",
    "drop *_*NoNu_*_*",
    "drop *_*PFlow_*_*",
    "keep *_patType1CorrectedPFMetPFlow_*_*",
    "drop *_softElectronCands_*_*",
    "drop *_*_caloTowers_*",
    "drop *_shiftedPat*_*_*",
    "drop *_selectedPat*_*_*",
    "drop *_smearedPat*_*_*",
    "drop *_pfCandsNotInJet_*_*",
    "drop *_inclusiveMergedVertices_*_*",
    "drop *_inclusiveVertexFinder_*_*",
    "drop *_trackVertexArbitrator_*_*",
    "drop *_vertexMerger_*_*",
    "drop *_pfCandidateToVertexAssociation_*_*",
    "drop *_trackToVertexAssociation_*_*",
    "drop *_pfCandsNotInJetNotSmeared_*_*",
    "drop *_particleFlowDisplacedVertex_*_*",
    "drop *_selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0_*_*",
    "drop *_selectedVerticesForPFMEtCorrType0_*_*"
    #added 2-Jul-13 after estimating data skim size
##     "drop *_clusterSummaryProducer_*_*",
##     "drop *_hcalnoise_*_*",
##     "drop *_castorDigis_*_*",
##     "drop *_hcalDigis_*_*",
##     "drop double_ak5PFJets_rho*_*",
##     "drop double_ak5PFJets_sigma*_*",
##     "drop *_tevMuons_*_*",
##     "drop recoIsoDepositedmValueMap_*_*_*",
##     "drop *_logErrorHarvester_*_*",
##     "drop *_l1extraParticles_*_*",
##     "drop *_particleFlowTmp_*_*",
##     "drop *_particleFlowCluster*_*_*",
##     "drop *_particleFlowRecHit*_*_*",
##     "drop recoPFCandidates_CleanJets_*_SKIM"
    )
    )

# b-tagging general configuration
process.load("RecoBTag.Configuration.RecoBTag_cff")
process.load("RecoJets.JetAssociationProducers.ak5JTA_cff")
from RecoBTag.SoftLepton.softLepton_cff import *
from RecoBTag.ImpactParameter.impactParameter_cff import *
from RecoBTag.SecondaryVertex.secondaryVertex_cff import *
from RecoBTau.JetTagComputer.combinedMVA_cff import *
process.impactParameterTagInfos.jetTracks = cms.InputTag("ak5JetTracksAssociatorAtVertex")
process.ak5JetTracksAssociatorAtVertex.jets = cms.InputTag("ak5PFJets")
process.ak5JetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
process.btagging = cms.Sequence(
    process.ak5JetTracksAssociatorAtVertex*
    # impact parameters and IP-only algorithms
    process.impactParameterTagInfos*
    (process.trackCountingHighEffBJetTags +
     process.trackCountingHighPurBJetTags +
     process.jetProbabilityBJetTags +
     process.jetBProbabilityBJetTags +
     # SV tag infos depending on IP tag infos, and SV (+IP) based algos
     process.secondaryVertexTagInfos*
     (process.simpleSecondaryVertexHighEffBJetTags +
      process.simpleSecondaryVertexHighPurBJetTags +
      process.combinedSecondaryVertexBJetTags +
      process.combinedSecondaryVertexMVABJetTags) +
     process.ghostTrackVertexTagInfos*
     process.ghostTrackBJetTags)##  +
##     process.softPFMuonsTagInfos*
##     process.softPFMuonBJetTags *
##     process.softPFElectronsTagInfos*
##     process.softPFElectronBJetTags
    )

#only proceed if event is a true W-->munu event
process.genWMuNuSelector = cms.EDFilter(
    'GenObjectProducer',
    genParticleTag = cms.InputTag('genParticles'),
    absMatchPDGIDs = cms.vuint32(MU_PDGID),
    sisterAbsMatchPDGID = cms.uint32(NUMU_PDGID),
    genTauDecayIDPSet = WMuNuPSet,
    primaryTauDecayType = cms.uint32(TAU_ALL),
    sisterTauDecayType = cms.uint32(TAU_ALL),
    primaryTauPTRank = cms.int32(ANY_PT_RANK),
    primaryTauHadronicDecayType = cms.int32(TAU_ALL_HAD),
    sisterHadronicDecayType = cms.int32(TAU_ALL_HAD),
    primaryTauAbsEtaMax = cms.double(-1.0),
    primaryTauPTMin = cms.double(-1.0),
    countSister = cms.bool(False),
    applyPTCuts = cms.bool(False),
    countKShort = cms.bool(True),
    minNumGenObjectsToPassFilter = cms.uint32(1),
    makeAllCollections = cms.bool(False)
    )

#require event to fire IsoMu24_eta2p1
process.IsoMu24eta2p1Selector = process.hltHighLevel.clone()
process.IsoMu24eta2p1Selector.HLTPaths = cms.vstring('HLT_IsoMu24_eta2p1_v1',
                                                     'HLT_IsoMu24_eta2p1_v2',
                                                     'HLT_IsoMu24_eta2p1_v3',
                                                     'HLT_IsoMu24_eta2p1_v4',
                                                     'HLT_IsoMu24_eta2p1_v5',
                                                     'HLT_IsoMu24_eta2p1_v6',
                                                     'HLT_IsoMu24_eta2p1_v7',
                                                     'HLT_IsoMu24_eta2p1_v8',
                                                     'HLT_IsoMu24_eta2p1_v9',
                                                     'HLT_IsoMu24_eta2p1_v10',
                                                     'HLT_IsoMu24_eta2p1_v11',
                                                     'HLT_IsoMu24_eta2p1_v12',
                                                     'HLT_IsoMu24_eta2p1_v13',
                                                     'HLT_IsoMu24_eta2p1_v14',
                                                     'HLT_IsoMu24_eta2p1_v15')
process.IsoMu24eta2p1Selector.throw = cms.bool(False)

#search for a muon with pT > 25 GeV as in WHbb CMS AN-2012/349 and proceed if one can be found
#this will produce a ref to the original muon collection
process.WMuonPTSelector = cms.EDFilter('MuonRefSelector',
                                       src = cms.InputTag('muons'),
                                       cut = cms.string('pt > 25.0'),
                                       filter = cms.bool(True)
                                       )

#produce photon isolations
from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFPhotonIso
process.phoIsoSequence = setupPFPhotonIso(process, 'photons')

#search for a tight PF isolated tight muon in |eta| < 2.1 with pT > 25 GeV
#(see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Muon_Isolation_AN1 for
#isolation definition; CMS AN-2012/349 uses loose isolation working point for WHbb muon selection)
#this will produce a ref to the original muon collection
process.WIsoMuonSelector = cms.EDFilter('CustomMuonSelector',
                                        baseMuonTag = cms.InputTag('muons'),
                                        muonTag = cms.InputTag('WMuonPTSelector'),
                                        vtxTag = cms.InputTag('offlinePrimaryVertices'),
                                        muonID = cms.string('tight'),
                                        PFIsoMax = cms.double(0.12),
                                        detectorIsoMax = cms.double(-1.0),
                                        PUSubtractionCoeff = cms.double(0.5),
                                        usePFIso = cms.bool(True),
                                        passIso = cms.bool(True),
                                        etaMax = cms.double(2.1),
                                        minNumObjsToPassFilter = cms.uint32(1)
                                        )

#search for a muon with pT > 5 GeV as in HZZ4l analysis and proceed if one can be found
#this will produce a ref to the original muon collection
process.tauMuonPTSelector = cms.EDFilter('MuonRefSelector',
                                         src = cms.InputTag('muons'),
                                         cut = cms.string('pt > 5.0'),
                                         filter = cms.bool(True)
                                         )

#search for soft muons
#(see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Soft_Muon) not overlapping with
#the W muon in |eta| < 2.4
#this will produce a ref to the original muon collection
process.tauMuonSelector = cms.EDFilter('CustomMuonSelector',
                                       baseMuonTag = cms.InputTag('muons'),
                                       muonTag = cms.InputTag('tauMuonPTSelector'),
                                       vtxTag = cms.InputTag('offlinePrimaryVertices'),
                                       vetoMuonTag = cms.InputTag('WIsoMuonSelector'),
                                       muonID = cms.string('soft'),
                                       PFIsoMax = cms.double(0.2),
                                       detectorIsoMax = cms.double(-1.0),
                                       PUSubtractionCoeff = cms.double(0.5),
                                       usePFIso = cms.bool(True),
                                       passIso = cms.bool(True),
                                       etaMax = cms.double(2.4),
                                       minNumObjsToPassFilter = cms.uint32(1)
                                       )

#clean the jets of soft muons, then rebuild the taus
process.CleanJets.muonSrc = cms.InputTag('tauMuonSelector')
process.CleanJets.PFCandSrc = cms.InputTag('particleFlow')
process.CleanJets.cutOnGenMatches = cms.bool(False)
process.CleanJets.outFileName = cms.string('NMSSMSignal_MuProperties_SAMPLE_VERSION.root')
process.recoTauAK5PFJets08Region.src = cms.InputTag("CleanJets", "ak5PFJetsNoMu", "SKIM")
process.ak5PFJetsRecoTauPiZeros.jetSrc = cms.InputTag("CleanJets", "ak5PFJetsNoMu", "SKIM")
process.combinatoricRecoTaus.jetSrc = cms.InputTag("CleanJets", "ak5PFJetsNoMu", "SKIM")
process.ak5PFJetTracksAssociatorAtVertex.jets = cms.InputTag("CleanJets", "ak5PFJetsNoMu",
                                                             "SKIM")
process.ak5PFJetsLegacyHPSPiZeros.jetSrc = cms.InputTag("CleanJets", "ak5PFJetsNoMu", "SKIM")
process.recoTauCommonSequence = cms.Sequence(process.CleanJets*
                                             process.ak5PFJetTracksAssociatorAtVertex*
                                             process.recoTauAK5PFJets08Region*
                                             process.recoTauPileUpVertices*
                                             process.pfRecoTauTagInfoProducer
                                             )
process.PFTau = cms.Sequence(process.recoTauCommonSequence*process.recoTauClassicHPSSequence)

#find taus in |eta| < 2.4 matched to muon-tagged cleaned jets that pass the medium isolation
#discriminator
#this will produce a ref to the cleaned tau collection
process.muHadIsoTauSelector = cms.EDFilter(
    'CustomTauSepFromMuonSelector',
    baseTauTag = cms.InputTag('hpsPFTauProducer', '', 'SKIM'),
    tauHadIsoTag = cms.InputTag('hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr', '',
                                'SKIM'),
    tauDiscriminatorTags = cms.VInputTag(
    cms.InputTag('hpsPFTauDiscriminationByDecayModeFinding', '', 'SKIM'), 
    cms.InputTag('hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr', '', 'SKIM')
    ),
    jetTag = cms.InputTag('CleanJets', 'ak5PFJetsNoMu', 'SKIM'),
    muonRemovalDecisionTag = cms.InputTag('CleanJets'),
    overlapCandTag = cms.InputTag('WIsoMuonSelector'),
    passDiscriminator = cms.bool(True),
    etaMax = cms.double(2.4),
    isoMax = cms.double(-1.0),
    dR = cms.double(0.5),
    minNumObjsToPassFilter = cms.uint32(1)
    )

#find taus in |eta| < 2.4 matched to muon-tagged cleaned jets
#this will produce a ref to the cleaned tau collection
process.muHadTauSelector = cms.EDFilter(
    'CustomTauSepFromMuonSelector',
    baseTauTag = cms.InputTag('hpsPFTauProducer', '', 'SKIM'),
    tauHadIsoTag = cms.InputTag('hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr', '',
                                'SKIM'),
    tauDiscriminatorTags = cms.VInputTag(
    cms.InputTag('hpsPFTauDiscriminationByDecayModeFinding', '', 'SKIM')
    ),
    jetTag = cms.InputTag('CleanJets', 'ak5PFJetsNoMu', 'SKIM'),
    muonRemovalDecisionTag = cms.InputTag('CleanJets'),
    overlapCandTag = cms.InputTag('WIsoMuonSelector'),
    passDiscriminator = cms.bool(True),
    pTMin = cms.double(0.0),
    etaMax = cms.double(2.4),
    isoMax = cms.double(-1.0),
    dR = cms.double(0.5),
    minNumObjsToPassFilter = cms.uint32(1)
    )

#find taus in |eta| < 2.4 matched to muon-tagged cleaned jets that fail the medium isolation
#discriminator
#this will produce a ref to the cleaned tau collection
process.muHadNonIsoTauSelector = cms.EDFilter(
    'CustomTauSepFromMuonSelector',
    tauTag = cms.InputTag('muHadTauSelector'),
    baseTauTag = cms.InputTag('hpsPFTauProducer', '', 'SKIM'),
    tauHadIsoTag = cms.InputTag('hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr', '',
                                'SKIM'),
    tauDiscriminatorTags = cms.VInputTag(
    cms.InputTag('hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr', '', 'SKIM')
    ),
    jetTag = cms.InputTag('CleanJets', 'ak5PFJetsNoMu', 'SKIM'),
    muonRemovalDecisionTag = cms.InputTag('CleanJets'),
    overlapCandTag = cms.InputTag('WIsoMuonSelector'),
    passDiscriminator = cms.bool(False),
    etaMax = cms.double(2.4),
    isoMax = cms.double(-1.0),
    dR = cms.double(0.5),
    minNumObjsToPassFilter = cms.uint32(1)
    )

process.tauShiftProducer = cms.EDProducer(
    'TauEnergyShifter',
#    baseTauTag = cms.InputTag('hpsPFTauProducer', '', 'SKIM'),
    tauTag = cms.InputTag('muHadTauSelector'),
    pTMin = cms.double(10.),
    pTShift = cms.double(0.03)
    )

#output
process.selectedOutput = cms.OutputModule(
    "PoolOutputModule",
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
    outputCommands = skimEventContent.outputCommands,
    fileName = cms.untracked.string(
    '/data1/' + USER + '/Wh1_Medium/EDM_files/data_selected_a9_VERSION.root'
    )
    )
process.antiSelectedOutput = cms.OutputModule(
    "PoolOutputModule",
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
    outputCommands = skimEventContent.outputCommands,
    fileName = cms.untracked.string(
    '/data1/' + USER + '/Wh1_Medium/EDM_files/data_anti-selected_a9_VERSION.root'
    )
    )
process.noSelectedOutput = cms.OutputModule(
    "PoolOutputModule",
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
    outputCommands = skimEventContent.outputCommands,
    fileName = cms.untracked.string(
    '/data1/' + USER + '/Wh1_Medium/EDM_files/data_no_selection_a9_VERSION.root'
    )
    )

#sequences
process.antiSelectionSequence = cms.Sequence(process.IsoMu24eta2p1Selector*
                                             process.WMuonPTSelector*
                                             process.WIsoMuonSelector*
                                             process.tauMuonPTSelector*
                                             process.tauMuonSelector*
                                             process.PFTau*
                                             process.muHadTauSelector*
                                             process.muHadNonIsoTauSelector*
                                             process.btagging*
                                             process.pfParticleSelectionSequence*
                                             process.phoIsoSequence)
process.selectionSequence = cms.Sequence(process.IsoMu24eta2p1Selector*
                                         process.WMuonPTSelector*
                                         process.WIsoMuonSelector*
                                         process.tauMuonPTSelector*
                                         process.tauMuonSelector*
                                         process.PFTau*
                                         process.muHadIsoTauSelector*
                                         process.btagging*
                                         process.pfParticleSelectionSequence*
                                         process.phoIsoSequence)
process.noSelectionSequence = cms.Sequence(process.IsoMu24eta2p1Selector*
                                           process.WMuonPTSelector*
                                           process.WIsoMuonSelector*
                                           process.PF2PAT*
                                           process.tauMuonPTSelector*
                                           process.tauMuonSelector*
                                           process.PFTau*
                                           process.muHadTauSelector*
                                           process.tauShiftProducer*
                                           process.btagging*
                                           process.pfParticleSelectionSequence*
                                           process.phoIsoSequence)

## #selection path
## process.p = cms.Path(process.selectionSequence)
## process.e = cms.EndPath(process.selectedOutput)

#anti-selection path
## process.p = cms.Path(process.antiSelectionSequence)
## process.e = cms.EndPath(process.antiSelectedOutput)

#no selection path
process.p = cms.Path(process.noSelectionSequence)
process.e = cms.EndPath(process.noSelectedOutput)
