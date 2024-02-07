
import pandas as pd
from collections import defaultdict
from googleapiclient.discovery import build
from collections import defaultdict


def execute_request(service, property_uri, request):
    return service.searchanalytics().query(siteUrl=property_uri, body=request).execute()

def gsc_with_filters(webmasters_service,site,creds,dimension,operator,expression, list_of_urls,start_date,end_date,rowLimit=5000):
    scDict = defaultdict(list) # Create a dict to populate with extraction
   
    request = {
    'startDate': start_date,
    'endDate': end_date,
    'dimensions': 'page',  #country, device, page, query, searchAppearance
    'dimensionFilterGroups': [{
                    'filters': [{
                        'dimension': dimension,              
                        'operator': operator,
                        'expression': expression
                    }]
                    }],
    'rowLimit': rowLimit
    }

    response = execute_request(webmasters_service, site, request)
     
    try:
        for row in response['rows']:
            for i in range(len(list_of_urls)):
                if(row['keys'][0] == list_of_urls[i] ):
                
                    # scDict['date'].append(row['keys'][0] or 0)    
                    scDict['page'].append(row['keys'][0] or 0)
                    # scDict['country'].append(row['keys'][1] or 0)
                    scDict['clicks'].append(row['clicks'] or 0)
                    scDict['impressions'].append(row['impressions'] or 0)
                    # scDict['ctr'].append(row['ctr'] or 0)
                    scDict['position'].append(row['position'] or 0)
    except Exception as e:
            print(f'An error occurred: {e}')

    # Add response to dataframe 
    df = pd.DataFrame(data = scDict)
    print(df)
    return df