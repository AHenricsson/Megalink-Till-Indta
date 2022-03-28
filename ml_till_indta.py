#!/usr/bin/python3
import csv

def main():
    indtaFil = "Från indta.csv"
    mlFil = "Från Megalink.csv"
    resultatFil = "Resultat.csv"
    with open(mlFil, newline='',encoding='ISO-8859-1') as mlcsv:
        mlReader = csv.reader(mlcsv, delimiter=',')
        mlDict = {}
        for row in mlReader:
            if len(row)>=7:
                mlDict[row[1]]=[row[0],*row[2:7]]
        with open(indtaFil, newline='') as csvfile:
            indtaReader = csv.reader(csvfile, delimiter=';', quotechar='"')
            with open(resultatFil,'w', newline='') as results:
                writer = csv.writer(results, delimiter=';',quotechar='"')
                for row in indtaReader:
                    name = row[9].upper()+ " " +row[8]
                    if name in mlDict:
                        mlRow = mlDict[name]
                        plac = mlRow[0]
                        series = mlRow[3].replace('.',',').split()
                        total = mlRow[4]
                        inner = mlRow[5]
                        outRow = row[:29]+[plac] + series + [total, inner] + ['0','','']
                        writer.writerow(outRow)
                    else:
                        writer.writerow([row[0].replace('"','')]+row[1:])

if  __name__ == "__main__":
    main()


