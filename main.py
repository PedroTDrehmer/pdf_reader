import PyPDF2
import re

caminho_pdf = "Simples Nacional_1476_122024.pdf"

def extrair_valor_regime_competencia(caminho_pdf):
    with open(caminho_pdf, "rb") as file:
        leitor_pdf = PyPDF2.PdfReader(file)
        
        for pagina in leitor_pdf.pages:
            texto = pagina.extract_text()
            print(texto)
            
            ## VALOR
            indice = texto.find("Receita Bruta do período de Apuração (RPA)")
            trecho = texto[indice:]  # Pega o texto a partir da frase encontrada
            padrao = r"Receita Bruta do período de Apuração \(RPA\)[^\d]*(\d[\d.,]*)"
            resultado = re.search(padrao, trecho)
            valor = resultado.group(1)
            print(valor)


            ## NOME
            indice = texto.find("CNPJ")
            trecho = texto[indice:]  # Pega o texto a partir da frase encontrada
            padrao = r"CNPJ:\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})"
            resultado = re.search(padrao, trecho)
            valor = resultado.group(1)
            # print(valor)
    

            ## CNPJ
            indice = texto.find("CNPJ")
            trecho = texto[indice:]  # Pega o texto a partir da frase encontrada
            padrao = r"CNPJ:\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})"
            resultado = re.search(padrao, trecho)
            valor = resultado.group(1)
            print(valor)



    

extrair_valor_regime_competencia(caminho_pdf)
