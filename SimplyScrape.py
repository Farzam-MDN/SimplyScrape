from bs4 import BeautifulSoup, Comment
import lxml
from lxml import html
import os
import requests
import webbrowser
import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from datetime import datetime


global chrome_path
chrome_path  = "chromedriver.exe"
global  driver


global soup
global scrapename
global scrapeurl

scrapename = input('The scrape name?')
scrapeurl = input('The scrape url?')



def scrapeit():
        global driver
        global soup
        r = requests.get(scrapeurl)

        soup = BeautifulSoup(r.content, 'lxml')


        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y,%Hh%Mm%Ss")
        filename = scrapename + '(' + date_time + ')' + ".html"
        f = open(filename, "w", encoding='utf-8')
        f.write(soup.prettify())
        f.close()
        print('results saved in: ' +  filename)
        print('Opening the html file..')

        path = os.getcwd()
        pathtofilefornotepad =  path + '/' + filename
        webbrowser.open(pathtofilefornotepad , new=2)

        driver.get("file://" + pathtofilefornotepad)
        driver.execute_script("window.stop();")




def useresults():
        global soup
        global scrapename
        global scrapeurl
        spanresults = []
        divresults = []
        atagresults = []
        anyelementresults = []


        #create the scrapecode text file
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y, %Hh%Mm%Ss")
        filename = 'Scrapecode-' + scrapename + '(' + date_time + ')' + ".txt"
        f = open(filename, "w", encoding='utf-8')
        print('scrapecode will be saved in: ' +  filename)

        fs = open('sample-scrapecode.txt', mode='r', encoding='utf-8')
        all_of_it = fs.read()




        spaninput = input('Give class of a span element on the page:')
        allspanresults = soup.find_all('span', class_ = spaninput)


        for result in allspanresults:
            spanresults.append(result.getText())

        print(spanresults)


        divinput = input('Give class of a div element on the page:')
        alldivresults = soup.find_all('div', class_ = divinput)



        for result in alldivresults:
            divresults.append(result.getText())

        print(divresults)






        classinput = input('Give class of any element on the page:')
        anyelementresults = soup.find_all("html_element", class_=classinput)

        for result in anyelementresults:
            anyelementresults.append(result.getText())

        print(anyelementresults)

        scrapeurlfile = 'scrapeurl = ' + " '" + scrapeurl + "' "
        spaninputfile = 'spaninput = ' + " '" + spaninput + "' "
        divinputfile = 'divinput = ' + " '" + divinput + "' "
        classinputfile = 'classinput = ' + " '" + classinput + "' "


        charcount = 0
        for char in all_of_it:
            charcount = charcount + 1

            if charcount == 222:
                f.write('\n')
                f.write(scrapeurlfile + ' \n')
                f.write(spaninputfile + '\n')
                f.write(divinputfile + '\n')
                f.write(classinputfile + '\n')

            else:
                f.write(char)

        f.close()
        fs.close()

        print('scrapecode is saved.')
        print('Opening scrapecode..')
        path = os.getcwd()
        pathtofilefornotepad =  path + '/' + filename
        webbrowser.open(pathtofilefornotepad , new=2)


def StartApp():
    global driver
    driver = webdriver.Chrome(chrome_path)
    scrapeit()
    useresults()

#program
StartApp()