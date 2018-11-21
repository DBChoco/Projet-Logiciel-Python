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
################

# Effet de Serre
################
# Q est le debit d'air(m**3/s)
# puissance
# h est le coefficient d'échange de chaleur entre la surface et le toit
# Fs est le flux d'énérgie produit par le sols par la loie des corps noirs
# Ft est le flux d'énérgie produit par le toit par la loie des corps noirs
# tempSurf est la temperature de la surface
# tempToit est la temperature du toit
V =  # vitesse du fluide
L =  # longueur de la plaque
µ =  # viscosité dynamique du fluide
M =  # masse volumique du fluide
λ =  # conductivité du fluide
g =  # Force de pesanteur
∆T =  # Difference de température
cp =  # Chaleur spécifique du fluide
β =  # Coefficient de dilatation
################

# Ventillation
################
# J = #Quantité d'eau évaporé par seconde (poivre/banane)
# Hamax = #Humidité absolue maximale
m_eau_init = 3  # 3kg d'eau par kg de matière sèche
m_eau_fin = 0, 1  # 0.1 kg d'eau par kg de matière sèche
m_bananes = 0, 5  # masse de bananes a sécher en kg
t = 8  # Durée du séchage en heures
Ha_banane = #Humidité abosulue de la banane
M_eau = #Masse molaire de l'eau
M_s = #Masse molaire de la matière sèche contenue dans la banene
################
#####################################################################
"""
#Block Environnement
"""


def environnement(Pto, Ta, t, ptot):
    psat =

    pe = (Hr * psat) / 100  # pression partielle de vapeur

    Trose = 373.15 / (1 - math.log(101325 / ptot, math.e))  # Température de rosée

    Tsky = Ta * (0.711 + (0.005 * Trose) + (7, 3 * (10 ** -5) * (Trose ** 2)) + 0.013 * math.cos(
        (2 * math.pi * t) / 24)) ** 1 / 4

    Ha = (Me / Ma) * ((Hr * psat) / (ptot - (Hr * psat)))  # Humidité absolue

    Fi = 5.67 * 10 ** (-8) * Tsky ** 4  # Flux indirect

    Fd =  # Flux direct


return [Fi, Fd, Ha]

#####################################################################
"""
#Block Effet-de-Serre
"""


def effetDeSerre(fluxD, fluxI, tempSerre, Q):
    v = µ / M  # viscosité cinématique du fluide

    Re = (V * L) / v

    Gr = (g * β *∆T * L * 3) / (v * 2)  # Nombre de Grashof

    Pr = (µ * cp) / λ  # Nombre de Prandtl

    if convection == 'Naturelle':  # Nu = Nombre de Nusselt
        # convection naturelle
        if Re < 3 * 10 ** 5:
            # écoulement laminaire:
            Nu = 0, 479.Gr ** (1 / 4)
        else:
            # écoulement turbulent:
            Nu = 0, 13 * ((Gr * Pr) ** (1 / 3))
    else:
        # convection forcée
        if Re < 3.104:
            # écoulement laminaire
            Nu = 0, 66 * Pr ** (1 / 3) * (Re ** (1 / 2))
        else:
            # écoulement turbulent
            Nu = 0, 036 * (Pr ** (1 / 3)) * (Re ** (4 / 5))

    h = (λ * Nu) / L

    return h


#####################################################################
"""
#Block Ventillation
"""


def ventillation(J, Hamax, Ha=environnement(Pto, Ta, t, ptot)[1]):
    
    t_sec = t * 60 * 60  # Temps de séchage en secondes

    m_matiereseche = (m_eau_init * M_eau)/(Ha_banane * M_s) ##Attention contenu non verifié

    J = ((Hainitbananes - Hafinbananes) * m_matiereseche) / t_sec ##Attention contenu non verifié

    Qmin = J / (Hamax - Ha)  # Débit d'air minimal (m³/s)

    print("Le débit d'air minimal en m³/s est de ",Qmin, " m³/s")

    return Qmin

