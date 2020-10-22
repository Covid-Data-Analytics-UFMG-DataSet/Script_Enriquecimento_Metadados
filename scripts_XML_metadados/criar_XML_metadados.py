import xml.etree.ElementTree as xml
import pandas as pd

def generate_xml(tabela_excel):

    df = pd.ExcelFile(tabela_excel)
    list_sheets = df.sheet_names
    meta = pd.read_excel(df, list_sheets[0])
    header = pd.read_excel(df, list_sheets[1])

    root = xml.Element('Arquivos')
    i = 0
    for row in meta.iterrows():
        i += 1
        arquivo = xml.SubElement(root, "ID_Arquivo", name=str(i))

        row[1].loc['Nome do arquivo'] = str(row[1].loc['Nome do arquivo']).capitalize()
        if(str(row[1].loc['Nome do arquivo']).find("brasil") != -1):
            row[1].loc['Nome do arquivo'] = str(row[1].loc['Nome do arquivo']).replace("brasil", "Brasil")

        for col in header.iterrows():
            nome_XML = col[1].loc['Nome XML']
            nome_original = str(col[1].loc['Nome original'])
            xml.SubElement(arquivo, nome_XML, name=nome_original).text = str(row[1].loc[nome_original])


    tree = xml.ElementTree(root)

    with open("metadados.xml", "wb") as file:
        tree.write(file)
