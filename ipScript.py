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
	    	response = requests.get("https://www.iplocation.net/", data={"query": line['source_ip'], "submit": "IP Lookup"})
	    	txt = html.fromstring(response.content)
	    	areas = txt.xpath('//td/text()')
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