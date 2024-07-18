import pandas as pd
import scraper as Scraper
from datetime import datetime, timedelta
import os, sys, argparse

# Define file paths
DB_PATH = "./Student_db.csv"
OUTPUT_PATH = "./leetcode_stats.csv"
CACHE = "./cache.txt"

# Function to process the statistics
def process_stats(val, name, date):
    if val:
        # Create a DataFrame with the provided stats
        df = pd.DataFrame(val, index=[name])
        df.columns = pd.MultiIndex.from_product([[date], df.columns])
    else:
        # Create a DataFrame with default values if no stats are provided
        df = pd.DataFrame({(date, 'Easy'): 0, (date, 'Medium'): 0, (date, 'Hard'): 0}, index=[name])
    return df

# Function to fetch statistics
def fetch_stats(date):
    df = pd.read_csv(DB_PATH)
    
    # Ensure the cache file exists
    if not os.path.isfile(CACHE):
        with open(CACHE, 'w') as op:
            pass

    stats = []
    # Iterate through each student in the database
    for index, row in df.iterrows():
        problems_by_date = Scraper.getProblems(row['Leetcode ID'])
        val = problems_by_date.get(date)
        # Process the stats for each student
        stats.append(process_stats(val, row['Name'], date))
    
    # Concatenate all student stats into a single DataFrame
    df2 = pd.concat(stats, axis=0)

    # If the output file exists, read it and concatenate with the new stats
    if os.path.isfile(OUTPUT_PATH):
        existing_df = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=0)
        df2 = pd.concat([df2, existing_df], axis=1)
    
    # Save the updated stats to the output file
    df2.to_csv(OUTPUT_PATH)
    print(df2)

# Main function to parse arguments and execute the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output File")
    parser.add_argument("-i", "--input", help="Input File")
    args = parser.parse_args()

    # Print help message if no arguments are provided
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    # Update the output file path if provided
    if args.output:
        OUTPUT_PATH = args.output
    
    # Update the input file path if provided and validate its existence
    if args.input:
        DB_PATH = args.input
        if not os.path.isfile(DB_PATH):
            print("Invalid input")
            sys.exit(1)

    # Get the current date
    date = datetime.now().date()
    print("Fetching for date:", date)
    
    # Ensure the cache file exists
    if not os.path.isfile(CACHE):
        open(CACHE, 'w').close()
    
    # Fetch and process the stats
    fetch_stats(date)
