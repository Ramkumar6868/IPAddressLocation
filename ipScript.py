import csv
import requests
from lxml import html
import sys
file_loacation = sys.argv[1]
# requests.get("https://ipinfo.io/54.198.187.108/geo?token=81d9ff0bda7f62")
# requests.get("http://api.db-ip.com/v2/free/8.8.8.8")
tsv_file = open(file_loacation[0:len(file_loacation)-4] + "_result.tsv", 'w')
headers = ["id",	"generated_at",	"received_at",	"source_id", "source_name", "source_ip", "facility_name", "severity_name", "program", "message", "IP2Location", "IPInfo", "EurekApi", "DBIP"]
file_writer = csv.DictWriter(tsv_file, delimiter='\t', lineterminator='\n', fieldnames=headers)
file_writer.writeheader()
with open(file_loacation, 'r') as csv_file:
	    csv_reader = csv.DictReader(csv_file, delimiter='\t')
	    count = 0
	    for line in csv_reader:
	    	print("<========== fetching for IP:" + str(line['source_ip']) + "=============>")
	    	response = requests.post("https://www.iplocation.net/", data={"query": line['source_ip'], "submit": "IP Lookup"},  headers={"authority": "www.iplocation.net", "method": "POST", "path": "/", "scheme": "https", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "accept-encoding": "gzip, deflate, br", "accept-language": "en-GB,en-US;q=0.9,en;q=0.8", "cache-control": "max-age=0", "content-length": "37", "content-type": "application/x-www-form-urlencoded", "cookie": "visid_incap_877543=owjWAzuXTJ22QAIsHv3bhCT6/FsAAAAAQUIPAAAAAADcEHr4z+PTAYFnMkDy5TjD; _ga=GA1.2.664070655.1543305767; _gid=GA1.2.604991871.1543305769; __gads=ID=19818120b6e079c8:T=1543305773:S=ALNI_MY5yWuGqacVn4oBu3_yg_cC0WHrlw; incap_ses_967_877543=eIQZPZt4g2EgNzDK8HlrDdkV/VsAAAAA53T3GdWXAG3vhk8FZRLrPw==; _gat=1", "origin": "https://www.iplocation.net", "referer": "https://www.iplocation.net/", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"})
	    	txt = html.fromstring(response.content)
	    	areas = txt.xpath('//td/text()')
	    	print(areas)
	    	ip2_location = areas[3] + ', ' + areas[2] + ', ' + areas[1]
	    	line['IP2Location'] = ip2_location
	    	ip_info = areas[10] + ', ' + areas[10] + ', ' + areas[9]
	    	line['IPInfo'] = ip_info
	    	eurek_api = areas[18] + ', ' + areas[17] + ', ' + areas[16]
	    	line['EurekApi'] = eurek_api
	    	db_ip = areas[26] + ', ' + areas[25] + ', ' + areas[24]
	    	line['DBIP'] = db_ip
	    	file_writer.writerow(line)
tsv_file.close()