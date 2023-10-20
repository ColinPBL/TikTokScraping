from tiktokapipy.api import TikTokAPI

def scrape_challenges(tag):
    with TikTokAPI() as api:
        challenge = api.challenge(tag, video_limit=10)
        for video in challenge.videos:
            print("====================")
            print("Video desc : " + video.desc)
            print("Video author : " + video.author.unique_id)
            print("Video creation time : " + str(video.create_time))



scrape_challenges("politique")