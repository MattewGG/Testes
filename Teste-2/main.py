import os
import pdfplumber
import pandas as pd
import zipfile
import re
from tqdm import tqdm

def clean_text(text):

    if not text:
        return ""
    return re.sub(r'\s+', ' ', str(text)).strip()

def extract_and_transform_pdf(pdf_path, output_zip, seu_nome):
    print("Iniciando extração e transformação dos dados...")
    
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

    legend_map = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }
    
    all_data = []
    columns = None
    required_columns = [
        "PROCEDIMENTO", "RN (ALTERAÇÃO)", "VIGÊNCIA", "OD", "AMB", "HCO", 
        "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
    ]
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in tqdm(pdf.pages, desc="Processando páginas"):
            try:
                tables = page.extract_tables()
                
                for table in tables:
                    if not table or len(table) < 2:
                        continue
                    
                    for row in table:
                        cleaned_row = [clean_text(cell) for cell in row]
                        
                        if all(cell == '' for cell in cleaned_row):
                            continue
                        
                        if columns is None and any(col in cleaned_row for col in required_columns):
                            columns = cleaned_row
                            columns = [col.upper().strip() for col in columns]
                            continue
                        
                        if columns:
                            if len(cleaned_row) < len(columns):
                                cleaned_row += [''] * (len(columns) - len(cleaned_row))
                            elif len(cleaned_row) > len(columns):
                                cleaned_row = cleaned_row[:len(columns)]
                            all_data.append(cleaned_row)
            
            except Exception as e:
                print(f"\nErro na página {page.page_number}: {str(e)}")
                continue
    
    if all_data:
        df = pd.DataFrame(all_data, columns=columns if columns else ['Coluna_' + str(i) for i in range(len(all_data[0]))])
        
        df.columns = [col.upper().strip() for col in df.columns]
        
        for col in required_columns:
            if col not in df.columns:
                df[col] = ''
        
        df = df[required_columns]
        
  
        for col in ['OD', 'AMB']:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: legend_map.get(str(x).strip().upper(), x))
        

        temp_csv = f"Teste_{seu_nome}.csv"
        df.to_csv(temp_csv, index=False, encoding='utf-8-sig', sep=';')
        

        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(temp_csv)
        os.remove(temp_csv)
        
        print(f"\nProcesso concluído com sucesso!")
        print(f"Arquivo ZIP gerado: {output_zip}")
        print(f"Total de registros extraídos: {len(df)}")
        print(f"Estrutura do DataFrame: {df.shape[0]} linhas x {df.shape[1]} colunas")
        
        print("\nAmostra dos dados extraídos:")
        print(df.head(10))
    else:
        print("\nNenhum dado estruturado foi encontrado no PDF.")

pdf_path = "Anexo\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
seu_nome = "extracted_data"  
output_zip = f"Test_{seu_nome}.zip"

try:
    extract_and_transform_pdf(pdf_path, output_zip, seu_nome)
except Exception as e:
    print(f"\nError: {str(e)}")