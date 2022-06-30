import PyPDF2 as pdf

def readPDF(fileName):
    file = open(fileName, "rb")
    pdf_reader = pdf.PdfFileReader(file)

    text = ""

    for i in range(pdf_reader.getNumPages()):
        text = '\n' + pdf_reader.getPage(i).extractText()

    return text

print(readPDF('example.pdf'))