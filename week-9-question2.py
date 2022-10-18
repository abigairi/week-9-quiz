from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Scrap Hacker News'
print(excel.sheetnames)
sheet.append(['rank', 'title', 'link'])

url= "https://news.ycombinator.com/"
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.content, 'html.parser')
lists =soup.find_all('tr', class_="athing")


for list in lists:
            rank = list.find('td', class_="title").span.text
            title = list.find('span', class_="titleline").a.text
            link = list.find('span', class_="titleline").find("a").get("href")
            #points = list.find_all('span', class_="score", id_="score_33229526")
            #comments = list.find('span', class_="age")
            #Author = list.find('span', class_="score").a.text

            
            print(rank, title, link)

            sheet.append([rank, title, link])



            excel.save('Scrap Hacker News.xlsx')
            



