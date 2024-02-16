from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import logging

import requests
from lxml import html
from bs4 import BeautifulSoup

try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    import xml.etree.ElementTree as etree
    print("running with Python's xml.etree.ElementTree")

import base64
import time
import os

path="/home/jason/Documents/football_app/"
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

def get(driver,data,leauge,time_sleep):
    time_sleep+=1
    
    driver.get(data[leauge][0])
    # wait for all html content loaded
    time.sleep(time_sleep)

    # get the html content 
    html_content = driver.page_source

    # parse the content to the tree
    tree= html.document_fromstring(html_content)

    ##write the content to a local file
    # file_name="html_content.html"
    # with open(file_name, 'w') as file:
    #     file.write(html_content)

   
    return tree

def playball(leauge, picture_gen=False):

    # using gl=us to force the result getting from united states
    url_premier = "https://www.google.com/search?q=the+premier+league+standing&gl=us&sca_esv=31fe38a8fb03ee39&sxsrf=ACQVn0_Ingf4ChLSXVoCSxfqH5x1p31Rdw%3A1707893744939&ei=8GPMZdj3OIXp1e8P5eaqeA&ved=0ahUKEwjYr-z_n6qEAxWFdPUHHWWzCg8Q4dUDCBA&uact=5&oq=the+premier+league+standing&gs_lp=Egxnd3Mtd2l6LXNlcnAiG3RoZSBwcmVtaWVyIGxlYWd1ZSBzdGFuZGluZzIFEAAYgAQyBRAAGIAEMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkiUE1AlWPcRcAF4AZABAJgBiwGgAfIHqgEDMi43uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAg4QABjkAhjWBBiwA9gBAcICExAuGIAEGIoFGEMYyAMYsAPYAQLCAgUQLhiABMICCBAAGBYYHhgPwgILEAAYgAQYigUYhgPiAwQYACBBiAYBkAYQugYGCAEQARgJugYGCAIQARgI&sclient=gws-wiz-serp#sie=lg;/g/11sk7gnh6c;2;/m/02_tc;st;fp;1;;;"
    url_laliga="https://www.google.com/search?q=laliga&gl=us&oq=laliga&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgcIARAAGIAEMgcIAhAAGIAEMgkIAxAuGAoYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEC4YgAQyBwgHEAAYgAQyCQgIEAAYChiABDIHCAkQABiABNIBCTIxNjNqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11khrmf0s3;2;/m/09gqx;st;fp;1;;;"
    url_serieA="https://www.google.com/search?q=sery+a&gl=us&oq=sery+a&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQLhiABDIHCAYQLhiABDINCAcQLhivARjHARiABDIHCAgQABiABDIHCAkQABiABNIBCTIxOTVqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11kbz3nwd5;2;/m/03zv9;st;fp;1;;;"
    url_bundesliga="https://www.google.com/search?q=bundesliga&gl=us&oq=bundes&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyBwgBEC4YgAQyBwgCEC4YgAQyBggDEEUYOTIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABKgCALACAA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11t82pjxl9;2;/m/037169;st;fp;1;;;"

    # the number of teams
    num_premier=20
    num_laliga=20
    num_bundesliga=18
    num_serieA=20
    time_sleep=0
    # the dictionary for leauge data
    data={'premier':[url_premier,num_premier],'laliga':[url_laliga,num_laliga],'bundesliga':[url_bundesliga,num_bundesliga],'serieA':[url_serieA,num_serieA]}

    chrome_options = Options() # to stop the page showing everytime the func called
    chrome_options.add_argument("--headless")  # Enables headless mode
    chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    
    tree=get(driver,data,leauge,time_sleep)
    ##write the content to a local file
    # file_name="html_content.html"
    # with open(file_name, 'w') as file:
    #     file.write(html_content)

    # get the main div of the data
    success=False
    while not success:
        try:
            body=tree.getchildren()[1]
            # for item in body.getchildren():
            #     print(item.attrib)
            main=body.cssselect('.main')[0]
            
            success=True
        except IndexError:
            # driver.quit()
            # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            logging.info("main div loading")
            tree=get(driver,data,leauge,time_sleep) 
            
    
    
    success = False
    while not success:
        try:
            table=main.cssselect('.Jzru1c')[0]
            success=True
        except IndexError:
            # driver.quit()
            # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            logging.info("table div loading")
            tree=get(driver,data,leauge,time_sleep)
            body=tree.getchildren()[1]
            main=body.cssselect('.main')[0]
           
        
    # extract the data from the standing table on the page
    tbody=table.find('tbody')
    tr_list=tbody.findall('tr')
    td_list=[] 
    for i in range(len(tr_list)):
        td_list.append(tr_list[i].findall('td'))
        # print(tr_list[i].findall('td'))
        # print("\n")
    
    success = False
    while not success:
        try:
            for j in range(1,data[leauge][1]+1):
                td_list[j][2]=td_list[j][2]
            success=True
        except IndexError:
            # driver.quit()
            # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            logging.info("tr loading")
            tree=get(driver,data,leauge,time_sleep)
            body=tree.getchildren()[1]
            main=body.cssselect('.main')[0]
            table=main.cssselect('.Jzru1c')[0]
            tbody=table.find('tbody')
            tr_list=tbody.findall('tr')
            td_list=[] 
            for i in range(len(tr_list)):
                td_list.append(tr_list[i].findall('td'))
                # print(tr_list[i].findall('td'))
                # print("\n")
    name_list=[]
    win_list=[]
    lose_list=[]
    draw_list=[]
    pts_list=[]
    Last_list=[]
    match_list=[]
    
    # dealing with each tr
    for j in range(1,data[leauge][1]+1):
        
        # dealing with each td of trs   
        # td 2 : for name
        name=td_list[j][2].getchildren()[0].getchildren()[0].getchildren()[0]
        # print(name.text)
        name_list.append(name.text)
        
        # td 3 : for match
        match=td_list[j][3].getchildren()[0]
        # print(match.text)
        match_list.append(match.text)

        # td 4 : for W
        win=td_list[j][4].getchildren()[0]
        # print(win.text)
        win_list.append(win.text)
        
        # td 5 : for D
        draw=td_list[j][5].getchildren()[0]
        # print(draw.text)
        draw_list.append(draw.text)
            
        # td 6 : for L 
        lose=td_list[j][6].getchildren()[0]
        # print(lose.text)
        lose_list.append(lose.text)

        # td 10 : for pts
        pts=td_list[j][10].getchildren()[0]
        # print(pts.text)
        pts_list.append(pts.text)
        
        # td 11 : for Last5
        Last=[]
        Last5=td_list[j][11].cssselect('.YCyuEf')
        for i in range(5):
            Last.append(Last5[i].text)
        Last_list.append(Last)
        # print(Last)
        
        # td 11 : for W,L,D icon
        # file_path = "./icon"+"/"++"_"+name+".png"
        icon=td_list[j][11].cssselect('.BPu3kf')
        w_path=path+"icon/l5l-w.svg"
        l_path=path+"icon/l5l-l.svg"
        d_path=path+"icon/l5l-t.svg"
        
        for item in icon:
            if  not (os.path.exists(w_path) and os.path.exists(l_path) and os.path.exists(d_path)):
                icondata=item.getchildren()[0].attrib['src']
                # print(icondata)
                img = base64.b64decode(icondata[26:])
                # print(img)
                with open(path+"icon/"+item.attrib['aria-labelledby']+".svg","wb") as file:
                    file.write(img)
            else :
                break
        # td 1 : for img
        if(picture_gen):
            file_path = path+leauge+"/"+leauge+"_"+name.text+".png"
            if not os.path.exists(file_path):
                imgdata=td_list[j][1].findall('div')[2].find('span').find('img').attrib['src']
                response=requests.get("https:"+imgdata)
                # print(response.content)
                # print("\n")
                # img = base64.b64decode(response.content)
                with open(path+leauge+"/"+leauge+"_"+name.text+".png", "wb") as file:
                    # Write the content of the response to the file
                    file.write(response.content)
        
    driver.quit()
    standing={'name':name_list,'match':match_list,'lose':lose_list,'win':win_list,'pts':pts_list,'last':Last_list,'draw':draw_list}
    return standing

result=playball('laliga',picture_gen=True)
