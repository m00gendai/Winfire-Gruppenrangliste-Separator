import csv

resultK = []
resultAk = []
kantonaleVereine = [
    "Schaffhausen",
    "Hallau",
    "Neunkirch",
    "Stein am Rhein",
    "Löhningen",
    "Neuhausen",
    "Neuhausen a/Rhf.",
    "Beggingen",
    "Löhningen",
    "Schleitheim"
    ]

with open('Gruppenrangliste Gesamt.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    group = []
    subgroup = []
    for row in reader:
        flag = False
        if row[0].isdigit() and row[1].isdigit():
            flag = True
            subgroup = []
            a = [row[0], row[1], row[5], row[6], row[8]]
            subgroup.append(a)
        if row[0].isdigit() and not row[1].isdigit():
            b = [row[0], row[1], row[2], row[3], row[4], row[5]]
            subgroup.append(b)
        if len(subgroup) > 1:
            group.append(subgroup)
            
    for i in group:
        if i[0][3] in kantonaleVereine:
            if i not in resultK: 
                resultK.append(i)
        else:
            if i not in resultAk: 
                resultAk.append(i)

k = open('kantonal.csv', 'w', newline='')
writerK = csv.writer(k)
indexK = 1
for row in resultK:
    for each in row:
        if each[0].isdigit() and each[1].isdigit():
            writerK.writerow("")
            writerK.writerow([indexK, each[1], each[2], None, None, each[3] + " " + each[4]])
            indexK += 1
        else:
            writerK.writerow(each)
k.close()

ak = open('ausserkantonal.csv', 'w', newline='')
writerAk = csv.writer(ak)
indexAk = 1
for row in resultAk:
    for each in row:
        if each[0].isdigit() and each[1].isdigit():
            writerAk.writerow("")
            writerAk.writerow([indexAk, each[1], each[2], None, None, each[3] + " " + each[4]])
            indexAk += 1
        else:
            writerAk.writerow(each)
ak.close()
