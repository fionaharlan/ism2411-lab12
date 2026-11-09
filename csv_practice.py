# Fiona Harlan
# Module 12 Lab: read a sales csv, write a cleaned report

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("---exercise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print("---exercise 2---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


