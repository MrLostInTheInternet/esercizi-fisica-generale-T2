import math
import numpy as np

K = 1 / (4 * math.pi * 8.85e-12)
def converti_in_metri(valore, unit):
    match(unit.lower()):
        case 'dm':
            valore *= 1e-1
        case 'cm':
            valore *= 1e-2
        case 'mm':
            valore *= 1e-3
    return valore

def converti_in_coulomb(valore, unit):
    match(unit.lower()):
        case 'mc':
            valore *= 1e-3
        case 'uc':
            valore *= 1e-6
        case 'nc':
            valore *= 1e-9
        case 'pc':
            valore *= 1e-12
    return valore

class CampoElettrico:
    def __init__(self, distanze, cariche):
        self.k = K
        self.cariche = cariche
        self.distanze = distanze

    def calcola_campo_elettrico(self):
        campo_totale = np.array([0.0, 0.0, 0.0])
        for carica, distanza in zip(self.cariche, self.distanze):
            # Calcolare la direzione del campo elettrico
            direzione = distanza / np.linalg.norm(distanza)
            campo_parziale = self.k * carica / (np.linalg.norm(distanza) ** 2)
            campo_totale += campo_parziale * direzione
        return np.round(campo_totale, 2)

class PotenzialeElettrico:
    def __init__(self, distanze, cariche):
        self.k = K
        self.cariche = cariche
        self.distanze = distanze

    def calcola_potenziale_elettrico(self):
        potenziale_totale = 0
        for carica, distanza in zip(self.cariche, self.distanze):
            potenziale_parziale = self.k * carica / np.linalg.norm(distanza)
            potenziale_totale += potenziale_parziale
        return np.round(potenziale_totale, 2)

class ForzaElettrica:
    def __init__(self, carica, campo_elettrico_totale):
        # Carica sulla quale agisce la forza
        self.carica = carica
        self.campo_elettrico = campo_elettrico_totale

    def calcola_forza_elettrica(self):
        return abs(self.carica) * self.campo_elettrico
    
class Distanza:
    def __init__(self, posizioni_cariche):
        """
        posizioni_cariche: lista di tuple [(posizione1, carica1), (posizione2, carica2), ...]
        """
        self.posizioni = np.array([posizione for posizione, carica in posizioni_cariche])
        self.cariche = np.array([carica for posizione, carica in posizioni_cariche])

    def calcola_vettori_distanza(self, posizione_origine):
        """
        Calcola i vettori distanza tra ogni carica e l'origine.
        posizione_origine: coordinate del punto di interesse [x0, y0, z0]
        Restituisce un array con i vettori distanza.
        """
        origine = np.array(posizione_origine)
        vettori_distanza = self.posizioni - origine
        return np.round(vettori_distanza, 5)
