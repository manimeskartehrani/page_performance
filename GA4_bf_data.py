import pandas as pd
import os
import GA4_requested_metrics

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from GA4_requested_metrics import run_GA4_report
from page_performance.app_data import bf_sites_short_name
# from data_organizer import df_correction_columns

""" 
collect data from GA4 for each sites 
"""


def GA4_data_collector(sites_info, this_month_start, this_month_end, this_month_name, pre_month_start, pre_month_end, pre_month_name):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = sites_info[0]
    GA4_requested_metrics.client = BetaAnalyticsDataClient()

    df_data = pd.DataFrame(run_GA4_report(this_month_start, this_month_end, this_month_name,
                           pre_month_start, pre_month_end, pre_month_name, property_id=sites_info[1], pages=sites_info[2]))

    return df_data


"""
Core pages GA4 data
"""


def store_GA4_data(arr, status: str, this_month_start, this_month_end, this_month_name, pre_month_start, pre_month_end, pre_month_name):
    GA4_data = {}
    k = 0
    # len(bf_sites_short_name)
    while k < 1:
        key = bf_sites_short_name[k] + f'_{status}_pages'
        value = pd.DataFrame(GA4_data_collector(
            arr[k], this_month_start, this_month_end, this_month_name, pre_month_start, pre_month_end, pre_month_name))

        GA4_data[key] = value
        k += 1

    return GA4_data
