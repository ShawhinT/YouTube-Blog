# script to extract the blog content from the html files according to the blog titles

import os
import re
from bs4 import BeautifulSoup
import html2text
import glob

# Create output directory if it doesn't exist
output_dir = 'blogs-markdown'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read the blog titles from the text file
with open('blog_titles.txt', 'r') as f:
    blog_titles = [line.strip() for line in f.readlines() if line.strip()]

# Function to find the matching HTML file for a blog title
def find_html_file(title, directory='raw-medium-extract'):
    # Get all HTML files in the directory
    html_files = glob.glob(f'{directory}/*.html')
    
    # Clean the title for comparison (remove special characters, lowercase)
    clean_title = re.sub(r'[^\w\s]', '', title).lower()
    words = clean_title.split()
    
    # Try to find a file that contains most of the words from the title
    best_match = None
    best_match_count = 0
    
    for html_file in html_files:
        filename = os.path.basename(html_file)
        # Count how many words from the title appear in the filename
        match_count = sum(1 for word in words if word.lower() in filename.lower())
        
        # If this file matches more words than our current best match, update
        if match_count > best_match_count:
            best_match_count = match_count
            best_match = html_file
    
    # Also check the title tag inside the HTML files if needed
    if best_match_count < len(words) // 2:  # If less than half the words matched
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    soup = BeautifulSoup(content, 'html.parser')
                    html_title = soup.title.string if soup.title else ""
                    
                    # Count how many words from the title appear in the HTML title
                    match_count = sum(1 for word in words if word.lower() in html_title.lower())
                    
                    if match_count > best_match_count:
                        best_match_count = match_count
                        best_match = html_file
            except Exception as e:
                print(f"Error reading {html_file}: {e}")
    
    return best_match

# Initialize HTML to text converter
h2t = html2text.HTML2Text()
h2t.ignore_links = False
h2t.ignore_images = False
h2t.ignore_tables = False

# loop through the blog titles and extract the blog content
for i, title in enumerate(blog_titles, 1):  # Start enumeration from 1
    print(f"[{i}/{len(blog_titles)}] Processing: {title}")
    
    # find the matching HTML file
    html_file = find_html_file(title)
    print(f"HTML file: {html_file}")

    if html_file and os.path.exists(html_file):
        try:
            # Read the HTML content
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Parse the HTML
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract the main content (article body)
            article = soup.find('article')
            if article:
                # Find the main content section
                body_section = article.find('section', {'data-field': 'body'})
                
                if body_section:
                    # Convert HTML to markdown text
                    content = h2t.handle(str(body_section))
                    
                    # Create a safe filename with number prefix
                    safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
                    # Format the number with leading zeros for proper sorting (e.g., 01, 02, etc.)
                    output_file = os.path.join(output_dir, f"{i}_{safe_title}.md")
                    
                    # Write the content to a file
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(f"# {title}\n\n")
                        f.write(content)
                    
                    print(f"  Saved to {output_file}")
                else:
                    print(f"  No body section found in {html_file}")
            else:
                print(f"  No article found in {html_file}")
        except Exception as e:
            print(f"  Error processing {html_file}: {e}")
    else:
        print(f"  No matching HTML file found for '{title}'")

print("Extraction complete!")  