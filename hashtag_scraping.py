from tiktokapipy.api import TikTokAPI

def scrape_challenges(tag):
    # Create an instance of the TikTokAPI class
    with TikTokAPI() as api:
        # Get trending videos with the corresponding challenge, up to video_limit
        challenge = api.challenge(tag, video_limit=10)

        # Print information about each video
        for video in challenge.videos:
            print("====================")
            print("Video desc : " + video.desc)
            print("Video author : " + video.author.unique_id)
            print("Video creation time : " + str(video.create_time))



scrape_challenges("politique")