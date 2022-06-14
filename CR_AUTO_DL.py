from ast import Index
from this import d
from time import strftime, strptime
from unittest import skip
import requests
from bs4 import BeautifulSoup
import csv
import calendar
from calendar import day_name
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver import Chrome


dateCR = ['MON','TUE','WED','THU','FRI','SAT','SUN']
date_CR = []
program_name = []
program_time = []
program_host = []
program_date = []

for x in range(7):
    driver = webdriver.Chrome()
    
    link_cr1 = 'https://www.881903.com/timetable/881/list#4'
    driver.get(link_cr1)

    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #f = requests.get(link, headers=headers)          
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    for tag_name in soup.find_all('div',class_='timetable-grid__headline-wrapper'):
        program_name.append(tag_name.text)

    for tag_host in soup.find_all('div',class_='flex timetable-grid__host'):
        program_host.append(tag_host.text)

    for tag_time in soup.find_all('div',class_='timetable-grid__time timetable-grid__time--wrap'):
        program_time.append(tag_time.text)

    for tag_date in soup.find_all('span',class_='week-bar__link base-button'):
        program_date.append(tag_date.text)

    break


# insetr date 
now = date.today()
for day in range(7):
    d = now +timedelta(days = day)
    date_CR.append( d.strftime("%Y%m%d"))

combine_data = []
i = 0
z = 0
for item in program_name:
    combine_data.append([item]+[program_host[i]]+[program_time[i]])
    i=i+1

count = 0
for everything in combine_data:
    everything.insert(0,'CR1')
    everything.insert(0,str(count))
    everything.append('Date')
    everything.append('SUN-MON')
    count = count + 1

for row in combine_data:
    if '一切從音樂開始'in row: 
        for change in combine_data[combine_data.index(row):]:
            change[-1] = dateCR[z]
            change[-2] = date_CR[z]
        z=z+1


# for CR2

combine_data_cr2 = []
program_name_cr2 = []
program_name_cr2 = []
program_time_cr2 = []
program_host_cr2 = []
program_date_cr2 = []

for x in range(7):
    driver = webdriver.Chrome()
    
    link_cr2 = 'https://www.881903.com/timetable/903/list#4'
    driver.get(link_cr2)

    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #f = requests.get(link, headers=headers)          
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    for tag_name in soup.find_all('div',class_='timetable-grid__headline-wrapper'):
        program_name_cr2.append(tag_name.text)

    for tag_host in soup.find_all('div',class_='flex timetable-grid__host'):
        program_host_cr2.append(tag_host.text)

    for tag_time in soup.find_all('div',class_='timetable-grid__time timetable-grid__time--wrap'):
        program_time_cr2.append(tag_time.text)

    for tag_date in soup.find_all('span',class_='week-bar__link base-button'):
        program_date_cr2.append(tag_date.text)

    break

i = 0
z = 0
for item in program_name_cr2:
    combine_data_cr2.append([item]+[program_host_cr2[i]]+[program_time_cr2[i]])
    i=i+1


count = 0
for everything in combine_data_cr2:
    everything.insert(0,'CR2')
    everything.insert(0,str(count))
    everything.append('Date')
    everything.append('SUN-MON')
    count = count + 1

for row in combine_data_cr2:
    if '一切從音樂開始'in row: 
        for change in combine_data_cr2[combine_data_cr2.index(row):]:
            change[-1] = dateCR[z]
            change[-2] = date_CR[z]
        z=z+1

#combine CR1 & CR2
for all in combine_data_cr2:
    combine_data.append(all)

#delete index
for column in combine_data:
    del column[0]



#re-order list
myorder = [0, 4, 5, 3 ,1, 2]
for order in combine_data:
    combine_data[combine_data.index(order)] = [order[z] for z in myorder]

# delimit space in time column
for space in combine_data:
    space[3] = space[3].replace(" ","")

csvheader = ['Program_channel','Date','SUN - MON','Program_time','CHIN_TITLE','Host']

file_name = 'CR_WEEKLY_DL.csv'

with open(file_name,'w',encoding='utf_8_sig', newline='')as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    for y in combine_data:
       writer.writerow(y)

print('done -.-') 