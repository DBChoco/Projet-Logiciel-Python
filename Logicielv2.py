"""
Titre : Logiciel.py Python projet
Date début : 5 novembre 2018
Auteurs : Groupe n°33 projet
"""
#####################################################################
"""
#Import des paquets
"""
import math

import numpy as np

from scipy.optimize import fsolve

"""
#Définition des variables utilisées
"""

Ma = 0.8 * 2 * 14.01 + 0.2 * 2 * 16  # Masse molaire de l'air (sec) (mol/g)
Me = 2 * 1.005 + 16  # Masse molaire de l'eau (mol/g)
R = 8.314  # Constante universelle des gaz parfaits
L = 2.454 * 18  # chaleur latente de vaporisation de l'eau
t = 8  # temps de séchage (heures)
HrMax = 20  # Humidité relatif maximal
m_eau_init = 3  # 3kg d'eau par kg de matière sèche
m_eau_fin = 0.1  # 0.1 kg d'eau par kg de matière sèche
m_bananes = 0.5  # masse de bananes a sécher en kg
f_massique_seche = 0.25  # Fraction massique de matière s!che dans la banane
Hainitbananes = 3  # humidité absolue initiale contenu dans les bananes
Hafinbananes = 0.909  # humidité absolue finale contenu dans les bananes
sigma = 5.67 * (10 ** (-8))
T = 300

###puissance
Cva = 1,256*10**(3)#Capacité calorifique volumique de l'air(J m**(−3) K**(−1))

#####################################################################
"""
#Block Environnement
"""


def environnement():
    pe = (Hr * psat)  # Pression partielle de vapeur

    Trose = (math.log(pe / psat, math.e) * (-R / L) + 1 / Tamb) ** (-1)  # Température de rosée

    Tsky = Tamb * (0.711 + (0.0056 * Trose) + (7.3 * (10 ** -5) * Trose ** 2))  # Tsky

    Ha = (Me / Ma) * ((Hr * psat) / (patm - (Hr * psat)))  # Humidité absolue

    Fi = 5.67 * 10 ** (-8) * Tsky ** 4  # Flux indirect

    # Fd = 900  #Flux direct

    print('pe = ', pe, '\n', 'Trose = ', Trose, '\n', 'Tsky = ', Tsky, '\n', 'Ha = ', Ha, '\n' , 'Fi = ', Fi, '\n',
          'Fd = ', Fd)  # débug

    return Fd, Fi, Ha


#####################################################################
"""
#Block Ventilation
"""


def ventillation():
    
    t_sec = t * 60 * 60  # Temps de séchage en secondes

    m_matiereseche = f_massique_seche * m_bananes  # Masse de matière sèche

    J = ((Hainitbananes - Hafinbananes) * m_matiereseche) / t_sec  # Masse d'eau évaporé par seconde (contenue dans le
    # poivre/banane)

    Qmin = J / (Hamax - Ha)  # Débit d'air minimal (m³/s)

    print("Le débit d'air minimal en m³/s est de ", Qmin, " m³/s")

    # print('t_sec = ',t_sec,'m_matiereseche = ',m_matiereseche,'J = ',J,'Qmin = ',Qmin)  #débug

    return Qmin


#####################################################################
"""
# Block Effet-de-Serre
"""


def func(x):
    
    P, Ts, Tp = x

    return P - h * (Ts - T) - h * (Tp - T), Fd + Fi - P - (sigma * Tp ** 4), Fd + (sigma * Tp ** 4) - (sigma * Ts ** 4) \
           - h * (Ts - T)


def effetdeserre():
    
    P, Ts, Tp = fsolve(func, (1, 1, 1))

    print('La puissance et de ', P, ' W/m²')

    return P, Ts, Tp


#####################################################################


# Environnement
################
altitude = 60  # altidude de ixelles par rapport a la mer de l'endroit ou il a le séchoire
patm = 101315 * (1 - (0.0065 * altitude / 288.15)) ** 5.255  # pression actuelle totale. Autrement dit la pression ambiante dans
# le lieu ou se trouve le séchoir.(en Pa)
Fd = 900  # Flux direct produit par les lampes (W/m**2)
Tamb = 291.15  # (a l'interieur du batiment de teste) Temperature de l'air ambiante (en Kelvin)
Hr = 0.80  # pour la belgique en % #Humidité relative
psat = 2.3 * 10 ** 3  # pression saturfante à temperature Tamb
Hamax = 0.6217 * HrMax * psat / (patm - HrMax * psat)  # Humidité absolue maximale

# Ventillation
################
Fd, Fi, Ha = environnement()

# Effet de Serre
################
h = 2  # coefficient d'échange de chaleur entre la surface et le toit
P = effetdeserre()[0]

#puissance totale
Qmin = ventillation()
Ptot = Qmin*Cva

