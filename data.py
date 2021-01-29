from train import Train
from parse import load

with open('nancy_besancon.csv') as f:
    aller = list(load(f))

with open('besancon_nancy.csv') as f:
    retour = list(load(f))
