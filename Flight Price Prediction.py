#!/usr/bin/env python
# coding: utf-8

# In[1]:


# lets first install the selinium library
get_ipython().system(' pip install selenium')


# In[2]:


# lets now import all the required libraries
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
import xlsxwriter
import csv


# In[18]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[19]:


url = 'https://www.makemytrip.com/flight/search?tripType=O&itinerary=CCU-DEL-06/11/2021&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1636145905327&forwardFlowRequired=true&gclid=EAIaIQobChMI2LaPssHw8wIVRTVyCh2i0g90EAAYAiAAEgKrBfD_BwE&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM%7CD%7CDF%7CG%7CRoute%7CDF_Route_Kolkata_Delhi_Exact%7CKolkata_Delhi_Exact%7CRSA%7C532427427811&s_kwcid=AL!1631!3!532427427811!e!!g!!kolkata%20to%20delhi%20flight&ef_id=EAIaIQobChMI2LaPssHw8wIVRTVyCh2i0g90EAAYAiAAEgKrBfD_BwE:G:s&isSemFlow=true'
driver.get(url)
sleep(6)


# In[20]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='boldFont blackText airlineName']")
titles_tags


# In[21]:


# Now the text of the flight title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles 


# In[24]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//p[@class='darkText']")
titles_tags


# In[68]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles 


# In[69]:


# so lets extract all the tags having the triptime-titles
titles = titles_tags=driver.find_elements_by_xpath("//div[@class='stop-info flexOne']")
titles_tags


# In[70]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles 


# In[71]:


# so lets extract all the tags having the layovers-titles
titles = titles_tags=driver.find_elements_by_xpath("//p[@class='flightsLayoverInfo']")
titles_tags


# In[72]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[73]:


# so lets extract all the tags having the to-titles
titles = titles_tags=driver.find_elements_by_xpath("//p[@class='darkText']")
titles_tags


# In[25]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles 


# In[8]:


# so lets extract all the tags having the price-titles
titles = titles_tags=driver.find_elements_by_xpath("//p[@class='blackText fontSize18 blackFont white-space-no-wrap']")
titles_tags


# In[26]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[29]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[4]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[5]:


url = 'https://flight.easemytrip.com/FlightList/Index?org=CCU-Kolkata,%20India%20,&dept=PNQ-Pune,%20India%20,&adt=1&chd=0&inf=0&cabin=0&airline=undefined&deptDT=08/11/2021&arrDT=undefined&isOneway=true&isDomestic=false&'
driver.get(url)
sleep(6)


# In[38]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='txt-r4 ng-binding']")
titles_tags


# In[39]:


# Now the text of the flight title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles 


# In[40]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='txt-r3-n ng-binding']")
titles_tags


# In[41]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles 


# In[42]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='dura_md ng-binding']")
titles_tags


# In[43]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles 


# In[44]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='dura_md2 ng-scope']")
titles_tags


# In[45]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[46]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='txt-r3-n ng-binding']")
titles_tags


# In[47]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[48]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='col-md-8 col-sm-8 col-xs-9 txt-r6-n ng-binding']")
titles_tags


# In[49]:


# Now the text of the from title is inside the tags extracted above

# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[50]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[6]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[7]:


url = 'https://www.goibibo.com/flights/air-CCU-BLR-20211113--1-0-0-E-D/'
driver.get(url)
sleep(6)


# In[13]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='font13 padL5 black']")
titles_tags


# In[14]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[15]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='font12 grey']//span")
titles_tags


# In[16]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[17]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='srp-card-uistyles__DurTime-sc-3flq99-16 bjQlFP fb padT10']")
titles_tags


# In[18]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[19]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='font12 grey']")
titles_tags


# In[20]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[28]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='truncate font12 grey']")


# In[29]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[30]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='srp-card-uistyles__Price-sc-3flq99-17 gqEhhU alignItemsCenter dF fb lh1 padT5']")
titles_tags


# In[31]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[32]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[3]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[4]:


url = 'https://www.goibibo.com/flights/air-CCU-MAA-20211130--1-0-0-E-D/?gi_source=google&gi_medium=organic&campaign=organic&gocashoffer=true'
driver.get(url)
sleep(6)


# In[13]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='font13 padL5 black']")
titles_tags


# In[14]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[15]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='font12 grey']//span")
titles_tags


# In[16]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[17]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='srp-card-uistyles__DurTime-sc-3flq99-16 bjQlFP fb padT10']")
titles_tags


# In[18]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[19]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='font12 grey']")
titles_tags


# In[20]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[21]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='truncate font12 grey']//span")
titles_tags


# In[22]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[23]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='srp-card-uistyles__Price-sc-3flq99-17 gqEhhU alignItemsCenter dF fb lh1 padT5']")
titles_tags


# In[24]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[25]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[5]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[6]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=HYD&bdestination=HYD&destinationL=Hyderabad&destinationCity=&destinationCN=&source=CCU&bsource=CCU&sourceL=Kolkata&sourceCity=&sourceCN=&month=11&day=21&year=2021&date=11/21/2021&numAdults=1&numChildren=0&numInfants=0&isAjax=false'
driver.get(url)
sleep(6)


# In[32]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[33]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[34]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[35]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[36]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[37]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[38]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='stops']")
titles_tags


# In[39]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[40]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[41]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[42]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[43]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[44]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[3]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[4]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=JAI&bdestination=JAI&destinationL=Jaipur,Jaipur&destinationCity=Jaipur&destinationCN=India&source=CCU&bsource=CCU&sourceL=Kolkata&sourceCity=&sourceCN=&month=11&day=22&year=2021&date=11/22/2021&numAdults=1&numChildren=0&numInfants=0&validation_result=&domesinter=international&livequote=-1&flightClass=ALL&travType=DOM&routingType=ALL&preferredCarrier=&prefCarrier=0&isAjax=false'
driver.get(url)
sleep(6)


# In[5]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[6]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[7]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[8]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[9]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[10]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[11]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[12]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[13]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[14]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[15]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[16]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[20]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[3]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[4]:


url = 'https://in.via.com/flight-tickets/from-kolkata-to-mumbai'
driver.get(url)
sleep(6)


# In[63]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[64]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[65]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[66]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[67]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[68]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[69]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[70]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[71]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[72]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[73]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[74]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[75]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[3]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[4]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=AMD&bdestination=AMD&destinationL=Ahmedabad&destinationCity=&destinationCN=&source=CCU&bsource=CCU&sourceL=Kolkata&sourceCity=&sourceCN=&month=12&day=2&year=2021&date=12/2/2021&numAdults=1&numChildren=0&numInfants=0&isAjax=false'
driver.get(url)
sleep(6)


# In[78]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[79]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[80]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[81]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[82]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[83]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[84]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[85]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[86]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[87]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[88]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[89]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[90]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[5]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[6]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=LKO&bdestination=LKO&destinationL=Lucknow,Lucknow&destinationCity=Lucknow&destinationCN=India&source=CCU&bsource=CCU&sourceL=Kolkata&sourceCity=&sourceCN=&month=12&day=6&year=2021&date=12/6/2021&numAdults=1&numChildren=0&numInfants=0&validation_result=&domesinter=international&livequote=-1&flightClass=ALL&travType=INTL&routingType=ALL&preferredCarrier=ALL&prefCarrier=0&isAjax=false'
driver.get(url)
sleep(6)


# In[94]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[95]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[96]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[97]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[98]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[99]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[100]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[101]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[102]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[103]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[104]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[105]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[106]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[3]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[4]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=DEL&bdestination=DEL&destinationL=Delhi,Delhi&destinationCity=Delhi&destinationCN=India&source=BOM&bsource=BOM&sourceL=Mumbai,Mumbai&sourceCity=Mumbai&sourceCN=India&month=12&day=6&year=2021&date=12/6/2021&numAdults=1&numChildren=0&numInfants=0&validation_result=&domesinter=international&livequote=-1&flightClass=ALL&travType=INTL&routingType=ALL&preferredCarrier=ALL&prefCarrier=0&isAjax=false'
driver.get(url)
sleep(6)


# In[110]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[111]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[112]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[113]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[114]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[115]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[116]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[117]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[118]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[119]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[120]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[121]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[122]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[3]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[4]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=BLR&bdestination=BLR&destinationL=Bangalore&destinationCity=&destinationCN=&source=DEL&bsource=DEL&sourceL=Delhi&sourceCity=&sourceCN=&month=11&day=14&year=2021&date=11/14/2021&numAdults=1&numChildren=0&numInfants=0&isAjax=false'
driver.get(url)
sleep(6)


# In[126]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[127]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[128]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[129]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[130]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[131]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[132]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[133]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[134]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[135]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[136]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[137]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[138]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[3]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[4]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=MAA&bdestination=MAA&destinationL=Chennai,Chennai&destinationCity=Chennai&destinationCN=India&source=CCU&bsource=CCU&sourceL=Kolkata,Kolkata&sourceCity=Kolkata&sourceCN=India&month=11&day=26&year=2021&date=11/26/2021&numAdults=1&numChildren=0&numInfants=0&validation_result=&domesinter=international&livequote=-1&flightClass=ALL&travType=DOM&routingType=ALL&preferredCarrier=&prefCarrier=0&isAjax=false'
driver.get(url)
sleep(6)


# In[141]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[142]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[143]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[144]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[145]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[146]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[147]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[148]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[149]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[150]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[151]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[152]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[153]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[5]:


driver=webdriver.Chrome("chromedriver.exe") 
sleep(4)


# In[6]:


url = 'https://in.via.com/flight/search?returnType=one-way&destination=GAU&bdestination=GAU&destinationL=Guwahati,Guwahati(gauhati)&destinationCity=&destinationCN=India&source=CCU&bsource=CCU&sourceL=Kolkata&sourceCity=&sourceCN=&month=11&day=30&year=2021&date=11/30/2021&numAdults=1&numChildren=0&numInfants=0&validation_result=&domesinter=international&livequote=-1&flightClass=ALL&travType=DOM&routingType=ALL&preferredCarrier=&prefCarrier=0&isAjax=false'
driver.get(url)
sleep(6)


# In[156]:


# so lets extract all the tags having the flight-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='name js-toolTip']")
titles_tags


# In[157]:


# Now the text of the flight title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
flight_titles=[]
for i in titles_tags:
    flight_titles.append(i.text)
flight_titles


# In[158]:


# so lets extract all the tags having the from-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[159]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
from_titles=[]
for i in titles_tags:
    from_titles.append(i.text)
from_titles


# In[160]:


# so lets extract all the tags having the triptime-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='dur']")
titles_tags


# In[161]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
triptime_titles=[]
for i in titles_tags:
    triptime_titles.append(i.text)
triptime_titles


# In[162]:


# so lets extract all the tags having the layovers-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='route js-toolTip']")
titles_tags


# In[163]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
layover_titles=[]
for i in titles_tags:
    layover_titles.append(i.text)
layover_titles


# In[164]:


# so lets extract all the tags having the to-titles
titles_tags=driver.find_elements_by_xpath("//div[@class='city']")
titles_tags


# In[165]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
to_titles=[]
for i in titles_tags:
    to_titles.append(i.text)
to_titles


# In[166]:


# so lets extract all the tags having the price-titles
titles_tags=driver.find_elements_by_xpath("//span[@class='price']")
titles_tags


# In[167]:


# Now the text of the from title is inside the tags extracted above
# so we will run a loop to iterate over the tags extracted above and extract the text inside them.
price_titles=[]
for i in titles_tags:
    price_titles.append(i.text)
price_titles


# In[168]:


print(len(flight_titles),len(from_titles),len(triptime_titles),len(layover_titles),len(to_titles),len(price_titles))


# In[ ]:





# In[106]:


# importing libraries
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

sns.set()


# In[107]:


#uploading csv file
data = pd.read_csv(r"C:\Users\SAGNIK DAS\OneDrive\Desktop\New folder (3)\Flight Price .csv")
orgdata = data


# In[108]:


# understanding the data
data.head()


# In[109]:


data.shape


# In[110]:


data.tail()


# In[111]:


data.columns


# In[112]:


data['Flight'].value_counts()


# In[113]:


data['Departure_city'].value_counts()


# In[114]:


data['Layover'].value_counts()


# In[115]:


data['Destination_city'].value_counts()


# In[116]:


data['Date_of_journey'].value_counts()


# In[117]:


data['Duration'].value_counts()


# In[118]:


data['Price'].value_counts()


# In[119]:


data.dropna(inplace=True)


# In[120]:


data.isnull().sum()


# In[121]:


data.info()


# In[103]:


data['Date_of_journey'] = pd.to_datetime(data.Date_of_journey,format="%d/%m/%Y").dt.day


# In[104]:


data.Date_of_journey.head()


# In[124]:


data["Journey_day"] = pd.to_datetime(data.Date_of_journey,format="%d/%m/%Y").dt.day


# In[125]:


data.Date_of_journey.head()


# In[126]:


data["Journey_month"] = pd.to_datetime(data["Date_of_journey"],format="%d/%m/%Y").dt.month


# In[127]:


data.Journey_month.head()


# In[128]:


data.head()


# In[129]:


data.drop(["Date_of_journey"], axis = 1, inplace = True)


# In[130]:


data.head()


# In[161]:


duration = list(data["Duration"])


# In[166]:


for i in range(len("duration")):
    if len(duration[i].split()) !=2:
        if "h" in duration[i]:
            duration[i] = duration[i].strip() +"0m"
        else:    
            duration[i] = "0m" + duration[i]
            
duration_hours = []
duration_mins = []
for i in range (len(duration)):
    duration_hours.append(int(duration[i].split(sep="h")[0]))
    duration_hours.append(int(duration[i].split(sep="h")[0].split()[-1]))


# In[131]:


data_num = data.select_dtypes(include = ['float64', 'int64', 'object'])
data_num.head()


# In[132]:


data_num.hist(figsize=(18, 22), bins=55, xlabelsize=10, ylabelsize=10); 


# In[133]:


# importing required library
import seaborn as sns
import os
import csv
import sklearn
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import utils
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
plt.style.use('bmh')


# In[134]:


Price = pd.pivot_table(data,index = 'Journey_day', values='Price')


# In[135]:


Price


# In[136]:


Price.plot(kind='bar')


# In[138]:


Price = pd.pivot_table(data,index = 'Duration', values='Price')


# In[139]:


Price


# In[140]:


Price.plot(kind='bar')


# In[141]:


Price = pd.pivot_table(data,index = 'Journey_month', values='Price')


# In[142]:


Price


# In[143]:


Price.plot(kind='bar')


# In[144]:


Price = pd.pivot_table(data,index = 'Layover', values='Price')


# In[145]:


Price


# In[146]:


Price.plot(kind='bar')


# In[147]:


Price = pd.pivot_table(data,index = 'Flight', values='Price')


# In[148]:


Price


# In[149]:


Price.plot(kind='bar')


# In[150]:


Price = pd.pivot_table(data,index = 'Departure_city', values='Price')


# In[151]:


Price


# In[152]:


Price.plot(kind='bar')


# In[154]:


Price = pd.pivot_table(data,index = 'Destination_city', values='Price')


# In[155]:


Price


# In[156]:


Price.plot(kind='bar')


# In[157]:


corelation = data.corr() 


# In[158]:


sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns
            ,annot=True)


# In[159]:


sns.boxplot


# In[160]:


sns.pairplot


# In[167]:


y = np.array(data['Price'])
y.shape


# In[211]:


x = np.array(data.loc[:, 'Journey_day' : 'Journey_month'])
x.shape


# In[212]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,)


# In[213]:


x_train.shape


# In[214]:


x_test.shape


# In[215]:


y_train.shape


# In[216]:


y_test.shape


# In[217]:


from sklearn.model_selection import KFold
folds = (KFold(n_splits = 10, shuffle = True, random_state = 100))


# In[218]:


hyper_params = [{'n_features_to_select':list(range(1,5))}]


# In[219]:


from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x_train, y_train)


# In[220]:


from sklearn.feature_selection import RFE
rfe = RFE(lm)
from sklearn.model_selection import GridSearchCV
modelcv = GridSearchCV(estimator = rfe,
                      param_grid = hyper_params,
                      scoring = 'r2',
                      cv = folds,
                      verbose = 1,
                      return_train_score = True)
modelcv.fit(x_train, y_train)


# In[221]:


cvresults = pd.DataFrame(modelcv.cv_results_)
cvresults


# In[222]:


data.shape


# In[223]:


print(np.mean(cvresults))


# In[225]:


plt.figure(figsize = (20,7))


# In[226]:


plt.plot(cvresults['param_n_features_to_select'], cvresults['mean_test_score'])
plt.plot(cvresults['param_n_features_to_select'], cvresults['mean_train_score'])
plt.xlabel('Number of features')
plt.ylabel('Optimal number of features')


# In[227]:


n_features_optimal = 6


# In[228]:


lm = LinearRegression()
lm.fit(x_train, y_train)


# In[229]:


rfe = RFE(lm, n_features_to_select = n_features_optimal)


# In[230]:


rfe.fit(x_train, y_train)


# In[231]:


y_pred = lm.predict(x_test)
y_pred


# In[232]:


r2 = sklearn.metrics.r2_score(y_test, y_pred)
print(r2)


# In[ ]:




