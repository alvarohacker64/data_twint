import time
t_ini = time.time()
import twint


# Cuentas de interés con sus fehcas de inicio y fin de jornada
dict_accounts = {'cb1939canarias': ['2021-05-01', '2021-05-03'], 
"valenciabasket": ['2021-05-01', '2021-05-03'], 
"BFuenlabrada": ['2021-05-01', '2021-05-03'], 
"UCAMMurcia": ['2021-05-01', '2021-05-03'], 
"unicajaCB": ['2021-04-30', '2021-05-02'],
"Baskonia": ['2021-05-10', '2021-05-12'], 
"gipuzkoabasket": ['2021-04-28', '2021-04-30'], 
"GranCanariaCB": ['2021-05-01', '2021-05-03'], 
"CB1939Canarias": ['2021-05-01', '2021-05-03'], 
"morabancandorra": ['2021-04-30', '2021-05-02'], 
"MovistarEstu": ['2021-05-01', '2021-05-03'], 
"bilbaobasket": ['2021-04-20', '2021-04-22'],
"SanPabloBurgos": ['2021-04-28', '2021-04-30'], 
"OBRADOIROCAB": ['2021-04-30', '2021-05-02'], 
"RealBetisBasket": ['2021-05-01', '2021-05-03'],
"BasquetManresa": ['2021-05-01', '2021-05-03'], 
"CasademontZGZ": ['2021-05-01', '2021-05-03'],
"Penya1930": ['2021-04-30', '2021-05-02'], 
"FCBbasket": ['2021-04-24', '2021-04-26'],
"RMBaloncesto": ['2021-05-01', '2021-05-03']}

accounts = list(dict_accounts.keys())
i = 0
while i < len(accounts):
    account = accounts[i]
    # Fechas
    SINCE = dict_accounts[account][0]
    UNTIL = dict_accounts[account][1]
    # Configuracion
    c = twint.Config()
    c.Search = '@' + account
    c.Since = SINCE
    c.Until = UNTIL
    c.Store_csv = True
    c.Output = account + '_date.csv'
    # Ejecucion
    try:
        twint.run.Search(c)
    except:
        print("Saltamos a la siguiente iteración")
    # Imprimimos
    print(f"Iteración {i+1}/{len(accounts)}: en procesar tweets de {account} ha tardado {round(abs(time.time()-t_ini), 3)} segundos")
    i+=1