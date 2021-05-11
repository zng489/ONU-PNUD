from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import time
from datetime import date
import csv  
from random import randint
from time import sleep

def site_vagas():
    
    #sleep(randint(1,2))
    dados = []
    for i in range(50,70):
        url = f'https://www.vagas.com.br/vagas-de-vagas?p%5B%5D=Brasil&q=vagas&pagina={i}&_={1620066765521+i}'
        r = requests.get(url).text 
        soup_h = BeautifulSoup(r, "html.parser" )
        print(i)
        
        
        
        
        try:
            for x in soup_h.findAll('a',{'class':"link-detalhes-vaga"}):
                links = 'https://www.vagas.com.br' + x.get('href')    
    
            
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
                
                lista = {"nome vaga":nome_vaga,
                     "url":links,
                     'dados da empresa':empresa,
                     'código':codigo,
                     "vagas":vagas,
                     'descrição':descrição,
                     'data':data_publicada,
                     'localidade':local,
                     'salário':salario,
                     'benefícios':beneficios,
                     'data do scraping':data_do_webscraping}
                #print(lista)

                dados.append(lista)

                #print(dados)
                df = pd.DataFrame(dados)
                df.to_csv('delete.csv', index=False)
                #print(df)
                
                
    
    #print(df)

        except:
            df = pd.DataFrame(dados)
            df.to_csv('testing2.csv',index=False)
            
  
        
    return 
   

# This tells your code to run the function search4vowels():
if __name__ == '__main__':
    site_vagas()
    sleep(randint(1,10))
    #print(search4vowels('your word'))

                
#def arrumando():
#    df = pd.read_csv('testing.csv')
#    
#    #ordering columns, i don`t think that is necessary  
#    #df[['url', 'código','nome vaga','sálario','vagas', 'localidade','data', 'conteúdo',
#    #  'denefícios','dados da empresa','data do scraping']]
#    
#    df_vagas_de_estagios = df[df['nome vaga'].str.contains('Estágio')==True]
#    df_vagas_de_estagios.to_csv('site_vagas_vagas_de_estagios.csv')
#    
#    df_vagas_limpas = df[df['nome vaga'].str.contains('Estágio')==False]
#    df_vagas_limpas = df_vagas_limpas.stack()
#    df_vagas_limpas = df_vagas_limpas.reset_index()
#    df_vagas_limpas.to_csv('df_vagas_limpassssssssssssss.csv')
#    return