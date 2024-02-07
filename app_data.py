import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
from date_calculator import check_date_condition
import performance_report


st.header("Welcome to Page Performance App")


bf_sites_full_name = [
    'https://www.site1.org',
    # 'https://www.site2.com',
    # 'https://www.site3.com',
    # 'https://www.site4.com',
    # 'https://www.site5.org',
]

# bf_sites_short_name = ['Site1','Site2','Site3','Site4','Site5']
bf_sites_short_name = ['Site1']

bf_sites_property_id = {
    'site1': "310314693",
    # 'site2':"310299920",
    # 'site3' : "309175679",
    # 'site4' : "310357841",
    # 'site5' : "309603795"
}

bf_sites_GA4_credential_files = {
    'site1': './credential/GA4/site1_service_account.json',
    # 'site2':'./credential/GA4/site2_service_account.json',
    # 'site3':'./credential/GA4/site3_service_account.json',
    # 'site4':'./credential/GA4/site4_service_account.json',
    # 'site5':'./credential/GA4/site5_service_account.json'
}

bf_sites_GSC_credential_files = [
    './credential/GSC/client_secret_site1.json',
    # './credential/GSC/client_secret_site2.json',
    # './credential/GSC/client_secret_site3.json',
    # './credential/GSC/client_secret_site4.json',
    # './credential/GSC/client_secret_site5.json'
]

# define core page and updated page path
cp_path = './excel_files/mini_core_pages.xlsx'
up_path = './excel_files/BF_updated_pages_Dec.xlsx'

# date instantiates
count = 0


# Filters
# dimension,operator,expression,
dimension = 'country'     # query, page
operator = 'equals'   # contains, equals, notEquals, notContains
expression = 'usa'   # whatever value that you want
# Using the "with" syntax
# Declare a form and call methods directly on the returned object
form = st.sidebar.form(key='my_form')
uploaded_files = form.file_uploader(
    "Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

todayDate = form.date_input(
    "Select the date for the report", value=date.today(), key=count)

this_month_start = check_date_condition(todayDate)[0][0]
this_month_end = check_date_condition(todayDate)[0][1]
this_month_name = check_date_condition(todayDate)[0][2]

pre_month_start = check_date_condition(todayDate)[1][0]
pre_month_end = check_date_condition(todayDate)[1][1]
pre_month_name = check_date_condition(todayDate)[1][2]

option = form.selectbox('Please select your properties:', ("Site1", "Site2",
                        "Site3", "Site4", "Site5"), index=None, placeholder="Select contact method...")

if (option == "Site1"):
    st.write('You selected:', option)
else:
    st.write("""
         
         
         """)


button1 = form.form_submit_button("Submit", type="primary")
button2 = form.form_submit_button("Reset", type="secondary")


def output_color(data):
    data['Bounce_Rate_Change'] = data['Bounce_Rate_Change'].str.replace(
        '%', '').astype(float)
    data['Engagement_Rate_Change'] = data['Engagement_Rate_Change'].str.replace(
        '%', '').astype(float)

    def bgcolor_positive_or_negative(value, props=''):
        bgcolor = "lightcoral" if value < 0 else "yellow" if value == 0 else "lightgreen"
        return f"background-color: {bgcolor};"

    s2 = data.style.map(bgcolor_positive_or_negative, props=f'background-color:{bgcolor_positive_or_negative};', subset=[
                        'Clicks_Change', 'Impressions_Change', 'Position_Change', 'Conversion_Change', 'Sessions_Change', 'Engaged_Sessions_Change', 'Bounce_Rate_Change', 'Engagement_Rate_Change', 'Average_Engagement_Time_Change'])

    return st.dataframe(s2.format({'Bounce_Rate_Change': '{:.2f}%', 'Engagement_Rate_Change': '{:.2f}%'}, precision=0))


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return pd.DataFrame.to_csv(df)


def dl_button(data):
    csv = convert_df(data)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )


print(this_month_start, this_month_end, this_month_name)
print(pre_month_start, pre_month_end, pre_month_name)
if (button1):
    if (option == "Site1"):
        data = performance_report.create_performance_report_for_cp(
            0, this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name)

        output_color(data)
        dl_button(data)

    if (option == "Site2"):
        data = performance_report.create_performance_report_for_cp(
            1, this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name)

        output_color(data)
        dl_button(data)

    if (option == "Site3"):
        data = performance_report.create_performance_report_for_cp(
            2, this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name)

        output_color(data)
        dl_button(data)

    if (option == "Site4"):
        data = performance_report.create_performance_report_for_cp(
            3, this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name)

        output_color(data)
        dl_button(data)

    if (option == "Site5"):
        data = performance_report.create_performance_report_for_cp(
            4, this_month_start, this_month_end, pre_month_start, pre_month_end, pre_month_name, this_month_name)

        output_color(data)
        dl_button(data)


if (button2):
    st.write('You selected:', option)
    st.write("""
            
            
            """)


# \
    # .format(precision = 1 ,thousands=",", decimal=".")
count += 1
