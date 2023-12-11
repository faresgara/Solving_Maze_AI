from collections import deque

import random

graphA = {
    'A': ['G', 'B'],
    'G': ['M', 'H', 'A'],
    'H': ['O', 'C', 'B', 'G'],
    'C': ['J', 'D', 'B', 'H'],
    'J': ['P', 'E', 'D', 'C'],
    'E': ['D', 'J', 'K'],
    'P': ['U'],
    'B': [],
    'M': [],
    'D': [],
    'K': [],
}

graphF = {
    'F': ['L'],
    'L': ['R', 'V', 'K'],
    'R': ['X', 'W'],
    'W': ['X', 'R', 'Z'],
    'Z': ['W', 'V'],
    'K': [],
    'V': [],
    'X': [],
}

graphY = {
    'Y': ['S'],
    'S': ['Y', 'T', 'M'],
    'T': ['V', 'O', 'S'],
    'O': ['I', 'H', 'N', 'T'],
    'H': ['O', 'C', 'B', 'G'],
    'G': ['M', 'H', 'A'],
    'A': ['G', 'B'],
    'C': ['J', 'D', 'B', 'H'],
    'J': ['P', 'E', 'D', 'C'],
    'E': ['D', 'J', 'K'],
    'P': ['U'],
    'M': [],
    'N': [],
    'I': [],
    'B': [],
    'D': [],
    'K': [],
}

graphZ = {
    'Z': ['W', 'V'],
    'W': ['X', 'R', 'Z'],
    'R': ['L', 'W', 'X'],
    'L': ['F', 'K', 'R'],
    'F': ['L'],
    'V': [],
    'X': [],
    'K': [],
}

piege = ['B', 'D', 'I', 'K', 'M', 'N', 'cV', 'X']


def depth_first(graphe, depart, but):
    ouvert = deque([depart])
    ferme = []
    parcours = []

    while ouvert:
        n = ouvert.pop()
        parcours.append(n)
        print(n)
        if n == but:
            print("Trésor Trouvé")
            return parcours
        if n in piege:
            print("Piégé", n)
        ferme.append(n)
        for successeur in graphe[n]:
            if successeur not in ferme:
                ouvert.append(successeur)
                ferme.append(successeur)
    return "Pas de chemin disponible pour le trésor"


graph = {'A': graphA, 'F': graphF, 'Y': graphY, 'Z': graphZ}
entre = ['A', 'F', 'Y', 'Z']
char = random.choice(entre)

for i in graph:
    if i == char:
        print("Vous avez choisi l'entrée", "|", i, "|")
        print(depth_first(graph[i], i, 'U'))
