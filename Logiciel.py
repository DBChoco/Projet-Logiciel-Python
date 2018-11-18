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
#Environnement 
################
#ptot = #pression actuelle totale. Autrement dit la pression ambiante dans le lieu ou se trouve le séchoir.
#Ta = #Temperature de l'air ambiante (en Kelvin)
#Ma = #Masse molaire de l'air (sec)
#Me = #Masse molaire de l'eau
#t = #temps exprimé en heures de séchage
#pe = #pression partielle de vapeur
#psat = #pression saturfante à temperature Trosé
################

#Effet de Serre
################
#Q est le debit d'air(m**3/s)
#puissance
#h est le coefficient d'échange de chaleur entre la surface et le toit
#Fs est le flux d'énérgie produit par le sols par la loie des corps noirs
#Ft est le flux d'énérgie produit par le toit par la loie des corps noirs
#tempSurf est la temperature de la surface
#tempToit est la temperature du toit
################

#Ventillation
################
#J = #Quantité d'eau évaporé par seconde (poivre/banane)
#Hamax = #Humidité absolue maximale
################
#####################################################################
"""
#Block Environnement
"""

def environnement(Pto,Ta,t,ptot):
    
    psat =

    Hr =Pe/psat*100 #humidité relative

    Trose = 373.15/(1-math.log(101325/ptot,math.e)) #Température de rosée

    Tsky = Ta*(0.711 + (0.005 * Trose) + (7,3 * (10 ** -5) * (Trose ** 2)) + 0.013 * math.cos((2*math.pi*t)/24))**1/4

    Ha = (Me/Ma) * ((Hr * psat)/(ptot-(Hr*psat))) #Humidité absolue

    Fi = 5.67*10**(-8)*Tsky**4 #Flux indirect
    
    Fd= #Flux direct
    
return [Fi,Fd,Ha]

#####################################################################
"""
#Block Effet-de-Serre
"""

#def effetDeSerre(fluxD, fluxI, tempSerre,Q ):



#####################################################################
"""
#Block Ventillation
"""

def ventillation(J,Hamax,Ha=environnement(Pto,Ta,t,ptot)[1]):
    
    Qmin = J/(Hamax - Ha) #Débit d'air minimal (m³/s)
    
    print("Le débit d'air minimal en m³/s est de " Qmin " m³/s")             
                 
    return Qmin

