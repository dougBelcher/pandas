# Use pandas to extract data from Excel and write to SQL text file
import pandas as pd

Sensi = pd.read_excel('/Users/Doug/Documents/My Dropbox/Yellow Folders/Python/Sensi 08737561.xlsx')

# writer = pd.ExcelWriter('/Users/Doug/Documents/My Dropbox/Yellow Folders/Python/Sensi 08737561(0).xlsx')

# Open the SQL text file
file1 = open("/Users/Doug/Documents/My Dropbox/Yellow Folders/Python/Sensi.sql", "w+")

# Open another text file
file2 = open("/Users/Doug/Documents/My Dropbox/Yellow Folders/Python/Sensi.txt", "w+")

# Start writing SQL statements to file
file1.write("Select *\n\tfrom wrddta/f55203\n\twhere mdpsn in (\'")

Sensi['SN'] = Sensi.Serial_Numbers.astype("string").str.split(pat="-")

for serial in Sensi.SN:
    for nbr in serial:
        file1.write(nbr + "\', \'")

file1.write(")\n")

# file2.write("\'")
for serial in Sensi.SN:
    for nbr in serial:
        file2.write("\'" + nbr + "\n")

# writer.save()

file1.close()
file2.close()
