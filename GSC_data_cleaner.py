import pandas as pd


def df_renaming(df, month):
    df = df.rename(columns={'clicks': f'{month}'+'_clicks','impressions': f'{month}'+'_impressions','position': f'{month}'+'_position'})
    
    return df

def df_change_calculator(df, month1, month2):
    df['Clicks_Change'] = df[f'{month2}'+'_clicks'] - df[f'{month1}'+'_clicks']
    df['Impressions_Change'] = df[f'{month2}'+'_impressions'] - df[f'{month1}'+'_impressions']

    ct = round(df[f'{month2}'+'_position'],2) - round(df[f'{month1}'+'_position'],2)
    
    df['Position_Change'] = (-1) * ct
    
    return df

def df_sorter(df, month1, month2):
     df = df[['page',f'{month1}'+'_clicks',f'{month2}'+'_clicks','Clicks_Change',f'{month1}'+'_impressions',f'{month2}'+'_impressions','Impressions_Change',f'{month1}'+'_position',f'{month2}'+'_position','Position_Change']]
     return df

"""
Organizing GSC data based on the Month
"""
def gsc_data_organizer(df_month1, df_month2, month1, month2):
    # print(df_month1)
    # print(df_month1['position'])
    # df_month2['position'] = round(df_month2['position'],2)
    df_month1['position'] = round(df_month1['position'],2) 
    df_month2['position'] = round(df_month2['position'],2)
    
    df_month1 = df_renaming(df_month1, month1)
    df_month2 = df_renaming(df_month2, month2)
    # print(df_month1['November_position'])
    df_final = pd.merge(df_month1, df_month2, on ='page', how='outer')
   
    df_final = df_change_calculator(df_final, month1, month2)
    df_final = df_sorter(df_final, month1, month2)
    
    return df_final

    print('success')