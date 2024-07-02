from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import cache as cacheManager
import time

def getUsername(link):
    i = link.find("u/")
    username = link[i+2:]
    return username.replace("/","")

def getDifficulty(problemTitle):

    # Check difficulty in cache
    cacheManager.initIfNot()
    if(cacheManager.checkCache(problemTitle)):
        return cacheManager.getCache(problemTitle)

    try:
        response = json.loads(requests.get("https://alfa-leetcode-api.onrender.com/select?titleSlug={}".format(problemTitle)).content)
        # time.sleep(5)
        response = response['difficulty']
        cacheManager.addCache(problemTitle,response)
    except:
        response = "Null"
    finally:
        return response


def getProblems(link):
    username = getUsername(link)

    print("Fetching for username:",username)

    response = json.loads(requests.get("https://alfa-leetcode-api.onrender.com/{}/acSubmission".format(username)).content)

    submissionList = response['submission']

    submissionByDate = {}    

    for submission in submissionList:
        dt = datetime.fromtimestamp(int(submission['timestamp']))
        
        submission['difficulty'] = getDifficulty(submission['titleSlug'])

        if(dt.date() not in submissionByDate.keys()):
            submissionByDate[dt.date()] = [submission]
        else:
            submissionByDate[dt.date()].append(submission)

    return submissionByDate


def getProblems_old(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    f = open("./soup.html","w+")
    f.write(soup.text)
    f.close()
    
    table = soup.find('div', recursive=True,attrs = {'class':'flex flex-col'})
    if(table == None):
        print("Could not find problems table in link")
        # return
    print("Table:",table)

    problems = soup.findAll('a',recursive=True)
    if(problems == None):
        print("No problems in link")
        return
    print("Problems:",problems)

    for row in problems:
        print(row['href'])

    pass

def print_problems_solved(link):
    problems=getProblems(link)
    for date in problems:
        print(date)
        for problem in problems[date]:
            print(problem["title"],problem['difficulty'])
        print("\n")

link = "https://leetcode.com/u/SUGANTH_47/"
print_problems_solved(link)