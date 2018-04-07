import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( 
    #SkipEvent = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True) 
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )    


process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")
#process.load('HLTrigger.Configuration.HLT_Effcy_cff')

# process.Tracer = cms.Service('Tracer')

import os
if "CMSSW_7_6_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('76X_dataRun2_v15')
    process.source.fileNames = [
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/0013A0EA-94AE-E511-9B84-001E67398683.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/02A9F67F-A2AE-E511-939A-0CC47A4C8EB6.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/02D39573-BDAE-E511-AF22-00266CF9AF00.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/0639B2A3-A7AE-E511-887E-A0000420FE80.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/06C00544-AAAE-E511-831D-00A0D1EE2BBC.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/06DCCB30-C7AE-E511-A318-0025905A6092.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/0ADF8F02-94AE-E511-96F0-549F358EB72E.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/0C78D007-95AE-E511-87A9-0CC47A4DEDCA.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/10438105-95AE-E511-ADCD-0090FAA59634.root',
        '/store/data/Run2015D/Charmonium/AOD/16Dec2015-v1/50000/1077A155-AAAE-E511-A1C7-0CC47A4DEF3E.root',
    ]
elif "CMSSW_8_0_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('80X_dataRun2_2016SeptRepro_v4')
    process.source.fileNames = [
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/0006BA63-7097-E611-BBE8-001E67E71412.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/0018FFBA-5B94-E611-AD99-008CFAFBF52E.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/003343EB-7496-E611-B5EC-848F69FD2997.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/0060EAA8-9197-E611-9D75-001E67E59BE3.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/00E2CD87-9798-E611-8CA4-848F69FD4598.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/020BB297-5B97-E611-82B5-848F69FD4541.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/04CA2B1A-0897-E611-A716-0025907FD242.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/06069075-3C97-E611-92D8-008CFA00018C.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/061698EB-E096-E611-840C-848F69FD3EC9.root',
        '/store/data/Run2016G/Charmonium/AOD/23Sep2016-v1/100000/062B282E-8097-E611-9710-001E67E6F86E.root',
    ]
    #process.source.fileNames = [ 'file:/tmp/gpetrucc/0006BA63-7097-E611-BBE8-001E67E71412.root' ]
    import FWCore.PythonUtilities.LumiList as LumiList
    json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    process.source.lumisToProcess = LumiList.LumiList(filename = json).getVLuminosityBlockRange()
elif "CMSSW_10_0_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('100X_dataRun2_relval_ForTSG_v1')
    process.source.fileNames = [
        'root://eoscms//eos/cms/store/group/phys_bphys/fiorendi/13TeV/data2017/Charmonium/crab_skim_Mu7p5_TrackX/180323_140349/0000/skim_1.root',
        'root://eoscms//eos/cms/store/group/phys_bphys/fiorendi/13TeV/data2017/Charmonium/crab_skim_Mu7p5_TrackX/180323_140349/0000/skim_2.root',
        'root://eoscms//eos/cms/store/group/phys_bphys/fiorendi/13TeV/data2017/Charmonium/crab_skim_Mu7p5_TrackX/180323_140349/0000/skim_3.root',
        'root://eoscms//eos/cms/store/group/phys_bphys/fiorendi/13TeV/data2017/Charmonium/crab_skim_Mu7p5_TrackX/180323_140349/0000/skim_4.root',
        'root://eoscms//eos/cms/store/group/phys_bphys/fiorendi/13TeV/data2017/Charmonium/crab_skim_Mu7p5_TrackX/180323_140349/0000/skim_5.root',
        'root://eoscms//eos/cms/store/group/phys_bphys/fiorendi/13TeV/data2017/Charmonium/crab_skim_Mu7p5_TrackX/180323_140349/0000/skim_6.root',
        'root://eoscms//eos/cms/store/group/phys_bphys/fiorendi/13TeV/data2017/Charmonium/crab_skim_Mu7p5_TrackX/180323_140349/0000/skim_7.root',

        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/90C4F902-C5EB-E711-9A7F-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/4C1DBF2E-C4EB-E711-BEDB-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/2EB6F26B-CEEB-E711-B7A4-0242AC1C0503.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/34F78254-CDEB-E711-87CE-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/CEBCF487-D2EB-E711-A50D-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/64895734-0BEC-E711-ADA2-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/D4C260E4-11EC-E711-8A6F-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/8E8F87C4-1AEC-E711-B183-0242AC1C0503.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/0A61E009-1BEC-E711-B1BC-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/200D6CE1-45EC-E711-8E22-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/D63543D0-55EC-E711-83A2-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/24F89A3A-4DEB-E711-8A69-0CC47A545060.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/D25F2679-17EC-E711-80AC-0CC47A166D66.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/BA72E421-56EC-E711-9567-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/E036BF2B-CEEB-E711-884E-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/8439F870-D6EB-E711-A7CE-0242AC1C0503.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/EE708871-D6EB-E711-A505-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/D6ACBF7A-D6EB-E711-83ED-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/605A9307-0CEC-E711-97D6-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/E22C934F-0BEC-E711-932B-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/EEFE0B56-12EC-E711-842B-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/A6AACBB6-10EC-E711-9F2A-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/C427FC5A-46EC-E711-B3DE-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/AA694811-44EC-E711-AF45-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/660A32A1-9BEB-E711-9FA7-003048C6B51A.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/5E40482F-E2EB-E711-BEBA-0CC47AE0F33A.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/14A46CD2-32EC-E711-A24E-C4346BC84780.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/0E6CC526-9CEB-E711-B6A8-001E67F67372.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/6E9327D8-32EC-E711-A682-008CFAF7455E.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60001/0C5262C4-A4EC-E711-9678-7845C4FC3638.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60001/D6900D2E-E6EC-E711-A967-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/1EF3296F-C6EB-E711-BDA8-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/F4A2A4E1-D5EB-E711-AD75-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/F0993B01-DCEB-E711-8C05-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/C68E4F7E-E4EB-E711-B7A1-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/D4BF2BCC-0CEC-E711-AD4B-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/A6A7A353-12EC-E711-AED9-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/88576753-12EC-E711-8FEC-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/58D74C52-10EC-E711-BD4B-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/6C3D67EA-10EC-E711-9F72-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/A0F2135B-46EC-E711-AD12-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/82405FDA-32EC-E711-82D9-7CD30AD09DD2.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/06BAC455-CDEB-E711-BC9C-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/3233B87F-DDEB-E711-A905-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/52557D6D-01EC-E711-9DE3-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/7C178500-0CEC-E711-BE42-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/EA22D25C-0CEC-E711-A1D9-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/48DB7278-0CEC-E711-960A-0242AC1C0503.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/8CF10032-10EC-E711-8113-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/042CB0AE-9BEB-E711-AF44-0CC47A166D66.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60001/10BD40DB-5EEC-E711-B865-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60001/4EE3D535-60EC-E711-8FFA-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/66CEDF4B-0BEC-E711-A9EB-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/5C1C0EC0-10EC-E711-8E1D-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/424A6F3B-1BEC-E711-BEDB-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/3A99C54D-1BEC-E711-9130-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/866B1095-24EC-E711-8BE5-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/36175C0F-44EC-E711-8718-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/36DD5B15-46EC-E711-980F-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60001/A8DFD822-56EC-E711-81EA-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/74599962-56EC-E711-BFB7-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/B44FC13C-56EB-E711-B584-0CC47A5450DA.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/9ADFE057-CDEB-E711-8BD6-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/92BEE513-D6EB-E711-8F24-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/86AC3D61-12EC-E711-B1C5-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/C26B96DE-45EC-E711-A5D5-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/FEC90035-45EC-E711-B39B-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/044A0E12-43EC-E711-8D0F-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/E8500C7E-43EC-E711-8E8C-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/101FD332-45EC-E711-977B-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60001/D833394C-57EC-E711-B2A4-0242AC1C0502.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/BCDD9FFE-55EC-E711-A1E5-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/EAE15942-DBEB-E711-BA27-0CC47AE0F33A.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60001/2648ABCA-5EEC-E711-9372-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/18B2C069-D1EB-E711-8086-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/1ECB494B-01EC-E711-8897-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/F09C1728-12EC-E711-9C7D-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/4C899BAD-10EC-E711-8E73-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/E0084C10-44EC-E711-B472-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/F287F7EE-55EC-E711-8FD6-0242AC1C0501.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/DAC8EBD6-55EC-E711-B757-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/0CE2F8D8-55EC-E711-A068-0242AC1C0500.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/EA627B92-B1EB-E711-B07A-B4E10FD21863.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/C888C21F-33EC-E711-A51A-008CFAFBDE0C.root',
        #'/store/data/Run2017E/Charmonium/AOD/17Nov2017-v1/60000/286320D8-32EC-E711-9ABD-7CD30AD09010.root',

        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/EE4F78E1-5FB0-E711-90A3-02163E014585.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/60DEC355-45B0-E711-BBC5-02163E01459D.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/C656433D-46B0-E711-996C-02163E01341E.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/800245A2-47B0-E711-93C7-02163E0141D6.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/408ED252-45B0-E711-9E9E-02163E014705.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/6C7A183F-46B0-E711-B6B7-02163E012611.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/DE9D77F9-46B0-E711-8048-02163E01A67E.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/CCF7EC41-46B0-E711-9E8E-02163E01A331.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/28CF33A0-9AB0-E711-AD2B-02163E01462C.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/C6B7C10C-47B0-E711-9BFB-02163E01A61B.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/CC1F3107-47B0-E711-A425-02163E019CE6.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/8437C608-BDB0-E711-A8E2-02163E01A6E2.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/189A4613-46B0-E711-94DB-02163E01465A.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/CCE0AAA8-47B0-E711-9F43-02163E01231F.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/44AB37DA-46B0-E711-B880-02163E01366D.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/2AF825D1-47B0-E711-911D-02163E011FBE.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/2A1C77FD-46B0-E711-BD27-02163E013521.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/90E986B9-47B0-E711-8AB5-02163E014355.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/4ED7515E-45B0-E711-80F0-02163E01375A.root',
        #'/store/data/Run2017E/Charmonium/AOD/PromptReco-v1/000/304/777/00000/72406E59-46B0-E711-9BA6-02163E019DC4.root',

        #'/store/data/Run2017E/HLTPhysics/AOD/PromptReco-v1/000/304/778/00000/B8E8FA7D-65B0-E711-A9E1-02163E014195.root'
        #'/store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/0EF64D35-5CB0-E711-9056-02163E0142F3.root',
        #'/store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/1E5146A6-69B0-E711-BE27-02163E0133A4.root',
        #'/store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/3C0373C5-B1B0-E711-A901-02163E014206.root',
    ]
    print 'OK!'
else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']

## ==== Fast Filters ====
process.goodVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
    filter = cms.bool(True),
)
process.noScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)

process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
process.triggerResultsFilter.triggerConditions = cms.vstring( 'HLT_Mu*_L2Mu*' )
process.triggerResultsFilter.l1tResults = ''
process.triggerResultsFilter.throw = True
#process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", "HLT" )
process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", "HLT2" )
process.HLTMu   = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*' ])
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_Mu*_L2Mu*', 'HLT_Mu*_Track*_Jpsi*' ])
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_DoubleMu4_JpsiTrk_Displaced_v*', 'HLT_DoubleMu4_Jpsi_Displaced_v*', 'HLT_Mu7p5_Track2_Jpsi_v*', 'HLT_Mu3*', 'HLT_Dimuon25_Jpsi_v*', 'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v*' ])
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_DoubleMu4_Jpsi*', 'HLT_Mu7p5_Track2_Jpsi*', 'HLT_Mu*_L2Mu*', 'HLT_Mu3*', 'HLT_Dimuon25_Jpsi*', 'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R*' ])
process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = [ 'HLT_DoubleMu4_Jpsi*', 'HLT_Mu7p5_Track2_Jpsi*', 'HLT_Mu3_v*', 'HLT_Dimuon25_Jpsi*', 'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R*' ])
#process.HLTBoth = process.triggerResultsFilter.clone(triggerConditions = ['HLT_Mu3_v*'])

#HLT_DoubleMu4_JpsiTrk_Displaced_v*,
#HLT_DoubleMu4_Jpsi_Displaced_v*,
#HLT_Mu7p5_Track2_Jpsi_v*,
#HLT_Mu3*,
#HLT_Dimuon25_Jpsi_v*,
#HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v*

process.fastFilter = cms.Sequence(process.goodVertexFilter + process.noScraping)
## ==== Merge CaloMuons and Tracks into the collection of reco::Muons  ====
from RecoMuon.MuonIdentification.calomuons_cfi import calomuons;
process.mergedMuons = cms.EDProducer("CaloMuonMerger",
    mergeTracks = cms.bool(True),
    mergeCaloMuons = cms.bool(False), # AOD
    muons     = cms.InputTag("muons"), 
    caloMuons = cms.InputTag("calomuons"),
    tracks    = cms.InputTag("generalTracks"),
    minCaloCompatibility = calomuons.minCaloCompatibility,
    ## Apply some minimal pt cut
    muonsCut     = cms.string("pt > 2 && track.isNonnull"),
    caloMuonsCut = cms.string("pt > 2"),
    tracksCut    = cms.string("pt > 2"),
)

## ==== Trigger matching
process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
## with some customization
from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import *
changeRecoMuonInput(process, "mergedMuons")
useL1Stage2Candidates(process)
appendL1MatchingAlgo(process)
#addHLTL1Passthrough(process)

from MuonAnalysis.TagAndProbe.common_variables_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("(isGlobalMuon || numberOfMatchedStations > 1) && pt > 5 && !triggerObjectMatchesByCollection('hltIterL3MuonCandidates').empty()"),
)

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string("track.isNonnull && (!triggerObjectMatchesByCollection('hltTracksIter').empty() || !triggerObjectMatchesByCollection('hltMuTrackJpsiEffCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltMuTrackJpsiCtfTrackCands').empty() || !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty())"),
)

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    cut = cms.string('2.8 < mass < 3.4 && abs(daughter(0).vz - daughter(1).vz) < 1'),
    decay = cms.string('tagMuons@+ probeMuons@-')
)
process.onePair = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairs"), minNumber = cms.uint32(1))

from MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cff import ExtraIsolationVariables

process.tpTree = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # choice of tag and probe pairs, and arbitration
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("None"),
    # probe variables: all useful ones
    variables = cms.PSet(
        AllVariables,
        ExtraIsolationVariables,
        dxyBS = cms.InputTag("muonDxyPVdzmin","dxyBS"),
        dxyPVdzmin = cms.InputTag("muonDxyPVdzmin","dxyPVdzmin"),
        dzPV = cms.InputTag("muonDxyPVdzmin","dzPV"),
        nSplitTk  = cms.InputTag("splitTrackTagger"),
    ),
    flags = cms.PSet(
       TrackQualityFlags,
       MuonIDFlags,
       HighPtTriggerFlags,
       HighPtTriggerFlagsDebug,
       LowPtTriggerFlagsPhysics,
       LowPtTriggerFlagsEfficienciesProbe,
       Acc_JPsi = cms.string("(abs(eta) <= 1.3 && pt > 3.3) || (1.3 < abs(eta) <= 2.2 && p > 2.9) || (2.2 < abs(eta) <= 2.4  && pt > 0.8)"),
    ),
    tagVariables = cms.PSet(
        pt  = cms.string('pt'),
        eta = cms.string('eta'),
        phi = cms.string('phi'),
        nVertices = cms.InputTag("nverticesModule"),
        l1rate = cms.InputTag("l1rate"),
        bx     = cms.InputTag("l1rate","bx"),
        instLumi = cms.InputTag("addEventInfo", "instLumi"),
    ),
    tagFlags     = cms.PSet(
        HighPtTriggerFlags,
        HighPtTriggerFlagsDebug,
        LowPtTriggerFlagsPhysics,
        LowPtTriggerFlagsEfficienciesTag,
    ),
    pairVariables = cms.PSet(
        pt = cms.string("pt"),
        dphiVtxTimesQ = cms.InputTag("tagProbeSeparation", "dphiVtxTimesQ"),
        drM1          = cms.InputTag("tagProbeSeparation", "drM1"),
        dphiM1        = cms.InputTag("tagProbeSeparation", "dphiM1"),
        distM1        = cms.InputTag("tagProbeSeparation", "distM1"),
        drM2          = cms.InputTag("tagProbeSeparation", "drM2"),
        dphiM2        = cms.InputTag("tagProbeSeparation", "dphiM2"),
        distM2        = cms.InputTag("tagProbeSeparation", "distM2"),
        drVtx         = cms.InputTag("tagProbeSeparation", "drVtx"),
        dz            = cms.string("daughter(0).vz - daughter(1).vz"),
        probeMultiplicity = cms.InputTag("probeMultiplicity"),
    ),
    pairFlags = cms.PSet(),
    isMC           = cms.bool(False),
    addRunLumiInfo = cms.bool(True),
)


process.load("MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cfi")

process.tnpSimpleSequence = cms.Sequence(
    process.tagMuons +
    process.oneTag     +
    process.probeMuons +
    process.tpPairs    +
    process.onePair    +
    process.muonDxyPVdzmin +
    process.nverticesModule +
    process.tagProbeSeparation +
    process.computeCorrectedIso + 
    process.probeMultiplicity + 
    process.splitTrackTagger +
    process.addEventInfo +
    process.l1rate +
    process.tpTree
)

#process.tagAndProbe = cms.Path( 
process.tagAndProbe = cms.EndPath( 
    process.HLTBoth    +
    process.fastFilter +
    process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequence
)

#tagAndProbe_ = process.tagAndProbe
#print tagAndProbe_

##    _____               _    _             
##   |_   _| __ __ _  ___| | _(_)_ __   __ _ 
##     | || '__/ _` |/ __| |/ / | '_ \ / _` |
##     | || | | (_| | (__|   <| | | | | (_| |
##     |_||_|  \__,_|\___|_|\_\_|_| |_|\__, |
##                                     |___/ 

## Then make another collection for standalone muons, using standalone track to define the 4-momentum
process.muonsSta = cms.EDProducer("RedefineMuonP4FromTrack",
    src   = cms.InputTag("muons"),
    track = cms.string("outer"),
)
## Match to trigger, to measure the efficiency of HLT tracking
from PhysicsTools.PatAlgos.tools.helpers import *
process.patMuonsWithTriggerSequenceSta = cloneProcessingSnippet(process, process.patMuonsWithTriggerSequence, "Sta")
process.muonMatchHLTL2Sta.maxDeltaR = 0.5
process.muonMatchHLTL3Sta.maxDeltaR = 0.5
massSearchReplaceAnyInputTag(process.patMuonsWithTriggerSequenceSta, "mergedMuons", "muonsSta")

## Define probes and T&P pairs
process.probeMuonsSta = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTriggerSta"),
    cut = cms.string("outerTrack.isNonnull && !triggerObjectMatchesByCollection('hltL2MuonCandidates').empty()"), 
)

process.tpPairsSta = process.tpPairs.clone(decay = "tagMuons@+ probeMuonsSta@-", cut = "2 < mass < 5")

process.onePairSta = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairsSta"), minNumber = cms.uint32(1))

process.load("MuonAnalysis.TagAndProbe.tracking_reco_info_cff")

process.tpTreeSta = process.tpTree.clone(
    tagProbePairs = "tpPairsSta",
    variables = cms.PSet(
        KinematicVariables, 
        ## track matching variables
        tk_deltaR     = cms.InputTag("staToTkMatch","deltaR"),
        tk_deltaEta   = cms.InputTag("staToTkMatch","deltaEta"),
        tk_deltaR_NoJPsi     = cms.InputTag("staToTkMatchNoJPsi","deltaR"),
        tk_deltaEta_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi","deltaEta"),
        tk_deltaR_NoBestJPsi     = cms.InputTag("staToTkMatchNoBestJPsi","deltaR"),
        tk_deltaEta_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi","deltaEta"),
    ),
    flags = cms.PSet(
        LowPtTriggerFlagsEfficienciesProbe,
        outerValidHits = cms.string("outerTrack.numberOfValidHits > 0"),
        TM  = cms.string("isTrackerMuon"),
        Glb = cms.string("isGlobalMuon"),
    ),
    tagVariables = cms.PSet(
        pt = cms.string("pt"),
        eta = cms.string("eta"),
        phi = cms.string("phi"),
        nVertices = cms.InputTag("nverticesModule"),
        combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
        chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
        neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
        photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
        combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
    ),
    tagFlags = cms.PSet(
        LowPtTriggerFlagsEfficienciesTag,
        LowPtTriggerFlagsEfficienciesProbe,
    ),
    pairVariables = cms.PSet(),
    pairFlags     = cms.PSet(),
)

process.tnpSimpleSequenceSta = cms.Sequence(
    process.tagMuons +
    process.oneTag     +
    process.probeMuonsSta +
    process.tpPairsSta      +
    process.onePairSta      +
    process.nverticesModule +
    process.staToTkMatchSequenceJPsi +
    process.addEventInfo +
    process.l1rate +
    process.tpTreeSta
)

## Add extra RECO-level info
if False:
    process.tnpSimpleSequenceSta.replace(process.tpTreeSta, process.tkClusterInfo+process.tpTreeSta)
    process.tpTreeSta.tagVariables.nClustersStrip = cms.InputTag("tkClusterInfo","siStripClusterCount")
    process.tpTreeSta.tagVariables.nClustersPixel = cms.InputTag("tkClusterInfo","siPixelClusterCount")
    process.tnpSimpleSequenceSta.replace(process.tpTreeSta, process.tkLogErrors+process.tpTreeSta)
    process.tpTreeSta.tagVariables.nLogErrFirst = cms.InputTag("tkLogErrors","firstStep")
    process.tpTreeSta.tagVariables.nLogErrPix   = cms.InputTag("tkLogErrors","pixelSteps")
    process.tpTreeSta.tagVariables.nLogErrAny   = cms.InputTag("tkLogErrors","anyStep")

if True: # turn on for tracking efficiency from RECO/AOD + earlyGeneralTracks
    process.tracksNoMuonSeeded = cms.EDFilter("TrackSelector",
      src = cms.InputTag("generalTracks"),
      cut = cms.string(" || ".join("isAlgoInMask('%s')" % a for a in [
                    'initialStep', 'lowPtTripletStep', 'pixelPairStep', 'detachedTripletStep',
                    'mixedTripletStep', 'pixelLessStep', 'tobTecStep', 'jetCoreRegionalStep' ] ) )
    )
    process.pCutTracks0 = process.pCutTracks.clone(src = 'tracksNoMuonSeeded')
    process.tkTracks0 = process.tkTracks.clone(src = 'pCutTracks0')
    process.tkTracksNoJPsi0 = process.tkTracksNoJPsi.clone(src = 'tkTracks0')
    process.tkTracksNoBestJPsi0 = process.tkTracksNoBestJPsi.clone(src = 'tkTracks0')
    process.preTkMatchSequenceJPsi.replace(
            process.tkTracksNoJPsi, process.tkTracksNoJPsi +
            process.tracksNoMuonSeeded + process.pCutTracks0 + process.tkTracks0 + process.tkTracksNoJPsi0 +process.tkTracksNoBestJPsi0
    )
    process.staToTkMatch0 = process.staToTkMatch.clone(matched = 'tkTracks0')
    process.staToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi.clone(matched = 'tkTracksNoJPsi0')
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatch, process.staToTkMatch + process.staToTkMatch0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoJPsi, process.staToTkMatchNoJPsi + process.staToTkMatchNoJPsi0 )
    process.staToTkMatchSequenceJPsi.replace( process.staToTkMatchNoBestJPsi, process.staToTkMatchNoBestJPsi + process.staToTkMatchNoBestJPsi0 )
    process.tpTreeSta.variables.tk0_deltaR     = cms.InputTag("staToTkMatch0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta   = cms.InputTag("staToTkMatch0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoJPsi   = cms.InputTag("staToTkMatchNoJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoJPsi = cms.InputTag("staToTkMatchNoJPsi0","deltaEta")
    process.tpTreeSta.variables.tk0_deltaR_NoBestJPsi   = cms.InputTag("staToTkMatchNoBestJPsi0","deltaR")
    process.tpTreeSta.variables.tk0_deltaEta_NoBestJPsi = cms.InputTag("staToTkMatchNoBestJPsi0","deltaEta")

process.tagAndProbeSta = cms.Path( 
    process.HLTMu      +
    process.fastFilter +
    process.muonsSta                       +
    process.patMuonsWithTriggerSequenceSta +
    process.tnpSimpleSequenceSta
)



if False: # turn on for tracking efficiency using L1 seeds
    process.probeL1 = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("l1extraParticles"),
        cut = cms.string("pt >= 2 && abs(eta) < 2.4"),
    )
    process.tpPairsTkL1 = process.tpPairs.clone(decay = "tagMuons@+ probeL1@-", cut = 'mass > 2')
    process.l1ToTkMatch    = process.staToTkMatch.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi = process.staToTkMatchNoJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi = process.staToTkMatchNoBestJPsi.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatch0    = process.staToTkMatch0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoJPsi0 = process.staToTkMatchNoJPsi0.clone(src = "probeL1", srcTrack="none")
    process.l1ToTkMatchNoBestJPsi0 = process.staToTkMatchNoBestJPsi0.clone(src = "probeL1", srcTrack="none")
    process.tpTreeL1 = process.tpTreeSta.clone(
        tagProbePairs = "tpPairsTkL1",
        arbitration   = "OneProbe",
        variables = cms.PSet(
            KinematicVariables,
            bx = cms.string("bx"),
            quality = cms.string("gmtMuonCand.quality"),
            ## track matching variables
            tk_deltaR     = cms.InputTag("l1ToTkMatch","deltaR"),
            tk_deltaEta   = cms.InputTag("l1ToTkMatch","deltaEta"),
            tk_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi","deltaR"),
            tk_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi","deltaEta"),
            tk_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaR"),
            tk_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi","deltaEta"),
            ## track matching variables (early general tracks)
            tk0_deltaR     = cms.InputTag("l1ToTkMatch0","deltaR"),
            tk0_deltaEta   = cms.InputTag("l1ToTkMatch0","deltaEta"),
            tk0_deltaR_NoJPsi   = cms.InputTag("l1ToTkMatchNoJPsi0","deltaR"),
            tk0_deltaEta_NoJPsi = cms.InputTag("l1ToTkMatchNoJPsi0","deltaEta"),
            tk0_deltaR_NoBestJPsi   = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaR"),
            tk0_deltaEta_NoBestJPsi = cms.InputTag("l1ToTkMatchNoBestJPsi0","deltaEta"),
        ),
        flags = cms.PSet(
        ),
        tagVariables = cms.PSet(
            pt = cms.string("pt"),
            eta = cms.string("eta"),
            phi = cms.string("phi"),
            nVertices   = cms.InputTag("nverticesModule"),
        ),
        pairVariables = cms.PSet(
            #nJets30 = cms.InputTag("njets30ModuleSta"),
            pt      = cms.string("pt"),
            rapidity = cms.string("rapidity"),
            deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"),
        ),
        pairFlags = cms.PSet(),
        allProbes     = cms.InputTag("probeL1"),
    )
    process.tagAndProbeTkL1 = cms.Path(
        process.HLTMu + 
        process.fastFilter +
        process.probeL1 +
        process.tpPairsTkL1 +
        process.preTkMatchSequenceJPsi +
        process.l1ToTkMatch + 
        process.l1ToTkMatchNoJPsi + process.l1ToTkMatchNoBestJPsi +
        process.l1ToTkMatch0 + 
        process.l1ToTkMatchNoJPsi0 + process.l1ToTkMatchNoBestJPsi0 +
        process.nverticesModule +
        process.tpTreeL1
    )

process.schedule = cms.Schedule(
   process.tagAndProbe,
   #process.tagAndProbeSta,
   #process.tagAndProbeTkL1
)

process.RandomNumberGeneratorService.tkTracksNoJPsi      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoJPsi0      = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoBestJPsi  = cms.PSet( initialSeed = cms.untracked.uint32(81) )
process.RandomNumberGeneratorService.tkTracksNoBestJPsi0  = cms.PSet( initialSeed = cms.untracked.uint32(81) )

#process.TFileService = cms.Service("TFileService", fileName = cms.string("tnpJPsi_Data.root"))
process.TFileService = cms.Service("TFileService", fileName = cms.string("tnpJPsi_Data.root"))
