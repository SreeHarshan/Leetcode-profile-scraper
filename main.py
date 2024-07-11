import pandas as pd 
import scraper as Scraper
from datetime import datetime

CSV_PATH = "./input.csv"
OUTPUT_PATH = "./output.csv"

def fetch_stats(date):
    df = pd.read_csv(CSV_PATH)
    f= False
    print(df.columns)

    problems = []

    for index, row in df.iterrows():
        problems_byDate = Scraper.getProblems(row['Leetcode ID'])
        df2 = pd.DataFrame(problems_byDate)
        problems.append(df2)
    df['Problems'] = problems

    df.to_csv(OUTPUT_PATH,index=False)


if __name__ == "__main__":

    date = datetime.now().date()
    print("Fetching for date:",date)

    fetch_stats(date)
