import unittest
from funzioni import *

'''
    DATI DA CAMBIARE PER EFFETTUARE I TEST SU DIVERSI MODELLI

        se avete bisogno di cambiare il modello da quadrato
        ad altra forma geometrica, dovrete cambiare la
        posizione delle cariche.

    PER VEDERE SE VI TORNANO I RISULTATI CON LA REALTA' DOVETE
    TOGLIERE IL COMMENTO A:
             self.assertAlmostEqual()
    E ASSEGNARE IL VOSTRO RISULTATO AL RISULTATO ATTESO
'''

DISTANZA_BASE=5.2                   # distanza base del problema
UNITA_DI_MISURA_DISTANZA='CM'       # unità di misura della distanza
CARICA_BASE=11.8                    # valore della carica base del problema
UNITA_DI_MISURA_CARICA='nC'         # unità di misura della carica base
INDICE_CARICA=4                     # carica numero 1


class TestElettrostatica(unittest.TestCase):

    def test_campo_elettrico(self):
        # Parametri iniziali
        q_base = converti_in_coulomb(CARICA_BASE, UNITA_DI_MISURA_CARICA)
        misura_base = converti_in_metri(DISTANZA_BASE, UNITA_DI_MISURA_DISTANZA)

        # Posizioni e cariche
        posizioni_cariche = [
            ([-0.5 * misura_base, 0.5 * misura_base, 0], 1 * q_base),
            ([0.5 * misura_base, 0.5 * misura_base, 0], -2 * q_base),
            ([0.5 * misura_base, -0.5 * misura_base, 0], 2 * q_base),
            ([-0.5 * misura_base, -0.5 * misura_base, 0], -1 * q_base)
        ]

        # Calcolo del campo elettrico
        distanza = Distanza(posizioni_cariche)
        vettori_distanza = distanza.calcola_vettori_distanza([0, 0, 0])
        cariche = [carica for _, carica in posizioni_cariche]
        campo = CampoElettrico(vettori_distanza, cariche)
        campo_elettrico = campo.calcola_campo_elettrico()

        # Risultati attesi
        '''
        risultato_atteso_campo = [0, -1.1098574e+05, 0]  # Componenti i, j, k del campo elettrico
        for componente_atteso, componente_calcolato in zip(risultato_atteso_campo, campo_elettrico):
            self.assertAlmostEqual(componente_atteso, componente_calcolato, places=2)
        '''
        # Calcolo del potenziale elettrico
        potenziale = PotenzialeElettrico(vettori_distanza, cariche)
        potenziale_elettrico = potenziale.calcola_potenziale_elettrico()

        # Risultato atteso del potenziale elettrico
        risultato_atteso_potenziale = 0  # Potenziale elettrico totale
        '''
        self.assertAlmostEqual(risultato_atteso_potenziale, potenziale_elettrico, places=2)
        '''
        indice_carica = INDICE_CARICA - 1
        q_forza = cariche[indice_carica]
        forza_elettrica = ForzaElettrica(q_forza, campo_elettrico).calcola_forza_elettrica()

        print("\nCampo elettrico totale:")
        print(f"Componente i: {np.format_float_scientific(campo_elettrico[0], precision=2)}")
        print(f"Componente j: {np.format_float_scientific(campo_elettrico[1], precision=2)}")
        print(f"Componente k: {np.format_float_scientific(campo_elettrico[2], precision=2)}\n")
        # Stampa del potenziale elettrico (che è scalare)
        print(f"Potenziale elettrico totale: {np.format_float_scientific(potenziale_elettrico, precision=2)}\n")
        print("Vettori di distanza:")
        for i, vettore in enumerate(vettori_distanza, start=1):
            print(f"Vettore di distanza {i}: i: {vettore[0]}, j: {vettore[1]}, k: {vettore[2]}")
        print("\n")
        print(f"Forza agente su carica {indice_carica + 1}")
        print(f"Componente i: {np.format_float_scientific(forza_elettrica[0], precision=2)}")
        print(f"Componente j: {np.format_float_scientific(forza_elettrica[1], precision=2)}")
        print(f"Componente k: {np.format_float_scientific(forza_elettrica[2], precision=2)}\n")


if __name__ == '__main__':
    unittest.main()