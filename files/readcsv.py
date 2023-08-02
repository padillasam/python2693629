import csv
# with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:
with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)    
    for elemento in csvReader:
        #if csvReader.index!=0:
        print(f"Nombre={elemento[0]}")
        print(f"Apellido={elemento[1]}")
        print(f"Correo={elemento[2]}")
        print(f"Documento={elemento[3]}")



    # for row in csvReader:
    #     #print(row)
    #     print('first name:',row[0])
    #     print('last name:',row[1])
    #     print('email:',row[2])
    #     print('id:',row[3])