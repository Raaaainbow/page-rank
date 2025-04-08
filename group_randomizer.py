import random

players = ["Sebastian", "Marguerite", "Victor", "Caroline", "Katarina", "Sophia"]

titles = [
    "Grafteori model stuff",
    "Link matricen og Random Surfer Modellen",
    "Rekursiv Model og Matrix Formulering",
    "Markov matricen: Egenskaber og Dæmpning i PageRank",
    "PageRank algoritmen: Iterativ Konvergens og Dæmpning i Markov Matricer",
    "Analyse af PageRank Modeller og Undersøgelse af Dæmpning"
]

random.shuffle(titles)
# Shuffle players for randomness
random.shuffle(players)
halfpoint = round(len(players)/2)
pairs = []
for i in range(0,halfpoint):
    pairs.append(players[i] + " og " + players[i+halfpoint])
    
chosenPair = 0 
for i in range(0,len(titles)):
    print(titles[i] + ": " + pairs[chosenPair])
    chosenPair += 1
    if chosenPair >= halfpoint:
        chosenPair = 0
    
