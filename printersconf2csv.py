#Import
import csv
import re
import itertools

#Initialize
file = open('printers.conf', mode = 'r', encoding = 'utf-8-sig')
infos = []
drivers = []
names = []
ips = []
locations = []
headers = ["Printername", "Location", "Comment", "Driver"]

#Get lines from file
lines = file.readlines()

#Parse printers names
for line in lines:
	if line.startswith('<Printer'):
		line = re.sub('<Printer', '', line)
		line = re.sub('>', '', line)
		line = re.sub(' ', '', line)
		line = re.sub('\n', '', line)
		names.append(line)

#Parse printer driver
for line in lines:
	if line.startswith('MakeModel'):
		line = re.sub('MakeModel ', '', line)
		line = re.sub('\n', '', line)
		drivers.append(line)

#Parse comments
for line in lines:
	if line.startswith('Info'):
		line = re.sub('Info ', '', line)
		line = re.sub('\n', '', line)
		infos.append(line)

#Parse IP Adresses
for line in lines:
	if line.startswith('DeviceURI'):
		line = re.sub('DeviceURI ', '', line)
		line = re.sub('socket://', '', line)
		line = re.sub('\n', '', line)
		ips.append(line)

for line in lines:
	if line.startswith('Location'):
		line = re.sub('Location ', '', line)
		line = re.sub('\n', '', line)
		locations.append(line)


#Export to csv file
with open('printers.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
	headers = ['Printername', 'Driver', 'Comment', 'IPAddress', 'Location']
	writer = csv.DictWriter(csvfile, fieldnames=headers)
	writer.writeheader()
	for name,driver,info,ip,location in zip(names,drivers,infos,ips,locations):
		writer.writerows([{'Printername': name, 'Driver': driver, 'Comment': info, 'IPAddress': ip, 'Location': location}])


file.close()