import csv

years = [1991, 1993, 1995, 1997, 2000, 2003, 2006, 2010, 2015, 2020]

songs = [
    "Beat the Drums",
    "Louder!",
    "Street Shadows",
    "The Power of the Night",
    "At the Edge",
    "Roads of Light",
    "Point of No Return",
    "All That We Love",
    "Step into the Unknown",
    "Fall and Rise"
]

with open('Kunteynir.csv',"w", newline='') as f:
    field = ["Song", "Year"]
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    for i in range(len(years)):
        writer.writerow({
            "Song" : songs[i],
            "Year" : years[i]
        })


with open('Kunteynir.csv', newline='') as f:
    reader = csv.DictReader(f)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row["Song"], row["Year"])
print('Done')