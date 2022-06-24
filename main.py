import csv

total = 0
inicjaly = []
imiona_nazwiska = []
kwota = []
with open("Lista_operacji_20220624_111319.csv","r") as plik:
    plik_csv = csv.DictReader(plik, delimiter=";")
    
    for row in plik_csv:
        row["Kwota operacji"] = row["Kwota operacji"].replace(",",".")
        row["Tytułem"] = row["Tytułem"].lower()
        
        if "saic" in row["Tytułem"]:
            total += float(row["Kwota operacji"])
            kwota.append(float(row["Kwota operacji"]))
            imiona_nazwiska = row["Nadawca / Odbiorca"].split()
            inicjaly.append([imiona_nazwiska[0][0], imiona_nazwiska[1][0]])
    print(total)
   
with open("rozliczenie.csv", "w") as plik:
    plik_csv = csv.writer(plik,delimiter=";")
    plik_csv.writerow(["Inicjały","Kowota"])
    for i in range(len(kwota)):
        plik_csv.writerow([inicjaly[i], kwota[i]])
    