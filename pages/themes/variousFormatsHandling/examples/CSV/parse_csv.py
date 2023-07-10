import csv

with open('sample_data.csv') as f:
  # read CSV file:
  f_csv = csv.reader(f)

  # skip header row:
  headers = next(f_csv)

  # print data, sorted by "Price"
  for row in sorted(f_csv, key=lambda a:a[1]):
    print(row)