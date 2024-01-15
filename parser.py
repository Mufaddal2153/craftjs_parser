import requests, json, re
from mappings import html_to_json_mapping


# Sample URL to fetch the html page 
# url = "https://mek.com.pk/"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#     'Accept-Encoding': 'none'
# }
  
# # Get the page through get() method 
# html_response = requests.get(url=url, headers=headers) 

# # Save the page content as sample.html 
# with open("sample.html", "w") as html_file: 
#     html_file.write(html_response.text)

data = html_to_json_mapping("test.html")

craftjs = {}

# for i, j in data.items():
#     if i == "children":
        