import csv
import sys

# open file for reading
with open(sys.argv[1], 'r') as f:
    # open file for writing
    with open(sys.argv[2], 'w') as tsv:
        # create reader object
        reader = csv.reader(f, delimiter=',')
        # create writer objectS
        writer = csv.writer(tsv, delimiter='\t')
        # write each row to the new file
        for row in reader:
            writer.writerow(row)