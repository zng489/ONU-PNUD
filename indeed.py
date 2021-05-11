import datetime
import lxml.html as parser
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
import json
import pandas as pd
from time import sleep
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browse
from datetime import date

def indeed():
    
    Indeed_dados = []
    #990
    for i in range(0, 20, 10):
        print(i)
        url_indeed = "https://br.indeed.com/jobs?q=&l=Brasil&sort=date&filter=0&start={numero_da_pagina}".format(numero_da_pagina = i) 
        req = requests.get(url_indeed).text
        soup = BeautifulSoup(req, 'lxml')
        #print(url_indeed)
        
        try:
            results = soup.find_all('div',{'class':'jobsearch-SerpJobCard unifiedRow row result'})
            for item in results:
                url = 'https://br.indeed.com' + item.find('a').get('href')
                print(url)

                try:
                    codigo_por_url = item.find('a').get('href')
                except:
                    codigo_por_url = '-'
        
        
                try: 
                    job = item.find('h2',{'class':'title'}).text.replace('   ','')
                except:
                    job = "-"
    
    
                try:
                    company = item.find('span',{'class':'company'}).text or item.find('a',{'data-tn-element':'companyName'}).text
                except:
                    company = '-'
    
    
    
    
                try:
                    local = item.find('span',{'class':'location accessible-contrast-color-location'}).text
                except:
                    local = item.find('div',{'class':'location accessible-contrast-color-location'}).text
            
            
            
                data_publicada = item.find('span',{'class':'date date-a11y'}).text
        
        
                #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                chromedriver = 'C:/Users/Yuan/Desktop/Indeed/chromedriver_win32/chromedriver'

                #driver = webdriver.Chrome(chromedriver)
                driver = webdriver.Chrome(chromedriver,options=option)
                driver.get(url)
                time.sleep(2)
        
        
                 #Single Page
        
 
                try:
                    salario = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/div[1]/div[3]/div[2]/span").text.replace('R$', ' ')
            
                except:
                    salario = 'a combinar'
        
                try:
                    regime = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div/div/div[3]').text.replace('\n', ' ')
                except:
                    regime = '-'
    
                #try:
                    #vcodigo = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/div[1]/div[5]/div[3]/text()[4]').text.replace('\n', ' ')
                #except:
                    #vcodigo = '-'
          
                try:
                    conteudo = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/div[1]/div[5]/div[3]').text.replace('\n', ' ')
                except:
                    conteudo = '-'
          
            
                data_do_webscraping = date.today()
        
                numero_de_vagas = '-'
        
                dados = {'Url':url,
                 'Codigo criado':codigo_por_url,
                 'Empresa':company.replace('\n', ' '),
                 'Nome Vaga':job.replace('\n',''),
                'Localidade':local,
                'Data publicada':data_publicada,
                'salario':salario,
                'Regime':regime,
                #'vcodigo':vcodigo,
                'Data do WebScraping':data_do_webscraping,
                'Vagas':numero_de_vagas,
                'Conteúdo/Benefícios/Exigências':conteudo}   

                Indeed_dados.append(dados)  

                df = pd.DataFrame(Indeed_dados)
                df.to_csv('indeed.csv',index=False)

        
        except:
            df = pd.DataFrame(Indeed_dados)
            df.to_csv('Problem.csv',index=False)

    return

if __name__ == '__main__':
    indeed()
    time.sleep(2)
        
        
#df = pd.DataFrame(Indeed_dados)
#df.to_csv('indeed_8.csv', index=False)