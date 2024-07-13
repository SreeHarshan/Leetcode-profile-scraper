# Leetcode Profile Scraper

## Objective:

To develop an automated tool that extracts daily LeetCode problem-solving statistics for a group of students and compiles the data into an Excel spreadsheet for easy tracking and analysis.

## Key Features:

- **User Profile Scraping:** Ability to scrape LeetCode profiles for multiple users.
- **Daily Data Extraction:** Extract the number of questions solved per day, categorized by difficulty level (Easy, Medium, Hard).
- **Batch Processing:** Handle multiple student profiles in a single run.
- **Data Storage:** Store extracted data in a structured format (Excel spreadsheet).
- **Automated Scheduling:** Run the scraper daily to keep track of progress over time.

## Technical Components:

- **Web Scraping:** Use libraries like requests and BeautifulSoup to extract data from LeetCode profiles.
- **Data Processing:** Utilize pandas for data manipulation and storage.
- **Excel Integration:** Employ libraries like openpyxl or xlsxwriter for creating and updating Excel files.
- **Scheduling:** Implement a scheduling mechanism for daily execution.

## Input and Output
### Input:

```
-> A list of LeetCode usernames for the students to be tracked.
```

### Output:

An Excel spreadsheet containing:

```
-> Student usernames
-> Date of data collection
-> Number of Easy, Medium, and Hard problems solved that day
-> Cumulative totals for each difficulty level
```


## To-Do list:

- **Data Visualization:** Generate graphs or charts to visualize progress over time.
- **Email Notifications:** Send daily or weekly summary reports to students or instructors.
- **Web Interface:** Create a simple web dashboard for viewing and analyzing the data.
- **Error Handling:** Implement robust error handling for network issues or profile changes.
