import csv

def csv_reader(file_name):
    with open(f'{file_name}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader: 
            if line_count == 0:
                line_count += 1
            else:
                if row[0].isdigit() == True:
                    file_number, song_title, artist_name  = row[0], row[2], row[3]
                    shazam_file_name = song_title + ' - ' + artist_name
                    print(file_number, " - " + shazam_file_name)
                else:
                    pass
def files(file):
    num_rows = 0
    for row in open(file):num_rows += 1
    print(num_rows)
file = 'shazamlibrary.csv'
files(file)
#csv_reader(file)