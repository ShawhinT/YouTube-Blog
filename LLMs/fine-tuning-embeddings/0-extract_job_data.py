# Extraction Pipeline for AI Job Postings
# Code authored by: Shaw Talebi

import asyncio
from functions import scrape_jobs, scrape_job_details
import time
import csv

# define list of search queries
search_query_list = ["Data Scientist", "Data Analyst", "Machine Learning Engineer", "Data Engineer", "AI Engineer", "Deep Learning"]

# initialize list to store job details
job_details_list = []

# loop through each search query
for search_query in search_query_list:
    start_time = time.time()
    
    # extract 10 pages of job urls
    job_urls = asyncio.get_event_loop().run_until_complete(scrape_jobs(search_query, 10))
    
    # extract job details for each url
    for url in job_urls:
        job_details = scrape_job_details(url)
        if job_details:
                job_details['search_query'] = search_query
                job_details_list.append(job_details)
    
    end_time = time.time()
    print(f"Extract time for {search_query}: {end_time - start_time:.2f} seconds")
    print(len(job_details_list))
    print("-"*20)

# write to CSV file
with open("data/job_data.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(job_details_list[0].keys()))
    writer.writeheader()
    writer.writerows(job_details_list)
