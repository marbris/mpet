import numpy as np

class DPhiFits():
    def __init__(self, D):
        self.D = D
        self.kToe = D['k']*D['Tref']/D['e']
        self.eokT = 1./self.kToe
        self.materialData = {}
        self.materialData['LiMn2O4'] = self.LiMn2O4
        self.materialData['LiC6'] = self.LiC6

    def LiMn2O4(self, y, del_phi_ref):
        """
        Fit \Delta\phi^{eq} for Li_y Mn_2 O_4 as a function of y.
        This can only return values for Tabs = 298 K
        This function was obtained from
        Doyle, Newman, 1996
        del_phi_ref is the offset (non-dimensional) potential by which
        the returned value will be shifted (for numerical convenience)
        """
        if self.D['Tabs'] != 298:
            raise NotImplementedError("Only fit for T = 298 K")
        del_phi_eq = self.eokT*(
                4.19829 + 0.0565661*np.tanh(-14.5546*y + 8.60942) -
                0.0275479*(1/((0.998432 - y)**(0.492465)) - 1.90111) -
                0.157123*np.exp(-0.04738*y**8) +
                0.810239*np.exp(-40*(y - 0.133875))
                ) - del_phi_ref
        return del_phi_eq

#    def LiC6(self, y, del_phi_ref):
#        """
#        Fit \Delta\phi^{eq} for Li_y C_6 as a function of y.
#        This can only return values for Tabs = 298 K
#        This function was obtained from
#        Doyle, Newman, 1996
#        """
#        if self.D['Tabs'] != 298:
#            raise NotImplementedError("Only fit for T = 298 K")
#        del_phi_eq = self.eokT*(-0.16 + 1.32*np.exp(-3.0*y) +
#                10.*np.exp(-2000.*y)) - del_phi_ref
#        return del_phi_eq

    def LiC6(self, y, del_phi_ref):
        """
        Fit \Delta\phi^{eq} for Li_y C_6 as a function of y.
        This can only return values for Tabs = 298 K
        This function was obtained from
        Safari, Delacourt 2011
        """
        if self.D['Tabs'] != 298:
            raise NotImplementedError("Only fit for T = 298 K")
        del_phi_eq = self.eokT*( 0.6379 + 0.5416*np.exp(-305.5309*y) +
                0.044*np.tanh(-(y - 0.1958)/0.1088) -
                0.1978*np.tanh((y - 1.0571)/0.0854) -
                0.6875*np.tanh((y + 0.0117)/0.0529) -
                0.0175*np.tanh((y - 0.5692)/0.0875)) - del_phi_ref
        return del_phi_eq
