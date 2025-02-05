import PyPDF2
import re
from utils.env import PATH_PDF


def pdf_reader():
    with open(PATH_PDF, "rb") as file:
        leitor_pdf = PyPDF2.PdfReader(file)
        
        # Lê somente a primeira página
        pagina = leitor_pdf.pages[0]
        texto = pagina.extract_text()
        # print(texto)
        # print('- - - - - - - - - - - - - - - - - - - - - - - -')

        # # # NOME # # #
        padrao = r"\d{2}/\d{2}/\d{4}\s*(.*?)\s*CNPJ"
        resultado = re.search(padrao, texto)
        valor = resultado.group(1)
        print(f'NOME - {valor}')


        # # # CNPJ # # #
        padrao = r"CNPJ:\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})"
        resultado = re.search(padrao, texto)
        valor = resultado.group(1)
        print(f'CNPJ - {valor}')



        # # # FATOR R # # #
        padrao = r'Fator r:\s*(\d{1,3},\d{2})'
        resultado = re.search(padrao, texto)
        if resultado:
            valor = resultado.group(1)
            print(f'FATOR R - {valor}')
        else:
            print('SEM FATOR R')


        # # # SIMPLES NACIONAL # # #
        padrao = r"SIMPLES NACIONAL"
        resultado_simples_nacional = re.search(padrao, texto)
        if resultado_simples_nacional:
            print("SIMPLES NACIONAL - TRUE")
        else:
            print("SIMPLES NACIONAL- FALSE")



    '''
        # # # MERCADO INTERNO # # #
        padrao = r"Receita Bruta do período de Apuração \(RPA\)[^\d]*(\d[\d.,]*)"
        resultado = re.search(padrao, texto)
        valor = resultado.group(1)
        print(f'MERCADO INTERNO - {valor}')

        # # # MERCADO EXTERNO # # #
        padrao = r"Regime de Competência\s*([\d.,]+)"
        resultado = re.search(padrao, texto)
        valor = resultado.group(1)
        print(f'MERCADO EXTERNO - {valor}')
    '''