from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs=[]
n=int(input("How many PDFs do you wanna merge?\n"))
for i in range(0,n):
    name=input(f"Enter the name of PDF {i+1}: ")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)

for pdf in ["pdf1.pdf", "pdf2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
