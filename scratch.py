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
ptot = #pression actuelle totale. Autrement dit la pression ambiante dans le lieu ou se trouve le séchoir.
Ta = #Temperature de l'air ambiante (en Kelvin)
Ma = #Masse molaire de l'air (sec)
Me = #Masse molaire de l'eau
t = #temps exprimé en heures de séchage




#####################################################################
"""
#Block Environnement
"""
Trosé =

Hr = 

psat =

Tsky = Ta*(0.711 + (0.005 * Trosé) + (7,3 * (10 ** -5) * (Trosé ** 2)) + 0.013 * math.cos((2*pi*t)/24))**1/4

Ha = (Me/Ma) * ((Hr * psat)/(ptot-(Hr*psat)))



#####################################################################
"""
#Block Effet-de-Serre
"""




#####################################################################
"""
#Block Ventillation
"""
