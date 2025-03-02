import os
from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(yt_id, out_file):
    """Generate transcript of yt video"""

    try:
        # Fetch the transcript and returns it as a list of dictionaries
        # dict contains text with start and duration.
        transcript = YouTubeTranscriptApi.get_transcript(yt_id)

        # Joins all the text into a single string
        transcript_text = " ".join([entry['text'] for entry in transcript])

        # Save transcrit to file
        with open(out_file, 'w', encoding='utf-8') as file:
            file.write(transcript_text)
        
        print("Transcript saved to {}".format(out_file))
        return True

    except Exception as e:
        print(f"Error extracting transcript: {e}")
        return False

URL = input("URL: ")
video_id = URL.split('=')[1]
output_file =  os.path.join(".", "transcript"+video_id+".txt")

if get_transcript(video_id, output_file):
    print("Transcript saved")
else:
    print("Failed to gen transcript")