from tiktokapipy.api import TikTokAPI
import csv

with TikTokAPI(navigator_type="chromium", emulate_mobile=False) as api:
    user = api.user("jlmelenchon")
    with open("stats_melenchon.csv", "w", newline='', encoding="utf_16") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(
            ["Author", "Description", "Creation time", "Diggs", "Shares", "Comments", "Play count", "Challenges"])
        for video in user.videos:
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
        output.close()


