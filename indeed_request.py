import pandas as pd
import numpy as np
import requests
import time
from datetime import date, timedelta


def indeed_t0_v2():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

    df = pd.read_csv('df_Indeed_t0_alin.csv',index_col=0)
    df = df[df['3_situacao da vaga'] == 200]
    df_c = df['codigo'].tolist()
    df_u = df['url'].tolist()
    df_data_do_scraping = pd.to_datetime(df['data do scraping'])

    connected = []
    error = []

    for (i,q,z) in zip(df_u,df_c,df_data_do_scraping):
        #proxies = {'https': \"socks5h://127.0.0.1:1080\"}
        # #r = requests.get(i,proxies=proxies)
        r = requests.get(i,allow_redirects=False, headers=headers)
        time.sleep(2)
        if r.status_code == 200:

            time.sleep(2)
            print(i,q,"Connected")
            urls = i
            cods = q
            data_do_scraping = z

            situacao = "200"
            df_data_scrap = z
            df_data_do_request = pd.to_datetime(date.today())
            dif_data = (df_data_do_request - df_data_scrap)
            dados = {'urls':urls,'cods':cods,'situacao_da_vaga':situacao,'dif_data':dif_data,'data_do_request':df_data_do_request,'data do scraping':data_do_scraping}
                


            connected.append(dados)
            df_0 = pd.DataFrame(connected)
            print(df_0.count())
            df_0.to_csv('infojobs_nao_excluidas4.csv')
        else:
            time.sleep(2)
            print(i,q,'Error 404')

            urls = i
            cods = q
            situacao = "200"
            df_data_scrap = z
            df_data_do_request = pd.to_datetime(date.today())
            dif_data = (df_data_do_request - df_data_scrap)

            dados = {'urls':urls,'cods':cods,'situacao_da_vaga':situacao,'dif_data':dif_data,'data_do_request':df_data_do_request}


            error.append(dados)
            df_1 = pd.DataFrame(error)
            df_1.to_csv('infojobs_excluidas4.csv')
            time.sleep(2)

    return print(error)

if __name__ == '__main__':
    indeed_t0_v2()