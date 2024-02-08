import pandas as pd

from constant_data import bf_sites_short_name, bf_sites_GA4_credential_files, bf_sites_property_id

def url_extractor (path :str) :
        
        big_foot = []      
# read excel file
        df = pd.read_excel(path)
        
#  extract each site url
        big_foot_urls = {}
        k = 0
        # len(bf_sites_short_name)
        while k < len(bf_sites_short_name):
        # dynamically create key
                key = bf_sites_short_name[k]
                # calculate value
                value = [x for x in df[bf_sites_short_name[k]].tolist() if str(x)!='nan']
                big_foot_urls[key] = value 
                k += 1
        
#  return an array including credential file, property_id and list of urls for each sites
        for site in big_foot_urls:
                big_foot.append([bf_sites_GA4_credential_files[site],bf_sites_property_id[site], big_foot_urls[site]])
       
        return  big_foot


# cp_path = './excel_files/mini_core_pages.xlsx'
# i = 0
# for i in range(len(bf_sites_short_name)):
#         x = url_extractor(cp_path)[i]
       
# print(x)