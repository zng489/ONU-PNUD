from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import time

from datetime import date
#https://www.vagas.com.br/vagas-de-vagas?p%5B%5D=Brasil&q=vagas&pagina=2&_=1620066765523
dados = []
#10
#10-30
#for i in range(1,50):
#    url = f'https://www.vagas.com.br/vagas-de-vagas?p%5B%5D=Brasil&q=vagas&pagina={i}&_={1620066765521+i}'
#    print(i)

for i in range(50,51):
    url = f'https://www.vagas.com.br/vagas-de-vagas?p%5B%5D=Brasil&q=vagas&pagina={i}&_={1620066765521+i}'
    print(i)
    
    r = requests.get(url).text  # content (would be preferred for "binary" filetypes, such as an image or PDF file)
    
    #oup_x = BeautifulSoup(r, 'lxml')
    #soup_h = BeautifulSoup(r, 'html')
    soup_h = BeautifulSoup(r, "html.parser" )
    
    for x in soup_h.findAll('a',{'class':"link-detalhes-vaga"}):
        #links = x['href']
        links = 'https://www.vagas.com.br' + x.get('href')    
        #print(links)
        
        url_0 = links

        r_0 = requests.get(url_0).text  # content (would be preferred for "binary" filetypes, such as an image or PDF file)
        soup_h_0 = BeautifulSoup(r_0, 'html')
        
        
        
        
        try:
            nome_vaga = soup_h_0.find('h1',{'class':"job-shortdescription__title"}).getText().replace('\n','')
        except:
            nome_vaga = soup_h_0.find('span',{'class':"job-hierarchylist__item job-hierarchylist__item--level"}).getText().replace('\n','')
        
        empresa = soup_h_0.find('h2',{'class':"job-shortdescription__company"}).getText().replace('\n','').replace('  ','')
        
        try:
            vagas = soup_h_0.find('span',{'class':"job-hierarchylist__item job-hierarchylist__item--quantity"}).getText().replace('\n','').replace('  ','')
        except:
            vagas = "None"
        
        
        codigo = soup_h_0.find('li',{'class':"job-breadcrumb__item job-breadcrumb__item--id"}).getText().replace('\n','').replace('  ','')
        
        descrição = soup_h_0.find('div',{'class':"job-tab-content job-description__text texto"}).getText().replace('\n','').replace('  ','').replace('Descrição','').replace(':','')
        
        data_publicada = soup_h_0.find('li',{'class':"job-breadcrumb__item job-breadcrumb__item--published job-breadcrumb__item--nostyle"}).getText().replace('\n','').replace('  ','')
        
        local = soup_h_0.find('span',{'class':"info-localizacao"}).getText().replace('\n','').replace('  ','')
        
        salario = soup_h_0.find('div',{'class':"infoVaga"}).div.getText().replace('\R$','').replace('\n','').replace('   ','')         
        
        try:
            beneficios = soup_h_0.find('ul',{'class':"job-benefits__list"}).getText().replace('\n',' ').replace('   ','')
        except:
            beneficios = "-"


        data_do_webscraping = datetime.datetime.now().strftime('%d/%m/%Y')
            
        lista = {"Nome_vaga":nome_vaga,
                 "Url":links,
                 'Dados da Empresa':empresa,
                 'código':codigo,
                 "Vagas":vagas,
                 'Descrição':descrição,
                 'Data':data_publicada,
                 'Localidade':local,
                 'Salário':salario,
                 'Benefícios':beneficios,
                 'Data do WebScraping':data_do_webscraping}
                 
                 
                 
        dados.append(lista)
    
df = pd.DataFrame(dados)
df.to_csv('Vagas2.csv')