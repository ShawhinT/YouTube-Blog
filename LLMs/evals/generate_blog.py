# Script to generate a blog post from a YouTube transcript

import os
import openai
import dotenv
from youtube_transcript_api import YouTubeTranscriptApi

# import openai api key from .env file
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_posts(template_name, video_ids):
    """
    Generate blog posts from YouTube video transcripts using OpenAI.
    
    Args:
        template_name (str): Name of the prompt template file (without path)
        video_ids (list): List of YouTube video IDs to process
    
    Returns:
        int: Number of blog posts generated
    """
    # loop through video IDs and generate blog posts
    for i, video_id in enumerate(video_ids):
        
        # get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([t["text"] for t in transcript])
        
        # format the prompt
        prompt = prompt_template.format(transcript=transcript_text)

        # generate the blog post
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "developer", "content": prompt},
            ], 
            temperature = 0.5
        )

        # save the blog post to a file
        blog_folder = template_name.split(".")[0]
        os.makedirs(f"blogs/{blog_folder}", exist_ok=True)

        with open(f"blogs/{blog_folder}/{i+1}-{video_id}.md", "w") as f:
            f.write(response.choices[0].message.content)

        # print the progress
        print(f"Generated blog post: {i+1} / {len(video_ids)}")
    
    return len(video_ids)

# Call the function with the template name and video IDs
if __name__ == "__main__":
    # load prompt template
    template_name = "4_gpt.txt"
    with open(f"prompt-templates/{template_name}", "r") as f:
        prompt_template = f.read()

    # load video IDs from video_ids.txt
    with open("video_ids.txt", "r") as f:
        video_ids = f.readlines()
        # remove the newlines from the video ids
        video_ids = [video_id.strip() for video_id in video_ids]

    generate_blog_posts(template_name, video_ids)
