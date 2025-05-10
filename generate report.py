import csv
from statistics import mean, median, stdev
from fpdf import FPDF

# Read data from a CSV file
def read_data(filename):
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        return [(row['Name'], int(row['Score'])) for row in reader]

# Analyze data
def analyze_data(data):
    scores = [score for _, score in data]
    return {
        'mean': mean(scores),
        'median': median(scores),
        'stdev': stdev(scores),
        'max': max(scores),
        'min': min(scores)
    }

# Generate a formatted PDF report
def generate_pdf(data, stats, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Internship Performance Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "Name", border=1)
    pdf.cell(40, 10, "Score", border=1)
    pdf.ln()

    pdf.set_font("Arial", '', 12)
    for name, score in data:
        pdf.cell(100, 10, name, border=1)
        pdf.cell(40, 10, str(score), border=1)
        pdf.ln()

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, "Statistics Summary", ln=True)

    for key, value in stats.items():
        pdf.set_font("Arial", '', 12)
        pdf.cell(200, 10, f"{key.capitalize()}: {value:.2f}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(200, 10, "Completion certificate will be issued on your internship end date.", ln=True, align='C')
    
    pdf.output(output_filename)

# Main execution
if __name__ == "__main__":
    input_file = "data.csv"
    output_pdf = "sample_report.pdf"
    
    data = read_data(input_file)
    stats = analyze_data(data)
    generate_pdf(data, stats, output_pdf)
    
    print(f"Report generated successfully: {output_pdf}")