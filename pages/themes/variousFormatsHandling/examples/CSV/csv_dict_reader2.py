import csv
with open('sample_data.csv',newline='') as f:
  reader = csv.DictReader(f, delimiter=',')

  for r in reader:
    print(r)

