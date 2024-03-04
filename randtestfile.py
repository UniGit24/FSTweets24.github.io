import csv
List = ["hey","hi","yo","hi"]
with open('FINALAUS1.csv', 'a', newline = '') as f_object:
    writer_object = csv.writer(f_object)
    writer_object.writerow(List)
f_object.close() 