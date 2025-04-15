# Functions for profile writer

import re
import textstat
import os

def read_context(filename):
    with open(f"context/{filename}", 'r', encoding='utf-8') as file:
        return file.read()
    
def write_profile(profile_text: str, filename: str) -> None:
    """
    Writes a profile text to a file in the profiles/ directory.

    Args:
        profile_text (str): The text content to write to the file
        filename (str): Name of the file (without .txt extension)

    Returns:
        None
    """
    
    # Create the full file path
    filepath = os.path.join('profiles', filename)
    
    # Write the profile text to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(profile_text)

    
def word_count_eval(lower_bound, upper_bound, text):
    """
    Evaluates if a text's word count falls within a specified range.

    Args:
        lower_bound (int): The minimum acceptable word count (inclusive)
        upper_bound (int): The maximum acceptable word count (inclusive)
        text (str): The text to evaluate

    Returns:
        bool: True if the word count is within the specified range, False otherwise
    """
    word_count = len(text.split())
    return True if lower_bound <= word_count <= upper_bound else False

def client_focus_eval(threshold, text):
    """
    Evaluates if a text has sufficient client-focused language by counting "you" and "your" mentions.

    Args:
        threshold (int): The minimum required combined count of "you" and "your" mentions
        text (str): The text to evaluate

    Returns:
        bool: True if the combined count of "you" and "your" meets or exceeds the threshold, False otherwise
    """
    you_mentions = text.lower().count("you")
    your_mentions = text.lower().count("your")
    return True if (you_mentions + your_mentions) >= threshold else False

def social_proof_eval(text):
    """
    Evaluates if a text contains social proof indicators.

    Args:
        text (str): The text to evaluate

    Returns:
        bool: True if the text contains social proof indicators, False otherwise
    """
    has_dollar_figures = bool(re.search(r"\$\d+[MK]?", text))
    has_testimonial_quotes = '"' in text or "“" in text
    return True if has_dollar_figures or has_testimonial_quotes else False

def clean_text_for_readability(text):
    # Remove emojis and markdown-like syntax
    text = re.sub(r'[^\w\s.,!?]', '', text)  # basic emoji/markdown cleaner
    return text

def readability_eval(text: str, target_grade: int = 9) -> bool:
    """
    Evaluates if a text's Flesch-Kincaid grade level is at or below the target grade.

    Args:
        target_grade (int, optional): The maximum acceptable grade level. Defaults to 9.
        text (str): The text to evaluate

    Returns:
        bool: True if the text's grade level is at or below the target grade, False otherwise
    """
    cleaned = clean_text_for_readability(text)
    return textstat.flesch_kincaid_grade(cleaned) <= target_grade

def run_all_evals(text, word_count_min=300, word_count_max=800, client_focus_min=5, target_grade=9):
    """
    Runs all evaluation functions on the provided text and returns results in a dictionary.

    Args:
        text (str): The text to evaluate
        word_count_min (int): Minimum word count (default: 300)
        word_count_max (int): Maximum word count (default: 800)
        client_focus_min (int): Minimum required "you"/"your" mentions (default: 5)
        target_grade (int): Target grade level for readability (default: 9)

    Returns:
        dict: Dictionary containing results of all evaluations
    """
    results = {
        "word_count": word_count_eval(word_count_min, word_count_max, text),
        "client_focus": client_focus_eval(client_focus_min, text),
        "social_proof": social_proof_eval(text),
        "readability": readability_eval(text, target_grade)
    }
    
    return results

def generate_eval_report(profile_text: str) -> str:
    """
    Generates a markdown-formatted prompt for an LLM to revise an Upwork profile,
    with explicit strategies for word count and readability improvements.

    Args:
        profile_text (str): The profile text to evaluate and generate a report for

    Returns:
        str: A markdown-formatted evaluation report and rewrite instructions
    """
    status_emoji = {True: "✅ Passed", False: "❌ Failed"}

    results = run_all_evals(profile_text)

    notes = {
        "word_count": {
            True: "Your profile is within the ideal range of 300 words.",
            False: "Your profile is under 300 words. Aim for 300-800 words to convey expertise without overwhelming the reader."
        },
        "client_focus": {
            True: "Your profile speaks directly to the client by using 'you' or 'your' frequently.",
            False: "The word 'you' or 'your' appears infrequently. Aim for at least 5 mentions to improve client-centric tone."
        },
        "social_proof": {
            True: "Your profile includes social proof such as testimonials or results.",
            False: "There's no mention of past clients, project outcomes, or measurable success."
        },
        "readability": {
            True: "The writing is clear and accessible, at or below a 9th grade reading level.",
            False: "The text may be too complex. Aim for a 9th grade reading level or lower by using simpler words and shorter sentences."
        }
    }

    markdown = "### 📄 Upwork Profile Evaluation + Rewrite Task\n\n"
    markdown += "You are an expert Upwork profile coach.\n\n"
    markdown += "Below is a freelancer's current Upwork profile, followed by a quality evaluation report.\n\n"
    markdown += "Your task is to revise the profile to address any **failed** metrics from the evaluation.\n\n"
    markdown += "---\n\n"

    markdown += "### ✏️ Current Profile Text\n\n"
    markdown += f"```text\n{profile_text.strip()}\n```\n\n"
    markdown += "---\n\n"

    markdown += "### 🧪 Evaluation Results\n\n"
    markdown += "| Metric         | Status | Notes |\n"
    markdown += "|----------------|--------|-------|\n"
    for metric in ["word_count", "client_focus", "social_proof", "readability"]:
        status = status_emoji[results[metric]]
        note = notes[metric][results[metric]]
        markdown += f"| **{metric.replace('_', ' ').title()}** | {status} | {note} |\n"

    markdown += "\n---\n\n"

    markdown += "### 🎯 Rewrite Instructions\n\n"
    markdown += "Revise the profile based on the **failed** metrics above.\n\n"

    if not results["word_count"]:
        markdown += f"- 📈 **Increase Word Count:** Your profile has {len(profile_text.split())} words, which is {max(0, 300 - len(profile_text.split()))} short of the minimum. Add: Address specific client pain points, Offer solutions tailored to client needs, Include client success stories with specific metrics, Provide a detailed explanation of your process or methodology, Highlight additional qualifications, skills, or relevant experience that solve client problems\n"

    if not results["readability"]:
        markdown += "- ✂️ **Improve Readability:** Simplify to a 9th-grade level using shorter sentences, simpler words, and breaking up long paragraphs.\n"

    if not results["client_focus"]:
        markdown += "- 🎯 **Make It More Client-Focused:** Use the words 'you' and 'your' frequently. Frame your services as solutions to the client's problems.\n"

    if not results["social_proof"]:
        markdown += "- 🧪 **Add Social Proof:** Mention past clients, testimonials (include quotes), or quantifiable outcomes (dollar figures).\n"

    markdown += "\n🛑 Only update the sections needed. Keep strong sections intact.\n"
    markdown += "🎯 Write in a confident, clear, and client-facing tone.\n"
    markdown += "📦 Return ONLY the revised profile in markdown format, with no extra commentary.\n\n"

    markdown += "---\n\n"
    markdown += "### 🚀 Revised Profile\n\n"

    return markdown


def rewrite_profile(instructions: str, prompt: str, client, temperature: float = 0.5) -> str:
    """
    Rewrites the profile text to improve readability and engagement.

    Args:
        instructions (str): The instructions for the rewrite
        prompt (str): The text of the profile to rewrite
        client (OpenAI): The OpenAI client

    Returns:
        str: The rewritten profile text
    """
    # make api call
    response = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=prompt,
        temperature=temperature
    )

    return response.output_text



