import PyPDF2 as pdfp
import tabula as table
document = open('Apostila.pdf', 'br')
ler = pdfp.PdfReader(document)
pagina1 = ler.pages[1]
print(pagina1.extract_text())
tabela = table.read_pdf("motores.pdf", pages = "10")
print(tabela)