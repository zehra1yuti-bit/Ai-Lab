"""Generates mock CSV datasets for Lab 2 and onwards directly in C:\ai-lab\data."""
import csv
from pathlib import Path

# ዳታውን በቀጥታ ዋናው C:\ai-lab ስር ባለው data ፎልደር ውስጥ እንዲፈጥር ማድረግ
Path("../data").mkdir(exist_ok=True)

# 1. ርዕስ (Header) እና መረጃዎች (Data rows)
header = ["id", "study_hours", "attendance", "final_score"]
students_data = [
    [1, 12.5, 95, 88],
    [2, 4.0, 60, 42],
    [3, 15.0, 98, 95],
    [4, 8.5, 80, 70],
    [5, 2.0, 50, 35],
    [6, 10.0, 85, 78],
    [7, 14.0, 92, 90],
    [8, 6.5, 75, 60],
]

# 2. 408 ረድፎችን ማመንጨት
extended_students = [header]  # መጀመሪያ ርዕሱን እንጨምራለን

for i in range(1, 409):
    base = students_data[(i - 1) % len(students_data)]
    row = [
        i, 
        max(1.0, float(base[1]) + (i % 3 - 1)), 
        min(100, max(40, int(base[2]) + (i % 5 - 2))), 
        min(100, max(30, int(base[3]) + (i % 4 - 2)))
    ]
    extended_students.append(row)

# 3. CSV ፋይል አድርጎ መጻፍ
with open("../data/students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(extended_students)

print("Successfully generated data/students.csv with 408 rows!")