from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

path="/home/jason/Documents/py/football_app/"
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

def get(driver,data,leauge,time_sleep):
    time_sleep+=1
    
    driver.get(data[leauge][0])
    time.sleep(time_sleep)
    element=driver.find_elements(By.CSS_SELECTOR,'.tb_h.ie7Asb.AAhKnb.TbbqEc.YPgUJe.B27Eaf')
    # print(element)
    elements_click = element[0].find_elements(By.CSS_SELECTOR, '.imso-hide-overflow.tb_l.GSkImd')
    # print(elements_click)
    
    elements_click[2].click()
    # wait for all html content loaded
    time.sleep(1)
    # get the html content 
    html_content = driver.page_source
    # html_content=requests.get(data[leauge][0]).content
    
    # parse the content to the tree
    tree= html.document_fromstring(html_content)
    
    ##write the content to a local file
    # file_name="html_content.html"
    # with open(file_name, 'w') as file:
    #     file.write(html_content)

   
    return tree

def playball(leauge, picture_gen=False):

    # using gl=us to force the result getting from united states
    url_premier = "https://www.google.com/search?q=premier+league&oq=&gl=us&gs_lcrp=EgZjaHJvbWUqCQgAEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIJCAMQRRg7GMIDMgkIBBBFGDsYwgMyCQgFEEUYOxjCAzIJCAYQRRg7GMIDMgkIBxBFGDsYwgPSAQg3OTlqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8"
    url_laliga="https://www.google.com/search?q=laliga&gl=us&oq=la&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBwgCEAAYgAQyDQgDEC4YxwEY0QMYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEC4YgAQyBwgHEAAYgAQyCggIEC4Y1AIYgAQyCggJEC4Y1AIYgATSAQkxNjYyajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8"
    url_serieA="https://www.google.com/search?q=serie+A&gl=us&sca_esv=f5f2bc2e5380d47d&hl=en&sxsrf=ACQVn08EqItNmReNuXvs6FofpMgV9KocZg%3A1708053961125&source=hp&ei=ydXOZfmBBe23vr0PzO-quAY&iflsig=ANes7DEAAAAAZc7j2XOf7-S00r_T3YYLYj7ZT201aWm3&ved=0ahUKEwi5iu7s9K6EAxXtm68BHcy3CmcQ4dUDCA0&uact=5&oq=serie+A&gs_lp=Egdnd3Mtd2l6IgdzZXJpZSBBMgUQLhiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAuGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjjHFAAWLUacAF4AJABAJgBlQGgAdMHqgEDMy41uAEDyAEA-AEBwgILEC4YgAQYxwEY0QPCAggQLhiABBjUAg&sclient=gws-wiz"
    url_bundesliga="https://www.google.com/search?q=bundesliga&gl=us&sca_esv=f5f2bc2e5380d47d&hl=en&sxsrf=ACQVn0_MvIMD8Zh3aIjBVYVvqwd3pVJamw%3A1708055561681&source=hp&ei=CdzOZcmfJvfn2roP-rCfqAE&iflsig=ANes7DEAAAAAZc7qGYHpLDhcIOYLQOe02Sa3aYBIEe0r&oq=bunde&gs_lp=Egdnd3Mtd2l6IgVidW5kZSoCCAAyBRAuGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQLhiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESMgMUABYgAVwAHgAkAEAmAF7oAG-BKoBAzAuNbgBA8gBAPgBAcICCxAuGIAEGMcBGNED&sclient=gws-wiz"

    # the number of teams
    num_premier=20
    num_laliga=20
    num_bundesliga=18
    num_serieA=20
    time_sleep=1
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
            driver.quit()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
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
            driver.quit()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
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

# result=playball('laliga',picture_gen=True)
