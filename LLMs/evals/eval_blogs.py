# Script to compate blogs by an LLM judge

import openai
import os
import dotenv
import re
import json
import csv
from rouge_score import rouge_scorer

# import openai api key from .env file
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# functions
def evaluate_blog_pair(blog_post_A, blog_post_B, transcript_text):
    """
    Evaluates two blog posts against a YouTube video transcript using an LLM.

    Parameters:
    - blog_post_A (str): The content of the first blog post.
    - blog_post_B (str): The content of the second blog post.
    - transcript_text (str): The transcript of the YouTube video.

    Returns:
    - tuple: A tuple containing (answer, response) where:
      - answer (str): The chosen blog post ('A' or 'B')
      - response (str): The full response from the LLM.
    """
    prompt = prompt_template.format(
        blog_post_A=blog_post_A,
        blog_post_B=blog_post_B,
        transcript=transcript_text
    )

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    answer = re.search(r'<answer>(.*?)</answer>', response.choices[0].message.content).group(1)

    return answer, response.choices[0].message.content

def read_text_file(folder_path, filename):
    """
    Reads a text file from a specified folder and returns its contents.

    Parameters:
    - folder_path (str): The path to the folder containing the text file.
    - filename (str): The name of the text file to read.

    Returns:
    - str: The contents of the text file as a string.

    Raises:
    - FileNotFoundError: If the specified file cannot be found.
    - IOError: If there is an error reading the file.
    
    Example:
    >>> content = read_text_file("data/blogs", "sample_post.txt")
    >>> print(content[:50])  # Print first 50 characters
    """
    try:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
        return text_content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")

def compute_rouge_scores(blog_text, transcript_text):
    """
    Computes ROUGE scores between a blog post and a reference transcript using Google's rouge-score library.
    
    Parameters:
    - blog_text (str): The content of the blog post
    - transcript_text (str): The reference transcript text
    
    Returns:
    - dict: Dictionary containing ROUGE-1, ROUGE-2, and ROUGE-L scores
            Each score includes precision, recall, and f1-measure
    """
    try:
        # Initialize scorer with ROUGE-1, ROUGE-2, and ROUGE-L
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
        
        # Calculate scores
        scores = scorer.score(transcript_text, blog_text)
        
        # Format scores to match the existing structure
        return {
            'rouge-1': {
                'p': scores['rouge1'].precision,
                'r': scores['rouge1'].recall,
                'f': scores['rouge1'].fmeasure
            },
            'rouge-2': {
                'p': scores['rouge2'].precision,
                'r': scores['rouge2'].recall,
                'f': scores['rouge2'].fmeasure
            },
            'rouge-l': {
                'p': scores['rougeL'].precision,
                'r': scores['rougeL'].recall,
                'f': scores['rougeL'].fmeasure
            }
        }
    except Exception as e:
        print(f"Error computing ROUGE scores: {e}")
        return {
            'rouge-1': {'f': 0.0, 'p': 0.0, 'r': 0.0},
            'rouge-2': {'f': 0.0, 'p': 0.0, 'r': 0.0},
            'rouge-l': {'f': 0.0, 'p': 0.0, 'r': 0.0}
        }

def evaluate_blog_pair_batch(foldername_A, foldername_B):
    """
    Evaluates pairs of blog posts from two folders against YouTube video transcripts.
    
    Parameters:
    - foldername_A (str): Path to the first folder containing blog posts
    - foldername_B (str): Path to the second folder containing blog posts
    
    Returns:
    - list: A list of dictionaries containing evaluation results for each blog pair
    """
    # get list of blog posts filenames
    filelist_A = os.listdir(foldername_A)
    filelist_B = os.listdir(foldername_B)
    
    # loop through blog posts and evaluate
    eval_list = []
    for i in range(len(filelist_A)):
        print(f"Evaluating blog post {i+1} / {len(filelist_A)}")
    
        # extract number and video id from filename
        match = re.match(r'(\d+)-(.+)\..*', filelist_A[i])
        index, video_id = int(match.group(1)), match.group(2)
    
        # read transcript
        transcript_text = read_text_file("transcripts", f"{index}-{video_id}.txt")
        # read blog post A
        blog_post_A = read_text_file(foldername_A, filelist_A[i])
        # read blog post B
        blog_post_B = read_text_file(foldername_B, filelist_B[i])
    
        # evaluate blogs
        answer, response = evaluate_blog_pair(blog_post_A, blog_post_B, transcript_text)
    
        # evaluate blogs in reverse order
        answer_swapped, response_swapped = evaluate_blog_pair(blog_post_B, blog_post_A, transcript_text)
        # Swap the answer values in eval_dict_swapped
        if answer_swapped == "A":
            answer_swapped = "B"
        elif answer_swapped == "B":
            answer_swapped = "A"
        
        # Compute ROUGE scores for both blog posts
        rouge_scores_A = compute_rouge_scores(blog_post_A, transcript_text)
        rouge_scores_B = compute_rouge_scores(blog_post_B, transcript_text)
        
        # add swapped answer to eval_dict
        eval_dict = {
            "index": index,
            "video_id": video_id,
            "answer": answer,
            "response": response,
            "answer_swapped": answer_swapped,
            "response_swapped": response_swapped,
            "rouge_scores_A": rouge_scores_A,
            "rouge_scores_B": rouge_scores_B
        }
    
        # add to eval list
        eval_list.append(eval_dict)

    # compute win rates
    win_rate_A = sum([1 for x in eval_list if x["answer"] == "A"]) / len(eval_list)
    win_rate_A_swapped = sum([1 for x in eval_list if x["answer_swapped"] == "A"]) / len(eval_list)
    win_rate_A_average = (win_rate_A + win_rate_A_swapped) / 2
    
    # Calculate average ROUGE-L F1 scores for A and B
    rouge_average_A = sum(x['rouge_scores_A']['rouge-l']['f'] for x in eval_list) / len(eval_list)
    rouge_average_B = sum(x['rouge_scores_B']['rouge-l']['f'] for x in eval_list) / len(eval_list)

    summary_stats = {
        "total_evaluations": len(eval_list),
        "folder_A": foldername_A.split('/')[-1],
        "folder_B": foldername_B.split('/')[-1],
        "win_rate_A": win_rate_A,
        "win_rate_A_swapped": win_rate_A_swapped,
        "win_rate_A_average": win_rate_A_average,
        "win_rate_B": 1 - win_rate_A,
        "win_rate_B_swapped": 1 - win_rate_A_swapped,
        "win_rate_B_average": 1 - win_rate_A_average,
        "agreement_rate": sum([1 for x in eval_list if x["answer"] == x["answer_swapped"]]) / len(eval_list),
        "rouge_score_A": rouge_average_A,
        "rouge_score_B": rouge_average_B
    }
    
    # Create folder name based on the comparison
    folder_name = f"{foldername_A.split('/')[-1]}-{foldername_B.split('/')[-1]}"
    folder_path = os.path.join("results", folder_name)
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # save eval list to json
    json_filename = os.path.join(folder_path, f"{folder_name}.json")
    with open(json_filename, "w") as f:
        json.dump(eval_list, f)
        
    # save summary statistics to json
    summary_filename = os.path.join(folder_path, f"{folder_name}_summary.json")
    with open(summary_filename, "w") as f:
        json.dump(summary_stats, f, indent=4)

    # save eval list to csv
    csv_filename = os.path.join(folder_path, f"{folder_name}.csv")
    with open(csv_filename, "w", newline='', encoding='utf-8') as f:
        fieldnames = ["index", "video_id", "winner", "winner_swapped", 
                     "rouge_l_f1_A", "rouge_l_f1_B"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in eval_list:
            row = {
                "index": item["index"],
                "video_id": item["video_id"],
                "winner": item["answer"],
                "winner_swapped": item["answer_swapped"],
                "rouge_l_f1_A": item["rouge_scores_A"]["rouge-l"]["f"],
                "rouge_l_f1_B": item["rouge_scores_B"]["rouge-l"]["f"]
            }
            writer.writerow(row)

    print(f"Saved evaluation results to {folder_path}")
    
    return summary_stats, eval_list

# load prompt template
with open("prompt-templates/0_gpt_judge.txt", "r") as file:
    prompt_template = file.read()

# Example usage
if __name__ == "__main__":
    foldername_A = "blogs/3_gpt"
    foldername_B = "blogs/4_gpt"

    evaluate_blog_pair_batch(foldername_A, foldername_B)

    # foldername_tuple_list = [("0_real", "1_gpt"), ("0_real", "2_gpt"), ("0_real", "3_gpt"), ("1_gpt", "2_gpt"), ("2_gpt", "3_gpt")]
    
    # for foldername_tuple in foldername_tuple_list:
    #     foldername_A = f"blogs/{foldername_tuple[0]}"
    #     foldername_B = f"blogs/{foldername_tuple[1]}"
    #     evaluate_blog_pair_batch(foldername_A, foldername_B)