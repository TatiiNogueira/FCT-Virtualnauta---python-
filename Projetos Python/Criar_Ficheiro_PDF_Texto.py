#Criar ficheiro PDF

#Módulos 
from fpdf import FPDF

#Indicamos a class pdf
pdf = FPDF()
#Indicamos que queremos adicionar uma página
pdf.add_page()
#Indicamos o tipo de letra e o tamanho
pdf.set_font("Arial",size=30)
#Indicamos a posição e texto que queremos
pdf.cell(200,100, txt = "Welcome to Python PDF", ln=1, align="C")
#Nome que queremos atribuir ao ficheiro PDF 
pdf.output("Python.pdf") 