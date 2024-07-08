import pandas as pd 
import scraper as Scraper
from datetime import datetime

CSV_PATH = "./input.csv"
OUTPUT_PATH = "./output.csv"

def fetch_stats(date):
    df = pd.read_csv(CSV_PATH)

    print(df.columns)

    problems = []

    for index, row in df.iterrows():
        if(row['Leetcode ID'] == 'VIGNESH R'):
            break
        problems_byDate = Scraper.getProblems(row['Leetcode ID'])
        if(date in problems_byDate):
            problems.append(problems_byDate[date])
        else:
            problems.append([])
    df['Problems'] = problems

    df.to_csv(OUTPUT_PATH)


if __name__ == "__main__":

    date = datetime.now().date()
    print("Fetching for date:",date)

    fetch_stats(date)
