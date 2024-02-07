import pandas as pd
import numpy as np
from page_performance.app_data import bf_sites_full_name


def df_columns_removers(df):
    try:
        df = df.drop(
            columns=['Unnamed: 0', 'userEngagementDuration', 'activeUsers'], axis=1)
    except KeyError:
        print('Column not found')
    return df


def df_one_columns_removers(df):
    try:
        df = df.drop(columns=['Date_list'], axis=1)
    except KeyError:
        print('Column not found')
    return df


def p2f(x):
    # if x == np.nan or x == 'NaN':
    #     return 0
    if '%' in x:
        return float(x.strip('%'))/100
    else:
        return x


def f2p(x):
    return "{:.2%}".format(x)


def convertor(ser1):
    res1 = []
    res2 = []
    res3 = []
    for i in range(len(ser1)):
        res1.append(p2f(ser1[i]))
        res2.append(res1[i] * (-1))
        res3.append(f2p(res2[i]))
    return res3


def series_calculator(ser1, ser2):
    df = []
    df2 = []
    df3 = []
    res = []
    series_len = range(len(ser1))
    for i in series_len:
        df.append(p2f(ser1[i]))
        df2.append(p2f(ser2[i]))
        df3.append(df2[i] - df[i])
        if '%' in ser1[i]:
            res.append(f2p(df3[i]))
        else:
            res.append(['%.2f' % elem for elem in df3])
    return res


def df_column_corrector(df, month):
    df = df.rename(columns={'conversions': f'{month}'+'_conversions', 'sessions': f'{month}'+'_sessions', 'engagedSessions': f'{month}'+'_Engaged_Sessions',
                   'bounceRate': f'{month}'+'_Bounce_Rate', 'engagementRate': f'{month}'+'_Engagement_Rate', 'averageEngagementTime': f'{month}'+'_Average_Engagement_Time'})

    return df


def df_column_sorter(df, month_1, month_2):
    df = df[['path', f'{month_1}'+'_conversions', f'{month_2}'+'_conversions', 'Conversion_Change', f'{month_1}'+'_sessions', f'{month_2}'+'_sessions', 'Sessions_Change', f'{month_1}'+'_Engaged_Sessions', f'{month_2}'+'_Engaged_Sessions', 'Engaged_Sessions_Change', f'{month_1}' +
             '_Bounce_Rate', f'{month_2}'+'_Bounce_Rate', 'Bounce_Rate_Change', f'{month_1}'+'_Engagement_Rate', f'{month_2}'+'_Engagement_Rate', 'Engagement_Rate_Change', f'{month_1}'+'_Average_Engagement_Time', f'{month_2}'+'_Average_Engagement_Time', 'Average_Engagement_Time_Change']]

    return df


def df_change_calculator(df, month_1, month_2):
    df['Conversion_Change'] = df[f'{month_2}' +
                                 '_conversions'] - df[f'{month_1}'+'_conversions']
    df['Sessions_Change'] = df[f'{month_2}' +
                               '_sessions'] - df[f'{month_1}'+'_sessions']
    df['Engaged_Sessions_Change'] = df[f'{month_2}' +
                                       '_Engaged_Sessions'] - df[f'{month_1}'+'_Engaged_Sessions']
    df['Bounce_Rate_Change'] = convertor(series_calculator(
        df[f'{month_1}_Bounce_Rate'], df[f'{month_2}'+'_Bounce_Rate']))
    df['Engagement_Rate_Change'] = series_calculator(
        df[f'{month_1}'+'_Engagement_Rate'], df[f'{month_2}'+'_Engagement_Rate'])
    df['Average_Engagement_Time_Change'] = df[f'{month_2}' +
                                              '_Average_Engagement_Time'] - df[f'{month_1}'+'_Average_Engagement_Time']

    return df


def df_null_column_convertor(df, month):
    if df[f'{month}_Bounce_Rate'].isnull().any():

        df.fillna({f'{month}'+'_Bounce_Rate': '0.0%'}, inplace=True)
        # df[f'{month}_Bounce_Rate'] = df[f'{month}_Bounce_Rate'].replace(0,'0.0%')
    if df[f'{month}_Engagement_Rate'].isnull().any():
        df.fillna({f'{month}'+'_Engagement_Rate': '0.0%'}, inplace=True)
    else:
        df = pd.DataFrame(df).fillna(0)
        # df[f'{month}_Engagement_Rate'] = df[f'{month}_Engagement_Rate'].fillna({f'{month}'+'_Engagement_Rate':'0.0%'})
        # df[f'{month}_Bounce_Rate'] = df[f'{month}_Bounce_Rate'].fillna({f'{month}'+'_Bounce_Rate':'0.0%'})
        # df.fillna({f'{month}'+'_conversions':0}, inplace= True)
        # df.fillna({f'{month}'+'_sessions':0}, inplace= True)
        # df.fillna({f'{month}'+'_Engaged_Sessions':0}, inplace= True)
        # df.fillna({f'{month}'+'_Average_Engagement_Time':0}, inplace= True)
    return df


def df_month_organizer(df, month):
    df = df[df['Date_list'] == f'{month}']
    df = df_columns_removers(df)
    df = df_one_columns_removers(df)
    return df


def df_correction_columns(df, sites):
    for i in range(len(sites)):
        df.rename(columns={'path': 'page'}, inplace=True)
        df['page'] = [sites + x for x in df['page']]

        return df


def sorted_report(df, month1, month2):

    df_month_1 = df_month_organizer(df, month1)
    df_month_2 = df_month_organizer(df, month2)

    df_month_1 = df_column_corrector(df_month_1, month1)
    df_month_2 = df_column_corrector(df_month_2, month2)
    # df_month_1 = df_null_column_convertor(df_month_1, month1)
    # df_month_2 = df_null_column_convertor(df_month_2, month2)
    df_final = pd.merge(df_month_1, df_month_2, on='path', how='right')

    df_final = df_null_column_convertor(df_final, month1)
    df_final = df_null_column_convertor(df_final, month2)
    # print(df_final['November_Bounce_Rate'])
    df_final = df_change_calculator(df_final, month1, month2)
    df_final = df_column_sorter(df_final, month1, month2)
    df_final = df_correction_columns(df_final, bf_sites_full_name[0])

    return df_final
