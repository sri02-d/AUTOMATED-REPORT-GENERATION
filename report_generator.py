import pandas as pd
from fpdf import FPDF

# Step 1: Read data
data_file = "data.csv"
df = pd.read_csv(data_file)

# Step 2: Analyze data
total_employees = len(df)
average_salary = df['Salary'].mean()
max_salary = df['Salary'].max()
min_salary = df['Salary'].min()
salary_by_department = df.groupby('Department')['Salary'].mean()

# Step 3: Create PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(200, 10, 'Employee Salary Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add summary
pdf.cell(200, 10, f"Total Employees: {total_employees}", ln=True)
pdf.cell(200, 10, f"Average Salary: {average_salary:.2f}", ln=True)
pdf.cell(200, 10, f"Maximum Salary: {max_salary}", ln=True)
pdf.cell(200, 10, f"Minimum Salary: {min_salary}", ln=True)
pdf.ln(10)

# Salary by department
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Average Salary by Department:", ln=True)
pdf.set_font("Arial", size=12)

for dept, salary in salary_by_department.items():
    pdf.cell(200, 10, f"{dept}: {salary:.2f}", ln=True)

# Save PDF
pdf.output("report.pdf")
print("Report generated successfully as 'report.pdf'")
