#Leitura de arquivo CSV

import csv

with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

