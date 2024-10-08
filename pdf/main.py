import textwrap

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Customize your header here (e.g., add logo, title, etc.)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Your Header Here', 0, 1, 'C')

    def footer(self):
        # Customize your footer here (e.g., add page number, copyright info, etc.)
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')


def txt_to_pdf(txt_filename, pdf_filename):
    pdf = PDF()
    pdf.add_page()

    # Add introductory paragraph
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'Smallpdf provides various services to enhance your documents.')

    # Add feature sections
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 10, 'Features:')
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, ' Enhance documents on one click')
    pdf.multi_cell(0, 10, ' Access files anytime, anywhere')
    pdf.multi_cell(0, 10, ' Collaborate with others')

    # Add bottom options (login buttons, social media links, etc.)

    # Save the PDF
    pdf.output(pdf_filename)


def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')


# Usage: Replace 'your_text_file.txt' and 'output.pdf' with your actual filenames


input = "outputboss.txt"
output = "output.pdf"
file = open("outputboss.txt")
text = file.read()
file.close()
text_to_pdf(text, "output.pdf")