import pandas as pd

from GA4_report import create_GA4_report_for_cp, create_GA4_report_for_up
from GSC_report import create_GSC_report_for_cp, create_GSC_report_for_up
from page_performance.app_data import bf_sites_short_name, pre_month_name, this_month_name


# Merging all the data from GSC and GA4
def merging_gsc_ga4_data(df_gsc, df_ga4):
    df_final = pd.merge(df_gsc, df_ga4, on='page', how='outer')
    return df_final

# Calling each properties for thier data


def create_performance_report_for_cp(i, this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name):
    report = merging_gsc_ga4_data(list(create_GSC_report_for_cp(this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name).values())[
                                  i], list(create_GA4_report_for_cp(this_month_start, this_month_end, this_month_name, pre_month_start, pre_month_end, pre_month_name).values())[i])
    report = report.fillna(0)
    return report

# def create_performance_report_for_up(i, this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name):
#     report = merging_gsc_ga4_data(list(create_GSC_report_for_up(this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name).values())[i], list(create_GA4_report_for_up(pre_month_name, this_month_name).values())[i])
#     report = report.fillna(0)
#     return report


def Create_xlsx_sheet(file_name, df1, df2, cp='Core_pages', up='Updated_pages'):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(
        './Result/'+f'{file_name}'+'.xlsx', engine="xlsxwriter")
    # Write each dataframe to a different worksheet.
    df1.to_excel(writer, sheet_name=f'{cp}', index=False)
    df2.to_excel(writer, sheet_name=f'{up}', index=False)
    # Close the Pandas Excel writer and output the Excel file.
    writer.close()

# def create_all_reports():
#     for i in range(len(bf_sites_short_name)):
#         Create_xlsx_sheet(bf_sites_short_name[i], create_performance_report_for_cp(i), create_performance_report_for_up(i))

# report = merging_gsc_ga4_data(list(create_GSC_report_for_cp().values())[0], list(create_GA4_report_for_cp().values())[0])


# df = pd.DataFrame.from_dict(create_performance_report_for_cp(0,this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name))
# print(pre_month_name, this_month_name)
# create_all_reports()
print("success")
