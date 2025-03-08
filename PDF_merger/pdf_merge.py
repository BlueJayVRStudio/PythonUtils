from pypdf import PdfWriter

# pdf file names; get input pdf's from ./1_input/
pdf_files = [f"./1_input/{i}.pdf" for i in range(1, 4)]
print(pdf_files)

# instantiate (get handle to) PdfMerger
merger = PdfWriter()

# append all PDFs
for pdf in pdf_files:
    merger.append(pdf)

# write output pdf to ./2_output/
merger.write("./2_output/output.pdf")
merger.close()

print("Success")
