
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Filter,
    FilterExpression,
    FilterExpressionList,
    Metric,
    RunReportRequest,
)

# from constant_data import this_month_start, this_month_end, this_month_name, pre_month_start, pre_month_end, pre_month_name

client = []

def run_GA4_report(this_month_start, this_month_end, this_month_name, pre_month_start, pre_month_end, pre_month_name, property_id , pages):
    path_list = []
    Date_list = []
    conversions_list = []
    sessions_list = []
    engagedSessions_list = []
    bounceRate_list = []
    engagementRate_list = []
    userEngagementDuration_list = []
    activeUsers_list = []
    averageEngagementTime_list = []
    data = {}
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="country"), Dimension(name="pagePath")],
        metrics=[Metric(name="conversions"), Metric(name="sessions"),Metric(name="engagedSessions"),Metric(name="bounceRate"),Metric(name="engagementRate"), Metric(name="userEngagementDuration"),Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=pre_month_start, end_date=pre_month_end, name=pre_month_name),DateRange(start_date=this_month_start, end_date=this_month_end, name=this_month_name)],
        dimension_filter=FilterExpression(
            and_group=FilterExpressionList(
                expressions=[
                    FilterExpression(
                            filter=Filter(
                                field_name="pagePath",
                                in_list_filter=Filter.InListFilter(
                                    values= pages
                                    )
                                )
                            ),
                        FilterExpression(filter=Filter(
                                field_name="country",
                                string_filter=Filter.StringFilter(value="United States"),
                            )
                        ),
                    ]
                    )
                )
        )
            

    response = client.run_report(request)
    
    for row in response.rows:
        path_list.append(row.dimension_values[1].value)
        Date_list.append(row.dimension_values[2].value)
        conversions_list.append(int(row.metric_values[0].value))
        sessions_list.append(int(row.metric_values[1].value)) 
        engagedSessions_list.append(int(row.metric_values[2].value))
        bounceRate_list.append("{:.2%}".format(float(row.metric_values[3].value)))
        engagementRate_list.append("{:.2%}".format(float(row.metric_values[4].value)))
        userEngagementDuration_list.append(int(row.metric_values[5].value))
        activeUsers_list.append(int(row.metric_values[6].value))
        if(int(row.metric_values[6].value) == 0):
            averageEngagementTime_list.append(int(0))
        else:
            averageEngagementTime_list.append(round(int(row.metric_values[5].value)/ int(row.metric_values[6].value),2))
            
            
    data = {'path':path_list,
        'Date_list': Date_list,
        'conversions':conversions_list,
        'sessions': sessions_list,
        'engagedSessions': engagedSessions_list,
        'bounceRate': bounceRate_list,
        'engagementRate': engagementRate_list,
        'userEngagementDuration': userEngagementDuration_list,
        'activeUsers': activeUsers_list,
        'averageEngagementTime' : averageEngagementTime_list
            }
    
    return data
