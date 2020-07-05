# Get start

## Install iqoptionapi

You can download the source code and run this

```
python setup.py install
```
or  install using (you need [git installed](https://git-scm.com/downloads)):
```
pip install -U git+git://github.com/iqoptionapi/iqoptionapi.git
```

## little sample

```python
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("email","password")
Iq.connect()#connect to iqoption
goal="EURUSD"
print("get candles")
print(Iq.get_candles(goal,60,111,time.time()))
```

## Import

```python
from iqoptionapi.stable_api import IQ_Option
```

## Login

Iq.connect() will return (check,reason)

if connect sucess return True,None

if connect fail return False,reason

```python
from iqoptionapi.stable_api import IQ_Option
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("email","password")
check, reason=Iq.connect()#connect to iqoption
print(check, reason)
```

## Debug mode on

```python
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
```

## Connect&Check connect

some time connect will close so this way can check connect and reconnect

try close your network and restart network in this sample

```python
from iqoptionapi.stable_api import IQ_Option
error_password="""{"code":"invalid_credentials","message":"You entered the wrong credentials. Please check that the login/password is correct."}"""
iqoption = IQ_Option("email", "password")
check,reason=iqoption.connect()
if check:
    print("Start your robot")
    #if see this you can close network for test
    while True:
        if iqoption.check_connect()==False:#detect the websocket is close
            print("try reconnect")
            check,reason=iqoption.connect()
            if check:
                print("Reconnect successfully")
            else:
                if reason==error_password:
                    print("Error Password")
                else:
                    print("No Network")

else:

    if reason=="[Errno -2] Name or service not known":
        print("No Network")
    elif reason==error_password:
        print("Error Password")
```

## set_session

Default User-Agent is "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

```python
from iqoptionapi.stable_api import IQ_Option
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

Iq=IQ_Option("email","password")

#Default is "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

header={"User-Agent":r"Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}
cookie={"Iq":"GOOD"}

Iq.set_session(header,cookie)

Iq.connect()#connect to iqoption
```

## Check version

```python
from iqoptionapi.stable_api import IQ_Option
print(IQ_Option.__version__)
```

## Check connect

return True/False

```
print(Iq.check_connect())
```

## Reconnect

```python
Iq.connect()
```

## time

get_server_timestamp
the get_server_timestamp time is sync with iqoption

```python
Iq.get_server_timestamp()
```
