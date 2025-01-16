import PyPDF2
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.utils.env import PATH_ARQUIVO

def tudo():
    with open(PATH_ARQUIVO, "rb") as file:
        leitor_pdf = PyPDF2.PdfReader(file)
        
        for pagina in leitor_pdf.pages:
            texto = pagina.extract_text()
            # print(texto)
            
            print('- - - - - - - - - - - - - - - - - - - - - - - -')

            # # # NOME # # #
            padrao = r"\d{2}/\d{2}/\d{4}\s*(.*?)\s*CNPJ"
            resultado = re.search(padrao, texto)
            valor = resultado.group(1)
            print(valor)


            # # # VALOR # # #
            padrao = r"Receita Bruta do período de Apuração \(RPA\)[^\d]*(\d[\d.,]*)"
            resultado = re.search(padrao, texto)
            valor = resultado.group(1)
            print(valor)


            # # # CNPJ # # #
            padrao = r"CNPJ:\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})"
            resultado = re.search(padrao, texto)
            valor = resultado.group(1)
            print(valor)


            # # # FATOR R # # #
            padrao = r'Fator r:\s*(\d+,\d{2})'
            resultado = re.search(padrao, texto)
            valor = resultado.group(1)
            print(valor)


            # # # MERCADO EXTERNO # # #
            padrao = r'Mercado Externo\s*([\d.,]+)'
            resultado = re.search(padrao, texto)
            valor = resultado.group(1)
            print(valor)


            # # # MERCADO INTERNO # # #
            padrao = r'Mercado Interno\s*([\d.,]+)'
            resultado = re.search(padrao, texto)
            valor = resultado.group(1)
            print(valor)


            padrao = r"SIMPLES NACIONAL"
            resultado_simples_nacional = re.search(padrao, texto)
            if resultado_simples_nacional:
                print("SIMPLES NACIONAL encontrado.")
            else:
                print("SIMPLES NACIONAL não encontrado.")

tudo()
