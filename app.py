import csv
import requests
from bs4 import BeautifulSoup

path = "./db/db.csv"
headers = {
	"authority": "empireflippers.com",
	"method": "GET",
	"path": "/marketplace/",
	"scheme": "https",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "en-US,en;q=0.9",
	"cache-control": "max-age=0",
	"cookie": "__cfduid=d55725d37a2e43176b6b2c297d2b424181610077058; _vwo_uuid_v2=D4B9F51286F72FDC9F544036146F7F987|c9b9acfc70db2df522be3f9751d65dee; _gcl_au=1.1.1297859503.1610077059; _gid=GA1.2.1901064526.1610077059; _wingify_pc_uuid=186af38637654c1f8c7f6e853c836fbd; _fbp=fb.1.1610077059821.323290752; __hstc=216198473.44825db2217bd4b9eabbce3247fb075d.1610077060247.1610077060247.1610077060247.1; hubspotutk=44825db2217bd4b9eabbce3247fb075d; __hssrc=1; wingify_donot_track_actions=0; messagesUtk=021011d1777c41ac9f3ecf5174241415; wingify_push_do_not_show_notification_popup=true; _ga_6PKXFNRMBY=GS1.1.1610077059.1.1.1610077279.0; _ga=GA1.2.1661713616.1610077059; _uetsid=db6fb180516211eb98e90b0e6de75f3b; _uetvid=db6fcc20516211eb83941dad141ecbed; _gat_UA-23233138-8=1; __hssc=216198473.2.1610077060247",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "none",
	"sec-fetch-user": "?1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"	
}
URL = "https://empireflippers.com/marketplace/"
page = requests.get(URL, headers=headers)

# read file
def readFromCSV():
  with open(path, 'r', newline='') as file:
    reader = csv.reader(file)

    for row in reader:
      print(row)

aa = ["i","hate","eggs"]
bb = ["salad", "is", "fav"]

data = [aa, bb]

# write file
def writeToCsv():
  with open(path, 'a') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    



soup = BeautifulSoup(page.content, 'html.parser')
resultsListing = soup.find(id="results-listing")
# print(resultsListing.prettify())

listingItems = soup.find('div','listing-item-row')

print(len(listingItems))
print(listingItems.prettify)






if __name__ == "__main__":
  # readFromCSV()

  pass