# Page Performance Report

## A fully functional application written in Python showing how you can pull GA4 and GSC data within the API request and show results in a beautiful coloured table with the streamlit 


This project is built in Python to fulfill the need to have a fully automated custom SEO report showing the important metrics of your core and the updated pages. It shows the SEO metrics of your pages after your page content is updated and compares the performance progress within previous and current months. Each part of this project is simply coded to do the following:

* Connect to GA4 API via Python
  
* Connect to GSC API via Python
  
* Create authentication files for accessing GA4 and GSC data of your sites (As many sites as you want)
  
* Request custom filters for the data query such as Country, pages and dates
  
* Request GA4 metrics such as Conversions, Sessions, Engaged Sessions, Bounce Rate, Engagement Rate, User Engagement Duration, Active Users and Average Engagement Time
  
* Request GSC metrics such as Clicks, Impressions and Position
  
* Combine GA4 and GSC data in an Excel sheet
  
* Organized your data based on the name of the previous and the current month
  
* Show the changes/differences for each metric during one month
  
* Show the coloured result in a web app with the Streamlit


## Installation

The easiest way is as follows:

* Use the requirements file: ```pip install -r requirements.txt```
  
* Create a folder named ``` credential``` inside it create 2 folder named ```GA4``` and ```GSC```

* Create a folder named ``` excel_files``` for your list of pages you need for the report
  
* Add your site credential service account file for GA4 and Client Secret JSON file for the GSC folder

* Instantiate variables in ```app_data.py``` file as follows:
  
* ```bf_sites_full_name``` : add your sites full name
  
* ```bf_sites_short_name```: add your site short name (It can be anything you like)
  
*  ```bf_sites_properties``` : you should add GA4 property id for your sites

*  ```bf_sites_GA4_credential_files```: add your GA4 location with the short name you choose for your site
  
*  ```bf_sites_GSC_credential_files```: add your GSC location with the short name you choose for your site
  
*  ```cp_path```: add your file path to your core pages (Static pages)
  
*  ```up_path```: add your file path to your updated pages (Dynamic pages)














