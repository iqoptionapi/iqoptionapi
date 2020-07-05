#For Binary Option


## buy

buy the binary option

### buy()

sample

```python
from iqoptionapi.stable_api import IQ_Option
import logging
import time
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("email","pass")
goal="EURUSD"
print("get candles")
print(Iq.get_candles(goal,60,111,time.time()))
Money=1
ACTIVES="EURUSD"
ACTION="call"#or "put"
expirations_mode=1

check,id=Iq.buy(Money,ACTIVES,ACTION,expirations_mode)
if check:
    print("!buy!")
else:
    print("buy fail")
```

```python
Iq.buy(Money,ACTIVES,ACTION,expirations)
                #Money:How many you want to buy type(int)
                #ACTIVES:sample input "EURUSD" OR "EURGBP".... you can view by get_all_ACTIVES_OPCODE
                #ACTION:"call"/"put" type(str)
                #expirations:input minute,careful too large will false to buy(Closed market time)thank Darth-Carrotpie's code (int)https://github.com/Lu-Yi-Hsun/iqoptionapi/issues/6
                #return:if sucess return (True,id_number) esle return(Fale,None)
```
### buy_multi()

```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
Money=[]
ACTIVES=[]
ACTION=[]
expirations_mode=[]

Money.append(1)
ACTIVES.append("EURUSD")
ACTION.append("call")#put
expirations_mode.append(1)

Money.append(1)
ACTIVES.append("EURAUD")
ACTION.append("call")#put
expirations_mode.append(1)

print("buy multi")
id_list=Iq.buy_multi(Money,ACTIVES,ACTION,expirations_mode)

print("check win only one id (id_list[0])")
print(Iq.check_win_v2(id_list[0],2))
```
### buy_by_raw_expirations()

buy the binary optoin by expired

```python
price=2
active="EURUSD"
direction="call"#put
option="turbo"#binary
expired=1293923# this expried time you need to count or get by your self
Iq.buy_by_raw_expirations(price, active, direction, option,expired)
```

## get_remaning()

purchase time=remaning time - 30
```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
Money=1
ACTIVES="EURUSD"
ACTION="call"#or "put"
expirations_mode=1
while True:
    remaning_time=Iq.get_remaning(expirations_mode)
    purchase_time=remaning_time-30
    if purchase_time<4:#buy the binary option at purchase_time<4
        Iq.buy(Money,ACTIVES,ACTION,expirations_mode)
        break
```

## sell_option()

```python
Iq.sell_option(sell_all)#input int or list order id
```
Sample

```python
from iqoptionapi.stable_api import IQ_Option
import time
print("login...")
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
Money=1
ACTIVES="EURUSD"
ACTION="call"#or "put"
expirations_mode=1

id=Iq.buy(Money,ACTIVES,ACTION,expirations_mode)
id2=Iq.buy(Money,ACTIVES,ACTION,expirations_mode)

time.sleep(5)
sell_all=[]
sell_all.append(id)
sell_all.append(id2)
print(Iq.sell_option(sell_all))
```

## check win

It will do loop until get win or loose

### check_win()

```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
check,id = Iq.buy(1, "EURUSD", "call", 1)
print("start check win please wait")
print(Iq.check_win(id))
```

```python
Iq.check_win(23243221)
#""you need to get id_number from buy function""
#Iq.check_win(id_number)
#this function will do loop check your bet until if win/equal/loose
```

### check_win_v2()

```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
check,id = Iq.buy(1, "EURUSD", "call", 1)
print("start check win please wait")
polling_time=3
print(Iq.check_win_v2(id,polling_time))
```

### check_win_v3()

great way

```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
check,id = Iq.buy(1, "EURUSD", "call", 1)
print("start check win please wait")
print(Iq.check_win_v3(id))
```

## get_binary_option_detail()
![](expiration_time.png)

sample
```python
from iqoptionapi.stable_api import IQ_Option
print("login...")
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
d=Iq.get_binary_option_detail()
print(d["CADCHF"]["turbo"])
print(d["CADCHF"]["binary"])
```
## get_all_init()

get_binary_option_detail is base on this api

you will get the raw detail about binary option
```
Iq.get_all_init()
```

## get_all_profit()

sample

```python
from iqoptionapi.stable_api import IQ_Option
print("login...")
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
d=Iq.get_all_profit()
print(d["CADCHF"]["turbo"])
print(d["CADCHF"]["binary"])
```

if you want realtime profit try this
[get real time profit](/all/#get_commission_change)

## get_betinfo()

if order not close yet or wrong id it will return False
```python
isSuccessful,dict=Iq.get_betinfo(4452272449)
#Iq.get_betinfo
#INPUT: order id
#OUTPUT:isSuccessful,dict
```
## get_optioninfo

### get_optioninfo()

input how many data you want to get from Trading History(only for binary option)
```python
print(Iq.get_optioninfo(10))
```

### get_optioninfo_v2()

input how many data you want to get from Trading History(only for binary option)
```python
print(Iq.get_optioninfo_v2(10))
```
### get_option_open_by_other_pc()

if your account is login in other plance/PC and doing buy option

you can get the option by this function

```python
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
while True:
    #please open website iqoption and buy some binary option
    if Iq.get_option_open_by_other_pc()!={}:
        break
    time.sleep(1)
print("Get option from other Pc and same account")
print(Iq.get_option_open_by_other_pc())

id=list(Iq.get_option_open_by_other_pc().keys())[0]
Iq.del_option_open_by_other_pc(id)
print("After del by id")
print(Iq.get_option_open_by_other_pc())
```

## Get mood

### sample

```python
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
goal="EURUSD"
Iq.start_mood_stream(goal)
print(Iq.get_traders_mood(goal))
Iq.stop_mood_stream(goal)
```

### start_mood_stream()

```python
Iq.start_mood_stream(goal)
```

### get_traders_mood()

call get_traders_mood() after start_mood_stream

```python
Iq.get_traders_mood(goal)
```

### get_all_traders_mood()

it will get all trade mood what you start stream

```python
Iq.get_all_traders_mood()
#output:(dict) all mood you start
```

### stop_mood_stream()

if you not using the mood ,please stop safe network

```python
Iq.stop_mood_stream(goal)
```

