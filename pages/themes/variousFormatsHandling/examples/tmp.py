# import csv

# # Open the file
# with open('sample_data.csv',newline='') as f:
#     # Create a CSV reader:
#     csv_reader = csv.reader(f)

#     # skip header row:
#     headers = next(csv_reader)

#     # print CSV data, sorted by "Price"
#     for row in sorted(csv_reader, key=lambda a:a[1]):
#         print(row)

import csv

with open('sample_data.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')

    for r in reader:
        print(r)