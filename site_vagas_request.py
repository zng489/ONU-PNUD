import sys
import pandas as pd
import numpy as np
import requests
import time
import urllib3
import itertools
import time
from bs4 import BeautifulSoup
from requests.api import head

from datetime import date, timedelta
from random import randint
from time import sleep

sleep(randint(0,10))


def t0():

    start_time = time.time()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    
    
    df = pd.read_csv('df_sitevagas_t0_alin.csv',index_col=0)
    df = df[df['3_situacao da vaga'] == 200]
    df_c = df['codigo'].tolist()
    df_u = df['url'].tolist()
    df_data_do_scraping = pd.to_datetime(df['data do scraping'])

    connected = []
    error = []

    for (i,q,z) in zip(df_u,df_c,df_data_do_scraping):
        #proxies = {'https': "socks5h://127.0.0.1:1080"}
        # #r = requests.get(i,proxies=proxies)
        #r = requests.get(i, timeout=600)  
        #proxies = {"http":'http://165.22.64.68:40402',"http":'http://43.224.10.42:6666'}
        #r = requests.get(i, proxies=proxies)

        r = requests.get(i, allow_redirects=False, headers=headers, timeout=200,verify=False).text
        req = requests.get(i,allow_redirects=False,verify=False)
        soup = BeautifulSoup(r, 'lxml')
        #if r.status_code == 200:

        
        try:
            if soup.find_all('div',{'class':'job-expired__text'}) == [] and soup.find_all('h2',{'class':'tit-nao-encontrado titulo'}) == []: #or req.status_code == 200:
                print(req.status_code)
                print(i,q,"A vaga permanece (Connected)")
                urls = i
                cods = q
                situacao = "200"
                df_data_scrap = z
                df_data_do_request = pd.to_datetime(date.today())
                dif_data = (df_data_do_request - df_data_scrap)

                dados = {'urls':urls,'cods':cods,'situacao_da_vaga':situacao,'dif_data':dif_data,'data_do_request':df_data_do_request}
                print(len(urls))
                connected.append(dados)
                df_0 = pd.DataFrame(connected)
                print(df_0.count())
                df_0.to_csv('vagas_nao_excluidas.csv')
                sleep(randint(0,10))

    #    http = urllib3.PoolManager()
    #    r = http.request('GET',i,retries=urllib3.Retry(redirect=2, raise_on_redirect=False))
#
    #    if r.status == 200:
    #        time.sleep(2)
    #        print(i,q,"Connected")
    #        urls = i
    #        cods = q
    #        dados = {'urls':urls,'cods':cods}
    #        connected.append(dados)
    #        df_0 = pd.DataFrame(connected)
    #        print(df_0.count())
    #        df_0.to_csv('connected.csv')

            else:

                print(i,q,'Não há mais essa vaga (Error)')

                urls = i
                cods = q
                situacao = "200"
                df_data_scrap = z
                df_data_do_request = pd.to_datetime(date.today())
                dif_data = (df_data_do_request - df_data_scrap)

                dados = {'urls':urls,'cods':cods,'situacao_da_vaga':situacao,'dif_data':dif_data,'data_do_request':df_data_do_request}

                print(len(urls))
                error.append(dados)
                df_1 = pd.DataFrame(error)
                df_1.to_csv('vagas_excluidas.csv')
                sleep(randint(0,10))


                #time.sleep(2)

        except:
            print(sys.exc_info())

    print("--- %s seconds ---" % (time.time() - start_time))       
    return print(error)

if __name__ == '__main__':
    t0()