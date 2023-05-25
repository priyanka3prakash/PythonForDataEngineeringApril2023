import csv

data = [
    ("sno", "country", "city"),
    ("1", "UK", "London"),
    ("2", "UK", "manchester"),
    ("3", "USA", "california"),
]

with open("csvfile.csv", "w") as csvOutput:
    writer = csv.writer(
        csvOutput,
        delimiter="|",
        escapechar=" ",
        quoting=csv.QUOTE_NONE,
        lineterminator="\n",
    )

    for row in data:
        writer.writerow([s.replace("\n", "\\n") for s in row])



"""
Quoting option: <csv.QUOTE_MINIMAL>
John,Doe,25,john@example.com
Jane,Smith,30,jane@example.com
Bob,Brown,N/A,bob@example.com

Quoting option: <csv.QUOTE_ALL>
"John","Doe","25","john@example.com"
"Jane","Smith","30","jane@example.com"
"Bob","Brown","N/A","bob@example.com"

Quoting option: <csv.QUOTE_NONNUMERIC>
John,Doe,"25",john@example.com
Jane,Smith,"30",jane@example.com
Bob,Brown,"N/A",bob@example.com

Quoting option: <csv.QUOTE_NONE>
John,Doe,25,john@example.com
Jane,Smith,30,jane@example.com
Bob,Brown,N/A,bob@example.com
"""