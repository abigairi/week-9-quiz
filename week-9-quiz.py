from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Best movies since 1980'
print(excel.sheetnames)
sheet.append(['rank','title','year','rating','metascore','runtime','genre'])

url= "https://www.imdb.com/list/ls000855851/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists =soup.find_all('div', class_="lister-list")


for list in lists:
            rank = list.find('div', class_="lister-item-content").span.text
            title = list.find('div', class_="lister-item-content").a.text
            year = list.find('span', class_="lister-item-year text-muted unbold").text
            rating = list.find('span', class_="ipl-rating-star small")
            metascore = list.find('div', class_="inline-block ratings-metascore").span.text
            #votes = list.find('p', class_="text-muted")
            #gross = list.find('span', class_="text-muted")
            #directors = list.find_all('a')
            #actors = list.find('a', class_="")
            runtime = list.find('span', class_="runtime").text
            genre = list.find('span', class_="genre").text
            #description = list.find('a', class_="")
            

            print(rank,title,year,rating,metascore,runtime,genre)
            sheet.append ([rank, title, year, rating, metascore, runtime, genre])

            excel.save('Movie imdb.xlsx')

            

            
