import time
t_ini = time.time()
import twint

# Límite de filas por cuenta
LIMIT = 2000
# Cuentas de interés
accounts = ['cb1939canarias', "valenciabasket", "BFuenlabrada", "UCAMMurcia", "unicajaCB",
"Baskonia", "gipuzkoabasket", "GranCanariaCB", "morabancandorra", "MovistarEstu", "bilbaobasket",
"SanPabloBurgos", "OBRADOIROCAB", "RealBetisBasket", "BasquetManresa", "CasademontZGZ", "Penya1930", "FCBbasket",
"RMBaloncesto"]

# account = "cb1939canarias"
i = 0
while i < len(accounts):
    account = accounts[i]
    # Configuracion
    c = twint.Config()
    c.Search = '@' + account
    c.Limit = LIMIT
    c.Store_csv = True
    c.Output = account + '.csv'
    # Ejecucion
    try:
        twint.run.Search(c)
    except:
        print("Saltamos a la siguiente iteración")
    # Imprimimos
    print(f"Iteración {i+1}/{len(accounts)}: en procesar {LIMIT} tweets de {account} ha tardado {round(abs(time.time()-t_ini), 3)} segundos")
    i+=1