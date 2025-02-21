from operator import itemgetter

L = [
    {"Name": "Python", "Learn": 8, "Trade": 20},
    {"Name": "Java", "Learn": 15, "Trade": 35},
    {"Name": "C#", "Learn": 15, "Trade": 70},
    {"Name": "Javascript", "Learn": 4, "Trade": 50}
]

print(sorted(L, key=itemgetter("Learn"), reverse=True))
