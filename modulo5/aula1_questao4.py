from datetime import date
data_atual = date.today()
data_em_texto = "{}/{}/{}".format(data_atual.day, data_atual.month,
data_atual.year)
print(f"Data: {data_em_texto}")
from datetime import datetime, timezone
th = datetime.now()
tempo = "{}:{}".format(th.hour, th.minute)
print(f"Hora: {tempo}")