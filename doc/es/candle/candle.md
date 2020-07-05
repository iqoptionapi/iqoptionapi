# Velas

## Obtener velas

Solo obtiene lass velas cerrada no en tiempo real

```
Iq.get_candles(ACTIVES,interval,count,endtime)
            #ACTIVES: Ejemplo de entrada "EURUSD" OR "EURGBP"..ñ
            #interval: Duración de las velas en Segundoss
            #count: Cuantas velas quieres obtener del pasado
            #endtime: Obtener velas del pasado hasta una fecha concreta
```

### Ejemplo

```python
from iqoptionapi.stable_api import IQ_Option
import time
Iq=IQ_Option("email","password")
Iq.connect()#conectar a iqoption
end_from_time=time.time()
ANS=[]
for i in range(70):
    data=Iq.get_candles("EURUSD", 60, 1000, end_from_time)
    ANS =data+ANS
    end_from_time=int(data[0]["from"])-1
print(ANS)
```

## Obtener las nuevas velas en tiempo real

### Ejemplo de indicador

```python

from talib.abstract import *
from iqoptionapi.stable_api import IQ_Option
import time
import numpy as np
print("login...")
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
goal="EURUSD"
size=10#size=[1,5,10,15,30,60,120,300,600,900,1800,3600,7200,14400,28800,43200,86400,604800,2592000,"all"]
timeperiod=10
maxdict=20
print("Empezar el stream...")
Iq.start_candles_stream(goal,size,maxdict)
print("Empezar ejemplo de EMA")
while True:
    candles=Iq.get_realtime_candles(goal,size)

    inputs = {
        'open': np.array([]),
        'high': np.array([]),
        'low': np.array([]),
        'close': np.array([]),
        'volume': np.array([])
    }
    for timestamp in candles:

        inputs["open"]=np.append(inputs["open"],candles[timestamp]["open"] )
        inputs["high"]=np.append(inputs["open"],candles[timestamp]["max"] )
        inputs["low"]=np.append(inputs["open"],candles[timestamp]["min"] )
        inputs["close"]=np.append(inputs["open"],candles[timestamp]["close"] )
        inputs["volume"]=np.append(inputs["open"],candles[timestamp]["volume"] )


    print("Mostrar la EMA")
    print(EMA(inputs, timeperiod=timeperiod))
    print("\n")
    time.sleep(1)
Iq.stop_candles_stream(goal,size)
```

### Ejemplo

```python
from iqoptionapi.stable_api import IQ_Option
import logging
import time
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
print("Accediendo...")
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
goal="EURUSD"
size="all"#size=[1,5,10,15,30,60,120,300,600,900,1800,3600,7200,14400,28800,43200,86400,604800,2592000,"all"]
maxdict=10
print("Empezar stream...")
Iq.start_candles_stream(goal,size,maxdict)
#DO something
print("Hacer algo...")
time.sleep(10)

print("imprimir velas")
cc=Iq.get_realtime_candles(goal,size)
for k in cc:
    print(goal,"size",k,cc[k])
print("parar velas")
Iq.stop_candles_stream(goal,size)
```

### Tamaño

![](image/time_interval.png)

### start_candles_stream()

```python
goal="EURUSD"
size="all"#size=[1,5,10,15,30,60,120,300,600,900,1800,3600,7200,14400,28800,43200,86400,604800,2592000,"all"]
maxdict=10
print("start stream...")
Iq.start_candles_stream(goal,size,maxdict)
```

### get_realtime_candles()

get_realtime_candles() despuess de llamr start_candles_stream()

```
Iq.get_realtime_candles(goal,size)
```

### stop_candles_stream()

Si no estás usando get_realtime_candles() porfavor cierra el stream

```python
Iq.stop_candles_stream(goal,size)
```