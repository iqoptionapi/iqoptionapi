# python
import math
from datetime import datetime as dt, timedelta
import time

# https://docs.python.org/3/library/datetime.html
# If optional argument tz is None or not specified, the timestamp is converted to the platform's local date and time, and the returned datetime object is naive.
# time.mktime(dt.timetuple())


def date_to_timestamp(dt):
    # local timezone to timestamp support python2 pytohn3
    return time.mktime(dt.timetuple())


def get_expiration_time(timestamp, duration):
    """
    Calcula o tempo de expiração para ordens na IQ Option.

    Parâmetros:
    - timestamp: int, timestamp Unix do servidor (hora atual)
    - duration: int, duração em minutos (1 a 180 minutos)

    Retorna:
    - tuple: (int, int) - timestamp Unix de expiração e índice (idx)
    """
    current_time = dt.fromtimestamp(timestamp)

    if duration <= 5:
        # Lógica para durações de 1 a 5 minutos (turbo)
        minutes_to_add = duration if current_time.second < 30 else duration + 1
        expiration_dt = current_time + timedelta(minutes=minutes_to_add)
        expiration_dt = expiration_dt.replace(second=0, microsecond=0)
        idx = duration - 1  # 0 a 4 para turbo
    else:
        # Lógica para durações maiores que 5 minutos (binary)
        # Calcula o tempo de expiração desejado
        desired_expiration = current_time + timedelta(minutes=duration)
        minute = desired_expiration.minute

        # Múltiplo de 15 anterior
        prev_multiple = (minute // 15) * 15
        prev_time = desired_expiration.replace(minute=prev_multiple, second=0, microsecond=0)

        # Múltiplo de 15 posterior
        next_multiple = math.ceil((minute + 1) / 15) * 15
        if next_multiple >= 60:
            next_time = desired_expiration.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        else:
            next_time = desired_expiration.replace(minute=next_multiple, second=0, microsecond=0)

        # Escolhe o mais próximo, garantindo que seja no futuro
        if prev_time < current_time:
            expiration_dt = next_time
        else:
            if abs((prev_time - desired_expiration).total_seconds()) <= abs((next_time - desired_expiration).total_seconds()):
                expiration_dt = prev_time
            else:
                expiration_dt = next_time
        idx = 5  # Para binary

    exp = int(date_to_timestamp(expiration_dt))
    return exp, idx


def get_remaning_time(timestamp):
    """
    Calcula os tempos restantes para expirações de curto e longo prazo.

    Parâmetros:
    - timestamp: int, timestamp Unix do servidor (hora atual)

    Retorna:
    - list: Lista de tuplas (duração_em_minutos, tempo_restante_em_segundos)
    """
    # Converte o timestamp para datetime e zera segundos/microssegundos
    current_time = dt.fromtimestamp(timestamp)
    exp_date = current_time.replace(second=0, microsecond=0)

    # Ajuste inicial para expirações de curto prazo
    seconds_to_next_minute = int(date_to_timestamp(exp_date + timedelta(minutes=1))) - timestamp
    if seconds_to_next_minute > 30:
        exp_date += timedelta(minutes=1)
    else:
        exp_date += timedelta(minutes=2)

    # Gera expirações de curto prazo (1 a 5 minutos)
    short_term_exps = []
    for i in range(5):
        exp_time = int(date_to_timestamp(exp_date))
        short_term_exps.append((i + 1, exp_time - timestamp))
        exp_date += timedelta(minutes=1)

    # Gera expirações de longo prazo (múltiplos de 15 minutos)
    long_term_exps = []
    exp_date = current_time.replace(second=0, microsecond=0)
    index = 0
    while index < 11:
        exp_time = int(date_to_timestamp(exp_date))
        if exp_date.minute % 15 == 0 and (exp_time - timestamp) > 300:  # 5 minutos
            long_term_exps.append((15 * (index + 1), exp_time - timestamp))
            index += 1
        exp_date += timedelta(minutes=1)

    # Combina as expirações de curto e longo prazo
    return short_term_exps + long_term_exps

