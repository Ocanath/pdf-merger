from pypdf import PdfMerger

pdfs = ['ch1.pdf', 'ch2.pdf', 'ch3.pdf', 'ch4.pdf', 'ch5.pdf', 'ch6.pdf', 'ch7.pdf', 'appendix.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_pdf.pdf")
merger.close()

