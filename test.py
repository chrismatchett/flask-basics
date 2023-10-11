import csv

# # Read a CSV file
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)

# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# Write a CSV File
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow([1, 2, 3.141592, 4])
# outputFile.close()

import csv
exampleFile = open('Marvel_Comics.csv', encoding="utf8")
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['comic_name'])




    
    
