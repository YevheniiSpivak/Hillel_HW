import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new.csv', 'w', newline='') as csv_file_new:
        field_names = ['email']
        csv_writer = csv.DictWriter(csv_file_new, fieldnames=field_names)

        csv_writer.writeheader()

        for row in csv_reader:
            del row['first_name']
            del row['last_name']
            csv_writer.writerow(row)
