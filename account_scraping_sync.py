from tiktokapipy.api import TikTokAPI
import csv

with TikTokAPI(navigation_retries=5, headless=False, navigator_type="chromium", navigation_timeout=0, emulate_mobile=False, scroll_down_time=1) as api:
    user = api.user("zemmour_eric", video_limit=0, scroll_down_time=30)
    with open("stats_zemmour.csv", "w", newline='', encoding="utf_16") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(
            ["Author", "Description", "Creation time", "Diggs", "Shares", "Comments", "Play count", "Challenges"])
        counter = 0
        for video in user.videos:
            counter += 1
            writer.writerow([
                video.author,
                video.desc,
                video.create_time,
                video.stats.digg_count,
                video.stats.share_count,
                video.stats.comment_count,
                video.stats.play_count,
                video.challenges]
            )
            print("====================")
            print("Video : " + str(counter))
            print("====================")
        print(counter)
        output.close()


