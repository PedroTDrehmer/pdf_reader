import PyPDF2
import re

caminho_pdf = "Simples Nacional_1476_122024.pdf"

def extrair_valor_regime_competencia(caminho_pdf):
    with open(caminho_pdf, "rb") as file:
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

extrair_valor_regime_competencia(caminho_pdf)
