# Forex&Stock&Commodities&Crypto&ETFs

## instrument_type y instrument_id
Tu puedes buscar instrument_type and instrument_id de este archivo

buscar [instrument_type and instrument_id](instrument.txt)

## Ejemplo

```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#conectar a iqoption
instrument_type="crypto"
instrument_id="BTCUSD"
side="buy"#Introducir:"buy"/"sell"
amount=1.23#Introducir la cantidad de dinero por operación

#"leverage"="Multiplier"
leverage=3#Puedes obtener más sinformación de get_available_leverages()

type="market"#Introducir:"market"/"limit"/"stop"

#Para type="limit"/"stop"

# olo funciona con type="limit"
limit_price=None#input:None/value(float/int)

#Solo funciona con type="stop"
stop_price=None#input:None/value(float/int)

#"percent"=Profit Percentage
#"price"=Asset Price
#"diff"=Profit in Money

stop_lose_kind="percent"#input:None/"price"/"diff"/"percent"
stop_lose_value=95#input:None/value(float/int)

take_profit_kind=None#input:None/"price"/"diff"/"percent"
take_profit_value=None#input:None/value(float/int)

#"use_trail_stop"="Trailing Stop"
use_trail_stop=True#True/False

#"auto_margin_call"="Utilizar el dinero te la cuenta para mantener Abierta la Posición"
auto_margin_call=False#True/False
#Si tu quieres "take_profit_kind"&
#            "take_profit_value"&
#            "stop_lose_kind"&
#            "stop_lose_value" all being "Not Set","auto_margin_call" need to set:True

use_token_for_commission=False#True/False

check,order_id=Iq.buy_order(instrument_type=instrument_type, instrument_id=instrument_id,
            side=side, amount=amount,leverage=leverage,
            type=type,limit_price=limit_price, stop_price=stop_price,
            stop_lose_value=stop_lose_value, stop_lose_kind=stop_lose_kind,
            take_profit_value=take_profit_value, take_profit_kind=take_profit_kind,
            use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
            use_token_for_commission=use_token_for_commission)
print(Iq.get_order(order_id))
print(Iq.get_positions("crypto"))
print(Iq.get_position_history("crypto"))
print(Iq.get_available_leverages("crypto","BTCUSD"))
print(Iq.close_position(order_id))
print(Iq.get_overnight_fee("crypto","BTCUSD"))
```

## buy_order()
devuelve (True/False,buy_order_id/False)

Si Buy es satisfactoria devuelve (True,buy_order_id)

"percent"=Profit Percentage

"price"=Asset Price

"diff"=Profit en dinero


|parameter|||||
--|--|--|--|--|
instrument_type|[instrument_type](#instrumenttypeid)
instrument_id| [instrument_id](#instrumenttypeid)
side|"buy"|"sell"
amount|value(float/int)
leverage|value(int)
type|"market"|"limit"|"stop"
limit_price|None|value(float/int):Only working by set type="limit"
stop_price|None|value(float/int):Only working by set type="stop"
stop_lose_kind|None|"price"|"diff"|"percent"
stop_lose_value|None|value(float/int)
take_profit_kind|None|"price"|"diff"|"percent"
take_profit_value|None|value(float/int)
use_trail_stop|True|False
auto_margin_call|True|False
use_token_for_commission|True|False

```python
check,order_id=Iq.buy_order(
            instrument_type=instrument_type, instrument_id=instrument_id,
            side=side, amount=amount,leverage=leverage,
            type=type,limit_price=limit_price, stop_price=stop_price,
            stop_lose_kind=stop_lose_kind,
            stop_lose_value=stop_lose_value,
            take_profit_kind=take_profit_kind,
            take_profit_value=take_profit_value,
            use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
            use_token_for_commission=use_token_for_commission)

```

## change_order()
ID_Name=""order_id" |  ID_Name="position_id"
:-------------------------:|:-------------------------:
![](image/change_ID_Name_order_id.png)  |  ![](image/change_ID_Name_position_id.png)


|parameter|||||
--|--|--|--|--|
ID_Name|"position_id"|"order_id"
order_id|"you need to get order_id from buy_order()"
stop_lose_kind|None|"price"|"diff"|"percent"
stop_lose_value|None|value(float/int)
take_profit_kind|None|"price"|"diff"|"percent"
take_profit_value|None|value(float/int)
use_trail_stop|True|False
auto_margin_call|True|False

### sample

```python
ID_Name="order_id"#"position_id"/"order_id"
stop_lose_kind=None
stop_lose_value=None
take_profit_kind="percent"
take_profit_value=200
use_trail_stop=False
auto_margin_call=True
Iq.change_order(ID_Name=ID_Name,order_id=order_id,
                stop_lose_kind=stop_lose_kind,stop_lose_value=stop_lose_value,
                take_profit_kind=take_profit_kind,take_profit_value=take_profit_value,
                use_trail_stop=use_trail_stop,auto_margin_call=auto_margin_call)
```

## get_order()

Obtener información sobre buy_order_id

devuelve (True/False,get_order,None)

```python
Iq.get_order(buy_order_id)
```

## get_pending()

Obtendrás los dato

![](image/get_pending.png)

```python
Iq.get_pending(instrument_type)
```

## get_positions()

Obtendrá los datos

![](image/get_positions.png)


devuelve (True/False,get_positions,None)

no soporte para ""turbo-option""

instrument_type="crypto","forex","fx-option","multi-option","cfd","digital-option"

```python
Iq.get_positions(instrument_type)
```

## get_position()

Obtendrás los datos

![](image/get_position.png)

Obtendráss una possición por buy_order_id

devuelve (True/False,position data,None)

```python
Iq.get_positions(buy_order_id)
```

## get_position_history
Obtendrás los datos

![](image/get_position_history.png)

### get_position_history()

devuelve (True/False,position_history,None)

```
Iq.get_position_history(instrument_type)
```

### get_position_history_v2

instrument_type="crypto","forex","fx-option","turbo-option","multi-option","cfd","digital-option"

get_position_history_v2(instrument_type,limit,offset,start,end)

```python
from iqoptionapi.stable_api import IQ_Option
import logging
import random
import time
import datetime
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("email","password")
Iq.connect()#conectar a iqoption
#instrument_type="crypto","forex","fx-option","turbo-option","multi-option","cfd","digital-option"
instrument_type="digital-option"
limit=2#Cuántos quieres obtener
offset=0#offset de tiempo final, si el tiempo final es 0,significa que se obtendrán los datos desde ahora
start=0#Empezar el tiempo en Timestamp
end=0#Timestamp
data=Iq.get_position_history_v2(instrument_type,limit,offset,start,end)

print(data)

#--------- Esto obtendrá los datos empezando por 2019/7/1(end) hasta  2019/1/1(start) y solo obteniendo 2(limit) datoss siendo el offset 0
instrument_type="digital-option"
limit=2#Cuántos quieres obtener
offset=0#offset de tiempo final, si el tiempo final es 0, significa que se obtendrán los datos desde ahora
start=int(time.mktime(datetime.datetime.strptime("2019/1/1", "%Y/%m/%d").timetuple()))
end=int(time.mktime(datetime.datetime.strptime("2019/7/1", "%Y/%m/%d").timetuple()))
data=Iq.get_position_history_v2(instrument_type,limit,offset,start,end)
print(data)
```

## get_available_leverages()

Obtener apalancamiento disponible

devuelve (True/False,available_leverages,None)

```python
Iq.get_available_leverages(instrument_type,actives)
```

## cancel_order()

Cancelarás la orden

![](image/cancel_order.png)

devuelve (True/False)

```python
Iq.cancel_order(buy_order_id)
```

## close_position()

Cancelarás la poición

![](image/close_position.png)

devuelve (True/False)

```python
Iq.close_position(buy_order_id)
```

## get_overnight_fee()

devuelve (True/False,overnight_fee,None)

```python
Iq.get_overnight_fee(instrument_type,active)
```