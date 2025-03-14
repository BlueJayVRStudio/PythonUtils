import os # We'll just use it to list input items
from pypdf import PdfWriter # https://github.com/py-pdf/pypdf

# pdf file names; get input pdf's from "./1_input/"
pdf_files = [f"./1_input/{filename}" for filename in os.listdir("./1_input")]
print(pdf_files)

# Instantiate PdfMerger
merger = PdfWriter()

# Append all PDFs
for pdf in pdf_files:
    merger.append(pdf)

# Write output pdf to ./2_output/
merger.write("./2_output/output.pdf")
merger.close()

print("Success")
