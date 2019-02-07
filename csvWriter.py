import csv
def writer(data,filename):
    with open(filename, "a",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


