import requests
from bs4 import BeautifulSoup
import csv

date = input("donnez moi le date sur cette forme MM/DD/YYYY:")
link = requests.get(f"https://www.yallakora.com/Match-Center?date={date}")
def main (link):
    src = link.content
    soup = BeautifulSoup(src,"lxml")
    matchesDetails = []
    championships = soup.find_all("div",{'class':'matchCard'})
    def get_match_info(championships) :
        championTitle = championships.contents[1].find("h2").text.strip()
        allMatches = championships.contents[3].find_all("div",{'class':'item finish liItem'})
        numbreOfMatches = len(allMatches)
        print (numbreOfMatches)
        for i in range(numbreOfMatches) :
            #get teamA 
            teamA = allMatches[i].find("div",{'class':'teamA'}).text.strip()
            teamB = allMatches[i].find("div",{'class':'teamB'}).text.strip()
            #get score
            matchResult = allMatches[i].find("div",{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f"{matchResult[0].text.strip()} - {matchResult[1].text.strip()}"
            #get time 
            matchTime = allMatches[i].find("div",{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
            #add match info to matches Details
            matchesDetails.append({"titre de championnat":championTitle,"équipe A": teamA,"équipe B": teamB, "temps":matchTime,"le score": score})
    
    for i in range(len(championships)) :
        get_match_info(championships[i])

    keys = matchesDetails[0].keys()
    with open("c:/Users/ouali/Desktop/matches.csv", "w", newline="", encoding="utf-8-sig") as outputFile :
        dict_writer = csv.DictWriter(outputFile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matchesDetails)
        print("la creation de ficher avec succésse")

main(link)
