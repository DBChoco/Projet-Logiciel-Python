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

"""
#Définition des variables utilisées
"""
# Environnement
################
# ptot = #pression actuelle totale. Autrement dit la pression ambiante dans le lieu ou se trouve le séchoir.
# Ta = #Temperature de l'air ambiante (en Kelvin)
# Ma = #Masse molaire de l'air (sec)
# Me = #Masse molaire de l'eau
# t = #temps exprimé en heures de séchage
# Hr = #Humidité relative
# pe = #pression partielle de vapeur
# psat = #pression saturfante à temperature Trosé
a = 0 #Permet de ne pas prendre en compte l'expression en cosinus dans la formule de Tsky, assignez une valeur de 0 ou 1 dépendant du cas.


# Ventillation
################
# J = #Quantité d'eau évaporé par seconde (poivre/banane)
# Hamax = #Humidité absolue maximale
m_eau_init = 3  # 3kg d'eau par kg de matière sèche
m_eau_fin = 0, 1  # 0.1 kg d'eau par kg de matière sèche
m_bananes = 0, 5  # masse de bananes a sécher en kg
t = 8  # Durée du séchage en heures
Ha_banane =  # Humidité abosulue de la banane
f_massique_seche = #Fraction massique de matière s!che dans la banane
Hainitbananes = #humidité absolue initiale contenu dans les bananes
Hafinbananes = #humidité absolue finale contenu dans les bananes
################


# Effet de Serre
################
Q  = ventillation(J, Hamax, Ha=environnement(Pto, Ta, t, ptot)[1]) #ebit d'air(m**3/s)
h =  #coefficient d'échange de chaleur entre la surface et le toit
Fd = environnement(Pto, Ta, t, ptot)[1] #Flux direct
Fi = environnement(Pto, Ta, t, ptot)[0] #Flux indirect
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


def environnement(Pto, Ta, t, ptot):

    pe = (Hr * psat) / 100  # pression partielle de vapeur

    Trose = 373.15 / (1 - math.log(101325 / ptot * math.e))  # Température de rosée

    Tsky = (Ta * (0.711 + (0.005 * Trose) + (7.3 * (10 ** -5) * (Trose ** 2)) + 0.013 * (a * math.cos(
        (2 * math.pi * t) / 24))) ** 1 / 4) - 273.15

    Ha = (Me / Ma) * ((Hr * psat) / (ptot - (Hr * psat)))  # Humidité absolue

    Fi = 5.67 * 10 ** (-8) * Tsky ** 4  # Flux indirect

    Fd = # Flux direct


    return [Fi, Fd, Ha]

#####################################################################
"""
#Block Ventillation
"""


def ventillation(J, Hamax, Ha=environnement(Pto, Ta, t, ptot)[1]):

    t_sec = t * 60 * 60  # Temps de séchage en secondes

    m_matiereseche = f_massique_seche * m_bananes  #Masse de matière sèche

    J = ((Hainitbananes - Hafinbananes) * m_matiereseche) / t_sec  #Masse d'eau évaporé par seconde (contenue dans le poivre/banane)

    Qmin = J / (Hamax - Ha)  # Débit d'air minimal (m³/s)

    print("Le débit d'air minimal en m³/s est de ", Qmin, " m³/s")

    return Qmin


#####################################################################
"""
# Block Effet-de-Serre
"""
def func(x):

    P, Ts, Tp = x
    eq = (P - h * (Ts - T) - h * (Tp - T), Fd + Fi - P - (sigma * Tp ** 4),
          Fd + (sigma * Tp ** 4) - (sigma * Ts ** 4) - h * (Ts - T))

    return eq


def effetDeSerre(Fd, Fi, T, Q): #Entrées du block effet de serre: Flux direct, flux indirect, Temperature intérieur de la serre et le débit.

    import numpy as np

    from scipy.optimize import fsolve

    P, Ts, Tp = fsolve(func, (1,1,1))


    return P





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
