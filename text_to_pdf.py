import os
from fpdf import FPDF # Usado para criar o PDF

###################
# Cria a classe PDF que extende FPDF 
# para utilizar o método footer.
class PDF(FPDF):
    # Função que cria o cabeçalho
    def cabecalho(self, arquivo):
        # Define a fonte e escreve o titulo centralizado
        self.set_font('Arial', style='B', size=20)
        self.cell(80) # Formatação
        self.cell(30, 10, txt=arquivo.readline(), ln=1, align='C')
        self.ln(10) # Formatação

    # Função que cria o corpo do texto
    def corpo(self, arquivo):
        # Define a fonte 
        self.set_font('Arial', size=14)

        # E escreve as linhas do corpo do texto
        for i in arquivo:
            self.multi_cell(0, 5, txt=i, align='J')

    # Função que cria o rodapé
    def footer(self):
        self.set_y(-15) # Move em mm de baixo para cima
        # Seleciona a fonte e mostra  o número da página
        self.set_font('Arial', style='I', size=10)
        self.cell(0, 10, txt=f'Página {self.page_no()}', align='C')

###################
def main():
    lista_arquivos = [
        "prologo.txt", "cap1.txt", "cap2.txt", 
        "cap3.txt", "epilogo.txt" 
    ] # Uma lista contendo o nome dos arquivos .txt
      # que serão lidos 

    # Diretório onde se encontra este arquivo
    diretorio_sistema = os.path.dirname(os.path.abspath(__file__))
    # Diretório onde estão os arquivos texto
    diretorio_arquivos = os.path.join(diretorio_sistema, "text_files/")
    # Cria objeto PDF
    pdf = PDF()

    # Gera o arquivo PDF
    for i in lista_arquivos:
        arquivo = open(diretorio_arquivos+i, "r") # Abre próximo arquivo .txt
        
        pdf.add_page() # Adiciona uma página
        pdf.cabecalho(arquivo) # Cria o header
        pdf.corpo(arquivo) # Cria o corpo do texto
        # O footer é utilizado por padrão pela biblioteca
        # eu apenas reescrevi as informações que ele mostra

        arquivo.close() # Fecha o arquivo atual

    # Salva o arquivo PDF 
    pdf.output("output.pdf")

###################
if __name__ == '__main__':
    main()