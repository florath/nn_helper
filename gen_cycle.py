import pandas as pd
import numpy as np

def gen_cyc_sc_time_in_day(data, tsname):
    '''Generate nn friendly sin/cos entries for hour in day'''
    ti_in_day = (data[tsname].dt.hour * 3600
                 + data[tsname].dt.minute * 60
                 + data[tsname].dt.second)
    data['time_in_day_sin'] = np.sin(2 * np.pi * ti_in_day/86400)
    data['time_in_day_cos'] = np.cos(2 * np.pi * ti_in_day/86400)
    return data

def gen_cyc_sc_time_in_week(data, tsname):
    '''Generate nn friendly sin/cos entries for time in week'''
    ti_in_week = (data[tsname].dt.dayofweek * 86400
                  + data[tsname].dt.hour * 3600
                  + data[tsname].dt.minute * 60
                  + data[tsname].dt.second)
    # Debug only!
    # data['time_in_week'] = ti_in_week
    data['time_in_week_sin'] = np.sin(2 * np.pi * ti_in_week/(86400 * 7))
    data['time_in_week_cos'] = np.cos(2 * np.pi * ti_in_week/(86400 * 7))
    return data

def gen_cyc_sc_time_in_month(data, tsname):
    '''Generate nn friendly sin/cos entries for time in month'''
    length_of_month = (data[tsname].dt.days_in_month * 86400)
    # Debug only!
    # data['length_of_month'] = length_of_month
    ti_in_month = (
        (data[tsname].dt.day - 1) * 86400
        + data[tsname].dt.hour * 3600
        + data[tsname].dt.minute * 60
        + data[tsname].dt.second)
    # Debug only!
    # data['time_in_month'] = ti_in_month
    data['time_in_month_sin'] = np.sin(2 * np.pi * ti_in_month/length_of_month)
    data['time_in_month_cos'] = np.cos(2 * np.pi * ti_in_month/length_of_month)
    return data

df = pd.DataFrame(
    {
        # 'timestamp': pd.date_range('2020-08-28', '2020-09-07', freq='15T')
        'timestamp': pd.date_range('2020-08-22', '2020-09-07', freq='8H')
    }
)

df = gen_cyc_sc_time_in_day(df, 'timestamp')
df = gen_cyc_sc_time_in_week(df, 'timestamp')
df = gen_cyc_sc_time_in_month(df, 'timestamp')
print(df)
print(df[:200])
    
