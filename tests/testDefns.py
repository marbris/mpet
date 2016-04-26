import os
import os.path as osp
import shutil
import sys

mpetdir = osp.join(os.environ["HOME"], "docs", "bazantgroup", "mpet")
sys.path.append(mpetdir)
import mpet
import mpetParamsIO as IO

def test001(testDir, dirDict):
    """ LFP ACR C3 """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "ACR")
    P.set("Material", "muRfunc", "LiFePO4")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test002(testDir, dirDict):
    """ LFP CHR cylinder """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "CHR")
    P.set("Particles", "shape", "cylinder")
    P.set("Material", "muRfunc", "LiFePO4")
    P.set("Material", "dgammadc", "5e-30")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test003(testDir, dirDict):
    """ LFP CHR sphere """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "CHR")
    P.set("Particles", "shape", "sphere")
    P.set("Material", "muRfunc", "LiFePO4")
    P.set("Material", "dgammadc", "-2e-30")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test004(testDir, dirDict):
    """ LFP CHR sphere with noise  """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "CHR")
    P.set("Particles", "shape", "sphere")
    P.set("Material", "muRfunc", "LiFePO4")
    P.set("Material", "noise", "true")
    P.set("Material", "dgammadc", "-2e-30")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test005(testDir, dirDict):
    """ LFP homog """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    P_s.set("Sim Params", "Nvol_c", "2")
    P_s.set("Sim Params", "Nvol_s", "2")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog")
    P.set("Material", "muRfunc", "LiFePO4")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test006(testDir, dirDict):
    """ LFP homog with logPad, Vmin """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    P_s.set("Sim Params", "Vmin", "2.8e-0")
    P_s.set("Particles", "cs0_c", "0.5")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog")
    P.set("Material", "muRfunc", "LiFePO4")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test007(testDir, dirDict):
    """ LFP homog with logPad, Vmax """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "-1e-2")
    P_s.set("Sim Params", "Vmax", "4.0e-0")
    P_s.set("Particles", "cs0_c", "0.5")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog")
    P.set("Material", "muRfunc", "LiFePO4")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test008(testDir, dirDict):
    """ LFP homog_sdn """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    P_s.set("Sim Params", "Nvol_c", "3")
    P_s.set("Sim Params", "Npart_c", "3")
    P_s.set("Particles", "stddev_c", "25e-9")
    P_s.set("Sim Params", "capFrac", "0.6")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog_sdn")
    P.set("Material", "muRfunc", "LiFePO4")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test009(testDir, dirDict):
    """ Graphite-2param homog """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog2")
    P.set("Material", "muRfunc", "LiC6")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test010(testDir, dirDict):
    """ Graphite-2param CHR cylinder """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "CHR2")
    P.set("Particles", "shape", "cylinder")
    P.set("Material", "muRfunc", "LiC6")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test011(testDir, dirDict):
    """ Graphite-2param CHR sphere """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    P_s.set("Sim Params", "relTol", "1e-7")
    P_s.set("Sim Params", "absTol", "1e-7")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "CHR2")
    P.set("Particles", "shape", "sphere")
    P.set("Material", "muRfunc", "LiC6")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test012(testDir, dirDict):
    """ Solid solution, diffn sphere, homog, LiC6_coke_ss2, LiMn2O4_ss2
    BV_mod01, BV_mod02
    cathode + anode
    """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_a.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrodec = osp.join(testDir, "params_c.cfg")
    ptrodea = osp.join(testDir, "params_a.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    P_s.set("Sim Params", "capFrac", "0.67")
    P_s.set("Sim Params", "Nvol_c", "2")
    P_s.set("Sim Params", "Nvol_a", "2")
    P_s.set("Sim Params", "Vmin", "2e0")
    P_s.set("Particles", "cs0_c", "0.2")
    P_s.set("Particles", "cs0_a", "0.495")
    P_s.set("Electrolyte", "elyteModelType", "SM")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrodec)
    P.set("Particles", "type", "homog")
    P.set("Particles", "shape", "cylinder")
    P.set("Material", "muRfunc", "LiMn2O4_ss2")
    P.set("Reactions", "rxnType", "BV_mod01")
    IO.writeConfigFile(P, ptrodec)
    P = IO.getConfig(ptrodea)
    P.set("Particles", "shape", "sphere")
    P.set("Material", "muRfunc", "LiC6_coke_ss2")
    P.set("Reactions", "rxnType", "BV_mod02")
    IO.writeConfigFile(P, ptrodea)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test013(testDir, dirDict):
    """ Solid solution, diffn cylinder, homog, testIS_ss, LiMn2O4_ss2
    Marcus, BV_raw
    cathode + separator + anode
    """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_a.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrodec = osp.join(testDir, "params_c.cfg")
    ptrodea = osp.join(testDir, "params_a.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "profileType", "CV")
    P_s.set("Sim Params", "Vset", "3.8")
    P_s.set("Sim Params", "Nvol_c", "2")
    P_s.set("Sim Params", "Nvol_s", "2")
    P_s.set("Sim Params", "Nvol_a", "2")
    P_s.set("Particles", "cs0_c", "0.2")
    P_s.set("Particles", "cs0_a", "0.95")
    P_s.set("Electrolyte", "elyteModelType", "dilute")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrodec)
    P.set("Particles", "type", "homog")
    P.set("Particles", "shape", "sphere")
    P.set("Material", "muRfunc", "LiMn2O4_ss2")
    P.set("Reactions", "rxnType", "Marcus")
    IO.writeConfigFile(P, ptrodec)
    P = IO.getConfig(ptrodea)
    P.set("Particles", "shape", "cylinder")
    P.set("Material", "muRfunc", "testIS_ss")
    P.set("Reactions", "rxnType", "BV_raw")
    IO.writeConfigFile(P, ptrodea)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test014(testDir, dirDict):
    """ LFP homog with CCsegments, MHC, Rser """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "profileType", "CCsegments")
    P_s.set("Sim Params", "segments",
            "[(1., 25), (-2., 10), (0., 30)]")
    P_s.set("Sim Params", "Rser", "1e-3")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog")
    P.set("Material", "muRfunc", "LiFePO4")
    P.set("Reactions", "rxnType", "MHC")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test015(testDir, dirDict):
    """ testRS homog with CVsegments, bulkCond, partCond """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "profileType", "CVsegments")
    P_s.set("Sim Params", "Npart_c", "5")
    P_s.set("Sim Params", "Nvol_c", "5")
    P_s.set("Sim Params", "segments",
            "[(-0.3, 25), (0., 10), (0.3, 30)]")
    P_s.set("Conductivity", "simBulkCond_c", "true")
    P_s.set("Conductivity", "mcond_c", "5e-2")
    P_s.set("Conductivity", "simPartCond_c", "true")
    P_s.set("Conductivity", "G_mean_c", "3e-14")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog")
    P.set("Material", "muRfunc", "testRS")
    P.set("Reactions", "rxnType", "BV_raw")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test016(testDir, dirDict):
    """ test CC continuation """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "Crate", "1e-2")
    P_s.set("Sim Params", "Nvol_c", "3")
    P_s.set("Sim Params", "Npart_c", "3")
    P_s.set("Sim Params", "capFrac", "0.34")
    test008dir = str(osp.join(testDir, "..", "test008", "sim_output"))
    P_s.set("Sim Params", "prevDir", test008dir)
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog_sdn")
    P.set("Material", "muRfunc", "LiFePO4")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test017(testDir, dirDict):
    """ test CV continuation """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "profileType", "CV")
    P_s.set("Sim Params", "Vset", "3.45")
    P_s.set("Sim Params", "tend", "3e3")
    P_s.set("Sim Params", "Nvol_c", "3")
    P_s.set("Sim Params", "Npart_c", "3")
    test008dir = str(osp.join(testDir, "..", "test008", "sim_output"))
    P_s.set("Sim Params", "prevDir", test008dir)
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog_sdn")
    P.set("Material", "muRfunc", "LiFePO4")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return

def test018(testDir, dirDict):
    """ Like test014, LFP homog with CCsegments, BV, Rfilm, Rfilm_foil """
    shutil.copy(osp.join(dirDict["baseConfig"], "params_system.cfg"), testDir)
    shutil.copy(osp.join(dirDict["baseConfig"], "params_c.cfg"), testDir)
    psys = osp.join(testDir, "params_system.cfg")
    ptrode = osp.join(testDir, "params_c.cfg")
    P_s = IO.getConfig(psys)
    P_s.set("Sim Params", "profileType", "CCsegments")
    P_s.set("Sim Params", "segments",
            "[(1., 25), (-2., 10), (0., 30)]")
    P_s.set("Electrodes", "k0_foil", "3e+0")
    P_s.set("Electrodes", "Rfilm_foil", "3e+0")
    IO.writeConfigFile(P_s, psys)
    P = IO.getConfig(ptrode)
    P.set("Particles", "type", "homog")
    P.set("Material", "muRfunc", "LiFePO4")
    P.set("Reactions", "Rfilm", "1e+1")
    IO.writeConfigFile(P, ptrode)
    mpet.main(psys, keepArchive=False)
    shutil.move(dirDict["simOut"], testDir)
    return
