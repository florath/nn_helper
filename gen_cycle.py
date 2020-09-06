import pandas as pd
import numpy as np
import datetime
import ephem


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

def gen_cyc_sc_time_in_year(data, tsname):
    '''Generate nn friendly sin/cos entries for time in year'''
    year_secs = (365 * 86400 + data[tsname].dt.is_leap_year * 86400)
    # Debug only!
    # data['year_secs'] = year_secs
    ti_in_year = (
        data[tsname].dt.dayofyear * 86400
        + data[tsname].dt.hour * 3600
        + data[tsname].dt.minute * 60
        + data[tsname].dt.second)
    # Debug only!
    # data['time_in_year'] = ti_in_year
    data['time_in_year_sin'] = np.sin(2 * np.pi * ti_in_year/year_secs)
    data['time_in_year_cos'] = np.cos(2 * np.pi * ti_in_year/year_secs)
    return data

def get_moon_phase_on_day(dtime):
    '''Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new'''

    date=ephem.Date(dtime)
    #print(date)
    nnm = ephem.next_new_moon(date)
    pnm = ephem.previous_new_moon(date)
    #print("Prev ", pnm)
    #print("Next ", nnm)
    lunation=(date-pnm)/(nnm-pnm)

    return lunation

def gen_cyc_sc_time_in_moon(data, tsname):
    '''Generate nn friendly sin/cos entries for time in moon'''
    moon_phase = data['timestamp'].apply(get_moon_phase_on_day)
    print(moon_phase)
    
    # Debug only!
    # data['moon_phase'] = moon_phase
    data['time_in_moon_sin'] = np.sin(2 * np.pi * moon_phase)
    data['time_in_moon_cos'] = np.cos(2 * np.pi * moon_phase)
    return data

def gen_cyc_sc_all(data, tsname):
    data = gen_cyc_sc_time_in_day(data, tsname)
    data = gen_cyc_sc_time_in_week(data, tsname)
    data = gen_cyc_sc_time_in_month(data, tsname)
    data = gen_cyc_sc_time_in_year(data, tsname)
    data = gen_cyc_sc_time_in_moon(data, tsname)
    return data

#print(get_moon_phase_on_day(datetime.datetime.now()))
#print(get_moon_phase_on_day("2020-09-02"))
#print(get_moon_phase_on_day("2020-08-19"))

df = pd.DataFrame(
    {
        # 'timestamp': pd.date_range('2020-08-28', '2020-09-07', freq='15T')
        'timestamp': pd.date_range('2020-08-22', '2020-10-09', freq='2D')
    }
)

df = gen_cyc_sc_all(df, 'timestamp')
print(df)
print(df[:200])
    
