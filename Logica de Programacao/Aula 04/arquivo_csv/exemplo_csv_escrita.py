import csv

linha = [['Amanda', 28],
        ['Felipe', 29],
        ['Jhonnatha', 22]]

with open('arquivo2_csv.csv', 'w', encoding='utf-8', newline='') as f:
    escritor = csv.writer(f, delimiter=';')
    escritor.writerow(linha)
    escritor.writerows(linha)

