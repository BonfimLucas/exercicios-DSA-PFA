
import pandas as pd
file = ('C:/Users/lucas/Desktop/Pastas/Programação/Python/Exercicios DSA/cap003/binary.csv')

def leitura(file):
        arquivo = pd.read_csv(file)
        return arquivo.describe()
        
leitura(file)
