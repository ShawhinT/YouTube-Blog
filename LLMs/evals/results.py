# Script to summarize the results of the evaluation

import os
import json
import csv

# Get list of folders in results/
folder_list = os.listdir("results/")

# keep only the folders that start with "0_real"
folder_list = [folder for folder in folder_list if folder.startswith("0_real")]

# loop through folder_list
prompt_performance_list = []
for folder in folder_list:
    # load the results
    with open(f"results/{folder}/{folder}_summary.json", "r") as f:
        results = json.load(f)

    # extract folder A name, average rouge score, and average win rate
    prompt_performance = {
        "prompt_name": results["folder_B"],
        "average_rouge_score": results["rouge_score_B"],
        "average_win_rate": results["win_rate_B_average"]
    }
    
    # add to prompt_performance_list
    prompt_performance_list.append(prompt_performance)

# sort the prompt_performance_list by prompt_name
prompt_performance_list.sort(key=lambda x: x["prompt_name"])

# write the prompt_performance_list to a .csv file
with open("results/prompt_performance.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["prompt_name", "average_rouge_score", "average_win_rate"])
    for prompt_performance in prompt_performance_list:
        writer.writerow([prompt_performance["prompt_name"], prompt_performance["average_rouge_score"], prompt_performance["average_win_rate"]])
