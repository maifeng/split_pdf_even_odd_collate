from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

input_file = sys.argv[1]
num_of_output_files = int(sys.argv[2])
output_prefix = sys.argv[3]

PDF_Entry = input_file
Pdf_File = PdfFileReader(open(PDF_Entry, "rb"))


def split_pdf_to_pages():
    inputpdf = Pdf_File
    outputs = []
    for j in range(num_of_output_files):
        outputs.append(PdfFileWriter())
    for i in range(inputpdf.numPages):
        j = i % num_of_output_files
        outputs[j].addPage(inputpdf.getPage(i))
    for j in range(num_of_output_files):
        with open(output_prefix + "_%s.pdf" % j, "wb") as outputStream:
            outputs[j].write(outputStream)

split_pdf_to_pages()
