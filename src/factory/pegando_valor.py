import PyPDF2
import re
from src.utils.env import PATH_ARQUIVO


def valor():
    with open(PATH_ARQUIVO, "rb") as file:
        leitor_pdf = PyPDF2.PdfReader(file)
        
        for pagina in leitor_pdf.pages:
            texto = pagina.extract_text()
            
            if "Receita Bruta do período de Apuração (RPA)" in texto:
                indice = texto.find("Receita Bruta do período de Apuração (RPA)")
                trecho = texto[indice:]  # Pega o texto a partir da frase encontrada
                
                # Usar regex para encontrar o número no trecho
                padrao = r"Receita Bruta do período de Apuração \(RPA\)[^\d]*(\d[\d.,]*)"
                resultado = re.search(padrao, trecho)
                
                if resultado:
                    valor = resultado.group(1)
                    print(valor)
                    return valor
                else:
                    print("Número não encontrado após 'Receita Bruta do período de Apuração (RPA)'.")
                    return None
            else:
                print("Frase 'Receita Bruta do período de Apuração (RPA)' não encontrada.")
                return None

