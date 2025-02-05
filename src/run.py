import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.factory.from_excel import excel_reader
from src.factory.from_pdf import pdf_reader


def main():
    excel_reader()
    pdf_reader()

if __name__ == "__main__":
    main()
