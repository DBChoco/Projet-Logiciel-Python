"""
Titre : Logiciel Python projet
Date début : 5 novembre 2018
Auteurs : Groupe n°33 projet
"""
#####################################################################
"""
#Import des paquets
"""
import math

# noinspection PyUnresolvedReferences
import scipy.optimize

"""
#Définition des variables utilisées
"""
# Environnement
################
altitude= 60 #altidude de ixelles par rapport a la mer de l'endroit ou il a le séchoire
ptot = 101315*(1-(0.0065*altitude/288.15))**5.255 #pression actuelle totale. Autrement dit la pression ambiante dans le lieu ou se trouve le séchoir.(en Pa)
Fd  = 900# Flux direct produit par les lampes (W/m**2)
Ta = 291.15 #(a l'interieur du batiment de teste) Temperature de l'air ambiante (en Kelvin)
Na = 0.8 * 2 * 14.01 + 0.2 *2*16#Masse molaire de l'air (sec) (mol/g)
Ne = 2* 1.005 +16 #Masse molaire de l'eau (mol/g)
t = 8#temps maximal exprimé en heures de séchage (heure)
Hr = 85 #pour la belgique en % #Humidité relative
psat = ptot/75 #pression saturfante à temperature Trosé
Me = 18 #Masse molaire eau
Ma = 28.976 #Masse molaire air
a = 0 #Permet de ne pas prendre en compte l'expression en cosinus dans la formule de Tsky, assignez une valeur de 0 ou 1 dépendant du cas.



# Ventillation
################
HrMax = 20 #Humidité relatif maximal
Hamax = 0.6217*HrMax*psat/(ptot-HrMax*psat) #Humidité absolue maximale
m_eau_init = 3  # 3kg d'eau par kg de matière sèche
m_eau_fin = 0.1  # 0.1 kg d'eau par kg de matière sèche
m_bananes = 0.5  # masse de bananes a sécher en kg
f_massique_seche = 0.25#Fraction massique de matière s!che dans la banane
Hainitbananes = 3 #humidité absolue initiale contenu dans les bananes
Hafinbananes = 0.909#humidité absolue finale contenu dans les bananes



# Effet de Serre
################
h = 4 #coefficient d'échange de chaleur entre la surface et le toit
sigma = 5.67*(10**(-8))
T = 300


###Convexion
#V =  # vitesse du fluide
#L =  # longueur de la plaque
#µ =  # viscosité dynamique du fluide
#M =  # masse volumique du fluide
#λ =  # conductivité du fluide
#g =  # Force de pesanteur
#dT =  # Difference de température
#cp =  # Chaleur spécifique du fluide
#β =  # Coefficient de dilatation
#convexion = 'Forcée' ou 'Naturelle' #Type de convexion
################
#####################################################################
"""
#Block Environnement
"""

pe = (Hr * psat) / 100  # pression partielle de vapeur

Trose = (373.15 / (1 - math.log((101325 / ptot) * math.e))) - 273.15  # Température de rosée

Tsky = (Ta * (0.711 + (0.005 * Trose) + (7.3 * (10 ** -5) * (Trose ** 2)) + 0.013 * (a * math.cos((2 * math.pi * t) / 24))) ** 1 / 4) - 273.15

Ha = (Me / Ma) * ((Hr * psat) / (ptot - (Hr * psat)))  # Humidité absolue

Fi = 5.67 * 10 ** (-8) * Tsky ** 4  # Flux indirect

Fd = 900 # Flux direct

print('pe = ',pe,'Trose = ',Trose,'Tsky = ',Tsky,'Ha = ',Ha,'Fi = ',Fi,'Fd = ',Fd,)  #débug

#####################################################################
"""
#Block Ventillation
"""

t_sec = t * 60 * 60  # Temps de séchage en secondes

m_matiereseche = f_massique_seche * m_bananes  #Masse de matière sèche

J = ((Hainitbananes - Hafinbananes) * m_matiereseche) / t_sec  #Masse d'eau évaporé par seconde (contenue dans le poivre/banane)

Qmin = J / (Hamax - Ha)  # Débit d'air minimal (m³/s)

print("Le débit d'air minimal en m³/s est de ", Qmin, " m³/s")


print('t_sec = ',t_sec,'m_matiereseche = ',m_matiereseche,'J = ',J,'Qmin = ',Qmin)  #débug


#####################################################################

"""
# Block Effet-de-Serre
"""

def func(x):

    P, Ts, Tp = x

    return P - h * (Ts - T) - h * (Tp - T), Fd + Fi - P - (sigma * Tp ** 4), Fd + (sigma * Tp ** 4) - (sigma * Ts ** 4) - h * (Ts - T)

import numpy as np

from scipy.optimize import fsolve

P,Ts,Tp = fsolve(func,(1,1,1))

print('P = ',P,'Ts = ',Ts,'Tp = ',Tp)




"""
def ConvexionH(µ, M, V, L, g, β, dT, cp, λ ,convexion):

    v = µ / M  # viscosité cinématique du fluide

    Re = (V * L) / v # Nombre de Reynolds

    Gr = (g * β * dT * L * 3) / (v * 2)  # Nombre de Grashof

    Pr = (µ * cp) / λ  # Nombre de Prandtl

    if convection == 'Naturelle':  # Nu = Nombre de Nusselt & cas : convection naturelle
        if Re < 3 * 10 ** 5: # écoulement laminaire:
            Nu = 0, 479 * Gr ** (1 / 4)
        else: # écoulement turbulent:
            Nu = 0, 13 * ((Gr * Pr) ** (1 / 3))
    else: # cas : convection naturelle
        if Re < 3.104: # écoulement laminaire
            Nu = 0, 66 * Pr ** (1 / 3) * (Re ** (1 / 2))
        else: # écoulement turbulent
            Nu = 0, 036 * (Pr ** (1 / 3)) * (Re ** (4 / 5))

    h = (λ * Nu) / L

    return h
"""
