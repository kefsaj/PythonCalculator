#Python program


import csv

new_rows = []

with open('file.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        row = [int(val) for val in row]
        row.append(sum(row))
        new_rows.append(row)

with open('file.csv', 'w') as csvfile:
    csv.writer(csvfile).writerows(new_rows)


# add function

def add(n1, n2):
    return n1 + n2

# Subract function

def subtract(n1, n2):
    return n1 - n2

# Multi Function

def multiply(n1, n2):
    return n1 * n2

# divide function

def divide(n1, n2):
    return n1 / n2

