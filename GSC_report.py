import pandas as pd

from GSC_data_cleaner import gsc_data_organizer
from GSC_bf_data import gsc_request
from url_organizer import url_extractor
from page_performance.app_data import bf_sites_short_name, cp_path, up_path, bf_sites_full_name
# this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name


def get_full_url(urls, site):
    # accessing the array of urls in dic from url_extractor
    urls_list = urls[2]
    urls_list = [site + x for x in urls_list]
    return urls_list


def get_url(path: str):
    list_of_url = []
    for i in range(len(bf_sites_short_name)):
        list_of_url.append(get_full_url(
            url_extractor(path)[i], bf_sites_full_name[i]))

    return list_of_url


def collect_GSC_data(start, end, path):
    gsc_data = gsc_request(start, end, get_url(path))

    return gsc_data


def create_GSC_report_for_cp(this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name):

    gsc_cp_reports = {}
    k = 0
    while k < len(bf_sites_short_name):
        key_cp = bf_sites_short_name[k] + '_gsc_cp'
        value_cp = gsc_data_organizer(collect_GSC_data(pre_month_start, pre_month_end, cp_path)[
                                      k], collect_GSC_data(this_month_start, this_month_end, cp_path)[k], pre_month_name, this_month_name)
        gsc_cp_reports[key_cp] = value_cp

        k += 1

    return gsc_cp_reports


def create_GSC_report_for_up(this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name):

    gsc_up_reports = {}
    k = 0
    while k < len(bf_sites_short_name):
        key_up = bf_sites_short_name[k] + '_gsc_up'
        value_up = gsc_data_organizer(collect_GSC_data(pre_month_start, pre_month_end, up_path)[
                                      k], collect_GSC_data(this_month_start, this_month_end, up_path)[k], pre_month_name, this_month_name)
        gsc_up_reports[key_up] = value_up

        k += 1

    return gsc_up_reports
