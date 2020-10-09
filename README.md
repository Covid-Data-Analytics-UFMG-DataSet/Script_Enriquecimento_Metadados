# Script_Enriquecimento_Metadados
O script de enriquecimento estrutura os metadados de diversos arquivos, contendo variadas informações sobre os impactos da COVID-19 nas áreas da saúde
e também socioeconomica do Brasil, coletados e mapeados de forma interdisciplinar pela Universidade Federal de Minas Gerais (UFMG).

# Objetivo
O objetivo do script é gerar um arquivo em formato XML, seguindo o padrão das normativas ODS, que servirá como base para a estrutura de um banco de dados.

# Estrutura do script e da árvore XML

### Linguagem e bibliotecas
O script foi desenvolvido na linguagem python utilizando as bibliotecas pandas e xml.
A biblioteca pandas foi utilizada para ler os metadados, que são fornecidos através de uma tabela em formato excel(.xlsx), e armazená-los em um dataframe 
para facilitar o acesso a esses dados. O módulo xml.etree.ElementTree foi utilizado para criar, alimentar e gerar o arquivo 'metadados.xml'.

### Árvore XML
A estrutura da árvore

![Arvore_2](https://user-images.githubusercontent.com/69644988/95624441-44ebdd80-0a4d-11eb-8f67-44ddff6fd3bc.PNG)

A raíz da árvore foi nomeada como "Arquivos" e os filhos dela serão os arquivos, identificados por uma ID sequencial, cujos filhos são todos os metadados
coletados sobre aquele arquivo.

Uma versao da árvore alimentada com alguns metadados coletados pode ser encontrada no repositório Script_Enriquecimento_Metadados/script_XML_metadados, no 
arquivo 'metadados.xml'.

# Metodologia
No arquivo excel de entrada foi anexada uma planilha contendo uma tabela contendo: uma coluna listando os nós (de 1 ao número total de nós) de acordo com
a ordem dos mesmos na árvore XML, uma coluna com os nomes dos nós e uma coluna contendo uma descrição dos nós (que será informada no campo "name" das tags
do xml). Essa tabela é acessada primeiro pelo script e utilizada para modelar a árvore para poder então acessar a tabela com os metadados e alimentá-los à 
árvore. Dessa forma, caso seja necessária uma alteração no modelo de dados, o script já seria capaz de tratá-las sem necessidade de modificações. 

### Colaboradores
* Product Owner: Ramon Salinas
* Scrum Master: Pedro Victor
* Time de Desenvolvimento: Gabriel Nunes, Alan Prado, Luvison Leal, Rodrigo Machado e Turi Vasconcelos
