#Código que faz merge de arquivos PDF

from PyPDF2 import PdfFileMerger

pdfs = ['arquivo1.pdf', 'arquivo2.pdf', 'arquivo3.pdf']

agrupador = PdfFileMerger()

for pdf in pdfs:
    agrupador.append(pdf)

agrupador.write("resultado.pdf")
agrupador.close()
