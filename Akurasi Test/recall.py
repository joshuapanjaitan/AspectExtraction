import csv
import clean
import nltk
from nltk import word_tokenize

acuan = clean.trainFeature()  # data acuan

test = []
with open("Akurasi Test File.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        test.append(line)

# hitung recall
Recall = []
for t in range(len(acuan)):
    hasil = 0
    test1 = test[t]
    acuan1 = acuan[t]
    # print(acuan1)
    if test1 == [] and acuan1 == ['']:
        total = 1
    else:
        for i in range(len(test1)):
            text = word_tokenize(test1[i])
            if len(text) > 1:
                for x in range(len(text)):
                    hit = text[x]
                    for line in acuan1:
                        if hit in line:
                            hasil += 0.5
            else:
                if test1[i] in acuan1:
                    hasil += 1
        bawah = len(test1)
        if bawah == 0:
            bawah = 0.00001
        total = hasil/bawah
        if total > 1:
            total = 1
    Recall.append(total)
# print(Recall)
"""
with open("Recall.csv", 'w', newline='') as f:
    tulis = csv.writer(f)
    for j in range(len(Recall)):
        tulis.writerow([Recall[j]])
"""
