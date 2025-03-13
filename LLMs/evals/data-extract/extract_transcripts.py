# Script to extract transcripts from YouTube videos

from youtube_transcript_api import YouTubeTranscriptApi

# get list of video ids from video_ids.txt
with open("video_ids.txt", "r") as f:
    video_ids = f.read().splitlines()

# remove new line characters from video ids
video_ids = [id.strip() for id in video_ids]

# loop through video ids and extract transcripts
for i, video_id in enumerate(video_ids):

    # get transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join([t["text"] for t in transcript])

    # save transcript to file
    with open(f"transcripts/{i+1}-{video_id}.txt", "w") as f:
        f.write(transcript_text)
