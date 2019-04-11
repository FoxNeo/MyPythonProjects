# Fechas y hora

from datetime import datetime

fechayhora = datetime.now()
print(fechayhora)

# year
year = fechayhora.year
month = fechayhora.month
day = fechayhora.day

# time
hour = fechayhora.hour
minute = fechayhora.minute
second = fechayhora.second
microsecond = fechayhora.microsecond

print("La hora es {}:{}:{}".format(hour, minute, second))