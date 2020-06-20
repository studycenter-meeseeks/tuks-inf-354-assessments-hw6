inFile = open('file-with-duplicates.csv','r')

outFile = open('duplicates-removed.csv','w')

csv_without_duplicates = []
found_duplicates = []

for line in inFile:

    if line in csv_without_duplicates:
        found_duplicates.append(line)
        continue

    else:
        outFile.write(line)
        csv_without_duplicates.append(line)

outFile.close()

inFile.close()


original_csv_records = len(found_duplicates) + len(csv_without_duplicates)
output = f"""
Original CSV records:
{original_csv_records}

Number of duplicates:
{len(found_duplicates)}

duplicates-removed.csv created with {len(csv_without_duplicates)} records
"""



print(output)

