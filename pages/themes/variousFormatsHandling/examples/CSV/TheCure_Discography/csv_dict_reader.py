import csv
with open('TheCure_Discography.csv',newline='') as f:
  reader = csv.DictReader(f, delimiter=';')

  for r in reader:
    print(r)

