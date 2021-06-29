import time
t_ini = time.time()
import twint


# Cuentas de interés con sus fehcas de inicio y fin de jornada
dict_accounts = {
"OBRADOIROCAB_aux_0205": ['2021-05-01', '2021-05-02'],
"BFuenlabrada": ['2021-04-03', '2021-04-04'], 
"OBRADOIROCAB": ['2021-04-03', '2021-04-04'],
"bilbaobasket": ['2021-04-03', '2021-04-04'],
"BasquetManresa": ['2021-04-03', '2021-04-04'], 
"RealBetisBasket": ['2021-04-03', '2021-04-04'],
"CB1939Canarias": ['2021-04-03', '2021-04-04'],
"GranCanariaCB": ['2021-04-03', '2021-04-04'],
"CasademontZGZ": ['2021-04-03', '2021-04-04'],
"MovistarEstu": ['2021-04-04', '2021-04-05'], 
"UCAMMurcia": ['2021-04-04', '2021-04-05'],
"morabancandorra": ['2021-04-04', '2021-04-05'],
"Baskonia": ['2021-04-04', '2021-04-05'],
"valenciabasket": ['2021-04-04', '2021-04-05'], 
"Penya1930": ['2021-04-04', '2021-04-05'],
"SanPabloBurgos": ['2021-04-04', '2021-04-05'], 
"FCBbasket": ['2021-04-04', '2021-04-05'], 
"gipuzkoabasket": ['2021-04-04', '2021-04-05'], 
"RMBaloncesto": ['2021-04-04', '2021-04-05']}

accounts = list(dict_accounts.keys())
i = 0
while i < len(accounts):
    account = accounts[i]
    if "_aux_" in account:
        account_tmp = account.split("_aux_")[0]
    else:
        account_tmp = account
    # Fechas
    SINCE = dict_accounts[account][0]
    UNTIL = dict_accounts[account][1]
    # Configuracion
    c = twint.Config()
    c.Search = '@' + account_tmp
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