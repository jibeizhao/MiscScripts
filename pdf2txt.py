from pdf2docx import Converter

pdf_file = '$R8RV92D.pdf'
docx_file = '$R8RV92D.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()