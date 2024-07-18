import pandas as pd
import scraper as Scraper
from datetime import datetime, timedelta
import os,sys,argparse

DB_PATH = "./Student_db.csv"
OUTPUT_PATH = "./leetcode_stats.csv"
CACHE = "./cache.txt"

def fetch_stats(date):
    df = pd.read_csv(DB_PATH)
    if not os.path.isfile(CACHE):
        with open('cache.txt','w') as op:
            pass
    stats = []
    for index, row in df.iterrows():
        problems_by_date = Scraper.getProblems(row['Leetcode ID'])
        val = problems_by_date.get(date)
        stats.append(process_stats(val, row['Name'], date))
    
    df2 = pd.concat(stats, axis=0)
    if not os.path.isfile(OUTPUT_PATH):
        df2.to_csv(OUTPUT_PATH)
    else:
        df1 = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=[0])
        if date in df1:
            df1.update(df2)
        else:
            df1=pd.merge(df2,df1,left_index=True,right_index=True)
        df1.to_csv(OUTPUT_PATH)             
    print(pd.read_csv(OUTPUT_PATH))

def process_stats(val, name, date):
    t = pd.DataFrame(val if val else {'Easy': 0, 'Medium': 0, 'Hard': 0}, index=[0])
    t['date'] = date
    t['Name'] = name
    melted_df = pd.melt(t, id_vars=['date', 'Name'], var_name='level', value_name='count')
    pivot_df = pd.pivot_table(melted_df, columns=['date', 'level'], index='Name', values='count', aggfunc='sum')
    return pivot_df

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help = "Output File")
    parser.add_argument("-i", "--input", help = "Input File")
    args = parser.parse_args()


    if(len(sys.argv)<=1):
        parser.print_help()
        sys.exit(1)

    if args.output:
        OUTPUT_PATH = args.output
    
    if args.input:
        DB_PATH = args.input

        if(not os.path.isfile(DB_PATH)):
            print("Invalid input")
            sys.exit(1)

    date = datetime.now().date()
    print("Fetching for date:", date)
    fetch_stats(date)