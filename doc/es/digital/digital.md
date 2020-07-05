# Digital


## Cerca del modo strike
![](image/near.png)
### Ejemplo

```python
from iqoptionapi.stable_api import IQ_Option
import time
import random
Iq=IQ_Option("email","password")
Iq.connect()#conectar a iqoption
ACTIVES="EURUSD"
duration=1#minuto 1 or 5
amount=1
Iq.subscribe_strike_list(ACTIVES,duration)
#get strike_list
data=Iq.get_realtime_strike_list(ACTIVES, duration)
print("get strike data")
print(data)
"""data
{'1.127100':
    {  'call':
            {   'profit': None,
                'id': 'doEURUSD201811120649PT1MC11271'
            },
        'put':
            {   'profit': 566.6666666666666,
                'id': 'doEURUSD201811120649PT1MP11271'
            }
    }............
}
"""
#Obtener la lista de precios
price_list=list(data.keys())
#Elegir una estratégia aleatoria
choose_price=price_list[random.randint(0,len(price_list)-1)]
#Obtener instrument_id
instrument_id=data[choose_price]["call"]["id"]
#Obtener profit
profit=data[choose_price]["call"]["profit"]
print("Elegir que quiere commprar")
print("precio:",choose_price,"side:call","instrument_id:",instrument_id,"profit:",profit)
#Escojer instrument_id para abrir operación
buy_check,id=Iq.buy_digital(amount,instrument_id)
polling_time=5
if buy_check:
    print("Esperar para comprobar win")
    #comprobar win
    while True:
        check_close,win_money=Iq.check_win_digital_v2(id,polling_time)
        if check_close:
            if float(win_money)>0:
                win_money=("%.2f" % (win_money))
                print("Tu has ganado",win_money,"dinero")
            else:
                print("Sin beneficioss")
            break
    Iq.unsubscribe_strike_list(ACTIVES,duration)
else:
    print("Fallo al comprar, porfavor prueba otra vez")
```

### Obtener toda la lissta de datos de todos los strike

Ejemplo
```python
from iqoptionapi.stable_api import IQ_Option
import time
Iq=IQ_Option("email","password")
Iq.connect()#conecta a iqoption
ACTIVES="EURUSD"
duration=1#minuto 1 or 5
Iq.subscribe_strike_list(ACTIVES,duration)
while True:
    data=Iq.get_realtime_strike_list(ACTIVES, duration)
    for price in data:
        print("precio",price,data[price])
    time.sleep(5)
Iq.unsubscribe_strike_list(ACTIVES,duration)
```
#### subscribe_strike_list()

```python
Iq.subscribe_strike_list(ACTIVES,duration)
```

#### get_realtime_strike_list

Tu necesitas llamar a subscribe_strike_list() antes de get_realtime_strike_list()
```python
Iq.get_realtime_strike_list(ACTIVES,duration)
```

#### unsubscribe_strike_list()
```python
Iq.unsubscribe_strike_list(ACTIVES,duration)
```
### buy_digital()

```python
buy_check,id=Iq.buy_digital(amount,instrument_id)
#obtener el instrument_id de Iq.get_realtime_strike_list
```

## Modo actual del precio

![](image/spot.png)



### buy_digital_spot
Comprar el dígito en el precio actual

Devuelve check y id

```python
from iqoptionapi.stable_api import IQ_Option

Iq=IQ_Option("email","password")
Iq.connect()#conectar a iqoption
ACTIVES="EURUSD"
duration=1#minuto 1 or 5
amount=1
action="call"#put
print(Iq.buy_digital_spot(ACTIVES,amount,action,duration))
```

### get_digital_spot_profit_after_sale()

Obtener Profit después de la Venta(P/L)

![](image/profit_after_sale.png)

Ejemplo

```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","passord")
ACTIVES="EURUSD"
duration=1#minute 1 or 5
amount=100
action="put"#put

Iq.subscribe_strike_list(ACTIVES,duration)
_,id=Iq.buy_digital_spot(ACTIVES,amount,action,duration)

while True:
    PL=Iq.get_digital_spot_profit_after_sale(id)
    if PL!=None:
        print(PL)
```

### get_digital_current_profit()

```python
from iqoptionapi.stable_api import IQ_Option
import time
import logging
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("email","password")
Iq.connect()#conectar a iqoption
ACTIVES="EURUSD"
duration=1#minuto 1 or 5
Iq.subscribe_strike_list(ACTIVES,duration)
while True:
    data=Iq.get_digital_current_profit(ACTIVES, duration)
    print(data)# La primera impresión puede ser falsa, sólo espera un segundo puedes obtener el beneficio
    time.sleep(1)
Iq.unsubscribe_strike_list(ACTIVES,duration)
```

## check win for digital

### check_win_digital()

Esta api esta implementada por get_digital_position()

Esta función esta encuestando, necesitas escojet el tiempo de encuesta

```python
Iq.check_win_digital(id,polling_time)#obtener el id de Iq.buy_digital
```
### check_win_digital_v2()

Esta api es asíncrona, obtiene el id de los datos. Solo puede obtener el id de los datos antess de que puedass comprar la opción.
Si reinicias el programa, no se puede obtener otra vez la id de los datos de manera asíncrona otra vez.
De esta forma no se puede trabajar con check_win_digital_v2, asi tu necesitas usar check_win_digital.

```python
 Iq.check_win_digital_v2(id)#obtener el id deIq.buy_digital
#return:check_close,win_money
#return sample
#if you loose:Ture,o
#if you win:True,1232.3
#if trade not clode yet:False,None
```

Ejemplo de código

```python
from iqoptionapi.stable_api import IQ_Option
import logging
import random
import time
import datetime
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
ACTIVES="EURUSD"
duration=1#minuto 1 or 5
amount=1
action="call"#put
_,id=(Iq.buy_digital_spot(ACTIVES,amount,action,duration))
print(id)
if id !="error":
    while True:
        check,win=Iq.check_win_digital_v2(id)
        if check==True:
            break
    if win<0:
        print("Has perdido "+str(win)+"$")
    else:
        print("Has ganado "+str(win)+"$")
else:
    print("Porfavor prueba otra vez")
```

## close_digital_option()

```python
Iq.close_digital_option(id)
```

## Obtener datos de opciones digitaless

Ejemplo 1
```python
from iqoptionapi.stable_api import IQ_Option
import logging
import time
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("email","password")
Iq.connect()#conectar a iqoption
ACTIVES="EURUSD-OTC"
duration=1#minuto 1 or 5
amount=1
action="call"#put
from datetime import datetime

_,id=Iq.buy_digital_spot(ACTIVES,amount,action,duration)

while True:
    check,_=Iq.check_win_digital(id)
    if check:
        break
print(Iq.get_digital_position(id))
print(Iq.check_win_digital(id))
```

Ejemplo 2

```python
print(Iq.get_positions("digital-option"))
print(Iq.get_digital_position(2323433))#Comprobar por id
print(Iq.get_position_history("digital-option"))
```