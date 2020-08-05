import csv

with open('/home/rahul/Desktop/Music', 'r') as csv_file:
    csv_reader = csv_reader(csv_file)

    for lines in csv_reader:
        print(lines)