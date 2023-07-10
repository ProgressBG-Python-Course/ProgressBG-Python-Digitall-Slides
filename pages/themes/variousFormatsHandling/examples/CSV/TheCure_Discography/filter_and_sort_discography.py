import csv
with open('TheCure_Discography.csv') as f:
    f_csv = csv.reader(f, delimiter=';')
    headers = next(f_csv)

    for row in filter(
        lambda l: "Fiction Records" in l[1] and 1980 <= int(l[2]) <= 1989,
        f_csv
    ):
        print(row)
