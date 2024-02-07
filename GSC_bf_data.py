
from GSC_auth import authorize_creds
from GSC_requested_metrics import gsc_with_filters
from page_performance.app_data import bf_sites_short_name, bf_sites_GSC_credential_files, bf_sites_full_name, dimension, expression, operator


def webmasters_services():
    webmasters_service_all = []
    for i in range(len(bf_sites_short_name)):
        webmasters_service_all.append(authorize_creds(
            bf_sites_GSC_credential_files[i], bf_sites_short_name[i]))

    return webmasters_service_all


all_creds = webmasters_services()


def assiging_arg(all_creds, sites, creds, dimension, operator, expression, list_of_url):
    args = all_creds, sites, creds, dimension, operator, expression, list_of_url

    return args


def gsc_request(start_date, end_date, url):
    gsc_report = []

    for i in range(len(bf_sites_short_name)):
        args = assiging_arg(all_creds[i], bf_sites_full_name[i],
                            bf_sites_GSC_credential_files[i], dimension, operator, expression, url[i])
        gsc_report.append(gsc_with_filters(*args, start_date, end_date))
    return gsc_report
