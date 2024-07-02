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
        response = response['difficulty']
        cacheManager.addCache(problemTitle,response)
    except:
        response = "Null"
    finally:
        return response


def getProblems(link):
    username = getUsername(link)

    print("Fetching for username:",username)

    response = requests.get("https://alfa-leetcode-api.onrender.com/{}/acSubmission".format(username)).content
    try:
        response = json.loads(response)
    except:
        print("Unable to scrape profile")
        return {}

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

def print_problems_solved(link):
    problems=getProblems(link)
    for date in problems:
        print(date)
        for problem in problems[date]:
            print(problem["title"],problem['difficulty'])
        print("\n")

link = "https://leetcode.com/u/sreeerode12/"
print_problems_solved(link)