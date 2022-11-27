import requests
import json
base_url = "https://www.sefaria.org.il/api/texts/Sefer%20Yetzirah.1.2-3?context=0"
# url = "https://www.sefaria.org.il/api/texts/Sefer%20Yetzirah.1.2-3?context=0"






payload={}
header={}
# headers = {
#   'Cookie': 'csrftoken=JxnVNi8tHataLsxw4IgIfAIbsB8CyDGojRnq56U7RzElWBn8VEpUx62RJJNjStnt; interfaceLang=hebrew'
# }






response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
