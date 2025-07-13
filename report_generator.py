import csv
from fpdf import FPDF

# Read data from CSV
total = 0
count = 0
rows = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # skip header
    for row in reader:
        rows.append(row)
        temp = int(row[1])
        total += temp
        count += 1

average = total / count

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Weather Report", ln=True, align='C')
pdf.ln(10)

# Table header
pdf.cell(100, 10, txt="City", border=1)
pdf.cell(40, 10, txt="Temperature", border=1)
pdf.ln()

# Table rows
for row in rows:
    pdf.cell(100, 10, txt=row[0], border=1)
    pdf.cell(40, 10, txt=row[1], border=1)
    pdf.ln()

pdf.ln(10)
pdf.cell(200, 10, txt=f"Average Temperature: {average:.2f}°C", ln=True)

# Save PDF
pdf.output("report.pdf")

print("Report generated successfully: report.pdf")
