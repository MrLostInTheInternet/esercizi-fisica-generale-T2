from funzioni import *

# Chiedere il numero totale di cariche
numero_cariche = int(input("Inserisci il numero totale di cariche: "))

# Chiedere il valore di base della carica
q_base = input("Inserisci quanto vale la carica di base in Coulomb: ")
q_base = converti_in_coulomb(float(q_base), 'nC')

# Chiedere la misura di base per le distanze
misura_base = input("Inserisci la misura di base per le distanze (in cm): ")
misura_base = converti_in_metri(float(misura_base), 'cm')

# Inizializzazione della lista delle posizioni e cariche
posizioni_cariche = []

# Ottenere i dettagli per ciascuna carica
for i in range(1, numero_cariche + 1):
    # Valore moltiplicatore per la carica
    moltiplicatore_q = float(input(f"Inserisci il moltiplicatore per la carica {i}: "))
    
    # Ottenere i moltiplicatori per le coordinate della carica
    moltiplicatore_x = float(input(f"Inserisci il moltiplicatore per la coordinata x della carica {i}: "))
    moltiplicatore_y = float(input(f"Inserisci il moltiplicatore per la coordinata y della carica {i}: "))
    moltiplicatore_z = float(input(f"Inserisci il moltiplicatore per la coordinata z della carica {i}: "))

    # Calcolare le coordinate effettive
    x = moltiplicatore_x * misura_base
    y = moltiplicatore_y * misura_base
    z = moltiplicatore_z * misura_base

    # Aggiungere la tupla (posizione, carica) alla lista
    posizioni_cariche.append(([x, y, z], moltiplicatore_q * q_base))

# Coordinata del punto di interesse
posizione_origine = [0, 0, 0]

distanza = Distanza(posizioni_cariche)
vettori_distanza = distanza.calcola_vettori_distanza(posizione_origine)

cariche = [carica for _, carica in posizioni_cariche]
campo = CampoElettrico(vettori_distanza, cariche)
campo_elettrico = campo.calcola_campo_elettrico()

# Stampa delle componenti i, j, k per il campo elettrico
print("\nCampo elettrico totale:")
print(f"Componente i: {np.format_float_scientific(campo_elettrico[0], precision=2)}")
print(f"Componente j: {np.format_float_scientific(campo_elettrico[1], precision=2)}")
print(f"Componente k: {np.format_float_scientific(campo_elettrico[2], precision=2)}\n")

potenziale = PotenzialeElettrico(vettori_distanza, cariche)
potenziale_elettrico = potenziale.calcola_potenziale_elettrico()

# Stampa del potenziale elettrico (che è scalare)
print(f"Potenziale elettrico totale: {np.format_float_scientific(potenziale_elettrico, precision=2)}\n")

# Stampa delle distanze
print("Vettori di distanza:")
for i, vettore in enumerate(vettori_distanza, start=1):
    print(f"Vettore di distanza {i}: i: {vettore[0]}, j: {vettore[1]}, k: {vettore[2]}")
print("\n")

forza_su_q = int(input("Inserisci il numero della carica sulla quale vuoi calcolare la forza elettrica (es. 1 o 4): "))
q_forza = cariche[forza_su_q - 1]
forza_elettrica = ForzaElettrica(q_forza, campo_elettrico).calcola_forza_elettrica()
print(f"\nLa forza elettrica che agisce sulla carica di indice {forza_su_q} equivale a: {forza_elettrica}\n")
