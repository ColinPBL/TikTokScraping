from tiktokapipy.api import TikTokAPI
import os

def scrape_challenges(tag):
    # Create an instance of the TikTokAPI class
    with TikTokAPI() as api:
        # Get trending videos with the corresponding challenge, up to video_limit
        challenge = api.challenge(tag, video_limit=100)

        # Print information about each video
        for video in challenge.videos:
            print("====================")
            print("Video desc : " + video.desc)
            print("Video author : " + video.author.unique_id)
            print("Video creation time : " + str(video.create_time))
            print("Video challenges : " + str(video.challenges))


os.system("playwright install")
scrape_challenges("nutrition")