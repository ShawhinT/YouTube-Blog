# script to extract blog titles from the video ids

import os
import requests
from dotenv import load_dotenv
import re
from functions import fetch_article, get_title


# load the environment variables
load_dotenv()

# load the video ids from the file
with open('video_ids.txt', 'r') as f:
    # read the video ids
    video_id_list = f.readlines()
    # remove the newlines from the video ids
    video_id_list = [video_id.strip() for video_id in video_id_list]

# loop through the video ids and gather the blog titles
blog_title_list = []
for video_id in video_id_list:
    # get the video description
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={os.getenv("YOUTUBE_API_KEY")}'
    response = requests.get(url)
    data = response.json()

    # extract the blog links from the video description
    description = data['items'][0]['snippet']['description']

    # find medium blog link in the description
    medium_blog_link = re.search(r'https://medium\.com/[^\n]+', description)
    if medium_blog_link:
        blog_url = medium_blog_link.group(0)
        try:
            # Fetch the article content
            article_html = fetch_article(blog_url)
            # Extract the title
            blog_title = get_title(article_html)
            blog_title_list.append(blog_title)
            print(f'Extracted title: {blog_title}')
        except Exception as e:
            print(f'Error extracting title from {blog_url}: {str(e)}')
            # Fallback to using the URL if we can't get the title
            blog_title_list.append(blog_url)
    else:
        print(f'No medium blog link found for id: {video_id}')

# Write all blog titles to a text file
with open('blog_titles.txt', 'w', encoding='utf-8') as f:
    for title in blog_title_list:
        f.write(f"{title}\n")
