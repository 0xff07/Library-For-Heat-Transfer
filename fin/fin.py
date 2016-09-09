from math import *

# List all possible cases#
Case = {'convection':1,
		'adiabatic':2,
		'constant temperatur':3,
		'inifinite':4
		}


class UNIFORM_FIN:

	# A memonic line to memorize function prototype #
    def __init__(self,_k=0,_h=0,_L=0,_P=0,_A=0,_T0=0,_Too=0):
        self.k = float(_k)
        self.h = float(_h)
        self.L = float(_L)
        self.P = float(_P)
        self.A = float(_A)
        self.T0 = float(_T0)
        self.Too = float(_Too)
        self.m = sqrt(_h/_A * _k/_h)

	# 4 cases on wikipedia. #
    def ThetaRatio(self, x = 0, type = ' ', Tl = 0):

        k = self.k
        h = self.h
        L = self.L
        P = self.P
        A = self.A
        T0 = self.T0
        Too = self.Too

        m = self.m
        res = -1
        len_comp = (L - x)
        if type == 'convection' :
            tmp  = h / (m * k)
            numtor = (1 + tmp)*exp(m*len_comp) + (1 - tmp)*exp(-m*len_comp)
            dnumtor = (1 + tmp)*exp(m*L) + (1 - tmp)*exp(-m*L)
            res = numtor / dnumtor
        elif type == 'adiabatic':
            numtor = cosh(m * len_comp)
            dnumtor = cosh(m * L)
            res =  numtor / dnumtor
        elif type == 'constant temperature':
            theta_fact = (Tl - Too) / (T0 - Too)
            numtor = theta_fact * sinh(m * x) + sinh(m * len_comp)
            dnumtor = sinh(m * L)
            res = numtor / dnumtor
        elif type == 'infinite':
            res = exp(-1 * m * x)
        else:
            res = -1
        return res

    # Find T by the ratio of theta b and theta. #
    def T(self, x, type, Tl = 0):
        T0 = self.T0
        Too = self.Too
        return Too + self.ThetaRatio(x,type,Tl)*(T0-Too)	


    def QRate(self, type, Tl = 0):
        k = self.k
        h = self.h
        L = self.L
        P = self.P
        A = self.A
        T0 = self.T0
        Too = self.Too
        m = self.m
        M = sqrt(h * P * k * A) * (T0 - Too)

        if type == 'convection' :
            tmp = h  / m / k;
            numtor = sinh(m * L) + tmp * cosh(m * L)
            dnumtor = cosh(m * L) + tmp * sinh(m * L)
            return M * numtor / dnumtor
        elif type == 'adiabatic':
            return M * tanh(m * L)
        elif type == 'constant temperature':
            theta_fact = (Tl - Too)/(T0 - Too)
            return M * (cosh(m * L) - theta_fact)/sinh(m * L)
        elif type == 'infinite':
            return M
        else:
            return -1;

    def getResistance(self, type):
        return (self.T0 - self.T(self.L, type))/self.QRate(self.L, type)


