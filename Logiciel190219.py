"""
Titre : Logiciel.py Python projet
Date debut : 5 novembre 2018
Auteurs : Groupe n33 projet
"""
#####################################################################
"""
#Import des paquets
"""
import math

import numpy as np

from scipy.optimize import fsolve

"""
#Definition des variables utilisees
"""
#condition environment
Tamb = 273.5+25
Tvoulu = 273.5 + 65 #temperature idéal pour le séchoire
# General
################
Ma = 0.8 * 2 * 14.01 + 0.2 * 2 * 16  # Masse molaire de l'air (sec) (mol/g)
Me = 2 * 1.005 + 16  # Masse molaire de l'eau (mol/g)
R = 8.314  # Constante universelle des gaz parfaits
L = 2.454 * 18  # chaleur latente de vaporisation de l'eau
t = 8  # temps de sechage (heures)
HrMax = 20  # Humidite relatif maximal
m_eau_init = 3  # 3kg d'eau par kg de matiere seche
m_eau_fin = 0.1  # 0.1 kg d'eau par kg de matiere seche
m_bananes = 0.5  # masse de bananes a secher en kg
f_massique_seche = 0.25  # Fraction massique de matiere seche dans la banane
Hainitbananes = 3  # humidite absolue initiale contenu dans les bananes
Hafinbananes = 0.909  # humidite absolue finale contenu dans les bananes
sigma = 5.67 * (10 ** (-8))
La = 2250*10**3 # enthalpie de vaporisation / chaleur latente de l'eau (j/kg)

# Environnement
################
altitude = 60  #altidude de ixelles par rapport a la mer de l'endroit ou il a le sechoir
patm = 101315 * (1 - (0.0065 * altitude / 288.15)) ** 5.255 #pression actuelle totale. Autrement dit la pression
                                                                # ambiante dans le lieu ou se trouve le sechoir.(en Pa)
Fd = 900  # Flux direct produit par les lampes (W/m**2)
Tref = 273.5 + 20  # température de référence (en Kelvin)
Hr = 0.65  #pour la belgique en % #Humidite relative
psatref = 2.3 * 10 ** 3  #pression saturfante a temperature Tref

# Convection
################
# V #vitesse du fluide
L = 0.3 # longueur de la plaque
mu = 1.8*10**(-5)  # (Pa.s) viscosite dynamique du fluide
rho = 1.225  # (kg/m**3) masse volumique du fluide
lambdaa = 0.0262  # (W/m.K) conductivite du fluide
g =  9.81 # Force de pesanteur
#dT =  # Difference de temperature
cp = 1004  # (J/Kg.K) Chaleur specifique du fluide
beta = 1/(273.15+65) # Coefficient de dilatation

# Effet de Serre
################
h = 4  # coefficient d'echange de chaleur entre la surface et le toitµ
T = 320

###puissance
Cva = 1.256*10**(3)#Capacité calorifique volumique de l'air(J m**(−3) K**(−1))


#####################################################################
"""
#Block Environnement
"""
def psat_(Tamb):
    psatT = 2.718**((La/R)*(1/Tamb - 1/Tref))*psatref
    return psatT

psat = psat_(Tamb)

Hamax = 0.6217 * HrMax * psat / (patm - HrMax * psat)  #Humidite absolue maximale

pe = (Hr * psat)  # Pression partielle de vapeur

Trose = (math.log(pe / psat, math.e) * (-R / L) + 1 / Tamb) ** (-1)  # Temperature de rosee

Tsky = Tamb * (0.711 + (0.0056 * Trose) + (7.3 * (10 ** -5) * Trose ** 2))  # Tsky

Ha = (Me / Ma) * ((Hr * psat) / (patm - (Hr * psat)))  # Humidite absolue

Fi = 5.67 * 10 ** (-8) * Tsky ** 4  # Flux indirect

# Fd = 900  #Flux direct

print('pe = ', pe, '\n', 'Trose = ', Trose, '\n', 'Tsky = ', Tsky, '\n', 'Ha = ', Ha, '\n', 'Fi = ', Fi, '\n',
      'Fd = ', Fd)  # debug


##########################################
"""
#Block Ventilation
"""

t_sec = t * 60 * 60  # Temps de sechage en secondes

m_matiereseche = f_massique_seche * m_bananes  # Masse de matiere seche

J = ((Hainitbananes - Hafinbananes) * m_matiereseche) / t_sec  # Masse d'eau evaporee par seconde (contenue dans le
# poivre/banane)

Qmin = J / (Hamax - Ha)  # Debit d'air minimal (m^3/s)

print("Le debit d'air minimal en m^3/s est de ", Qmin, " m^3/s")

print('t_sec = ',t_sec,'m_matiereseche = ',m_matiereseche,'J = ',J,'Qmin = ',Qmin)  #debug

##########################################
"""
#Convexion
"""


def ConvectionH(mu, rho, L, g, beta, dT, cp, lambdaa):

    alpha = lambdaa/(rho * cp)

    V = Qmin/0.0025

    v = mu / rho  # viscosite cinematique du fluide

    Re = (V * L) / v  # Nombre de Reynolds

    Gr = (g * beta * dT * L**3 * rho**2) / mu**2  # Nombre de Grashof

    Pr = (mu * cp)/lambdaa  # Nombre de Prandtl

    Ra = Pr*Gr

    Nu = 0.18 * Ra**(1/4)
        #0.54*(Ra/4)

    h = (Nu * lambdaa) / L

    return h


##########################################
"""
#Block Effet-de-Serre
"""


def func(x):
    P, Ts, Tp = x

    return P - h * (Ts - T) - h * (Tp - T), Fd + Fi - P - (sigma * Tp ** 4), Fd + (sigma * Tp ** 4) - (sigma * Ts ** 4) \
           - h * (Ts - T)


def effet_de_serre():
    P, Ts, Tp = fsolve(func, (1, 1, 1))
    return P, Ts, Tp

"""
Block dimensions
"""
def dimensions(P):
    # puissance totale
    Ptot = Qmin*Cva*(Tvoulu-Tamb)+ J * La
    Surface  = Ptot/P
    return Surface

#####################################################################

# Lancement du logiciel

h = 6
P, Ts, Tp = effet_de_serre()
dT = (Tp - (273.15 + 25))
print(dT)
h = ConvectionH(mu, rho, L, g, beta, dT, cp, lambdaa)
P, Ts, Tp = effet_de_serre()
print(Tp)
print('La puissance et de ', P, 'W/m^2')
print (P, h)
Surface = dimensions(P)
print("dimensions: ", Surface," m**2")



