import pandas as pd

from GA4_bf_data import store_GA4_data
from GA4_data_cleaner import sorted_report
from page_performance.app_data import cp_path, up_path, bf_sites_short_name
from url_organizer import url_extractor


def create_GA4_report_for_cp(this_month_start, this_month_end, this_month_name, pre_month_start, pre_month_end, pre_month_name):
    cp_data = url_extractor(cp_path)
    GA4_cp_reports = {}
    k = 0
    while k < len(bf_sites_short_name):
        key_cp = bf_sites_short_name[k] + '_GA4_cp'
        value_cp = sorted_report(list(store_GA4_data(cp_data, 'core', this_month_start, this_month_end, this_month_name,
                                 pre_month_start, pre_month_end, pre_month_name).values())[k], pre_month_name, this_month_name)
        GA4_cp_reports[key_cp] = value_cp

        k += 1

    return GA4_cp_reports


def create_GA4_report_for_up(pre_month_name, this_month_name):
    up_data = url_extractor(up_path)
    GA4_up_reports = {}
    k = 0
    while k < len(bf_sites_short_name):
        key_up = bf_sites_short_name[k] + '_GA4_up'
        value_up = sorted_report(list(store_GA4_data(up_data, 'updated').values())[
                                 k], pre_month_name, this_month_name)
        GA4_up_reports[key_up] = value_up

        k += 1
    return GA4_up_reports
