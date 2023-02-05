from tiktokapipy import TikTokAPIError
from tiktokapipy.api import TikTokAPI
import csv

from tiktokapipy.models.video import video_link


# Uncomment this if you have trouble with playwright install in a venv
# os.system("playwright install")

def scrape_account(api, account_name, output_path, debug=False, opening_mode="w"):
    user = api.user(account_name, video_limit=0, scroll_down_time=30)
    with open("./data/" + output_path, opening_mode, newline='', encoding="utf_16") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(
            ["Author", "Description", "Creation time", "Diggs", "Shares", "Comments", "Play count", "Challenges"])
        counter = 0
        for video_model in user.videos.light_models:
            counter += 1
            try:
                video = api.video(video_link(video_model.id))
                writer.writerow([
                    video.author,
                    video.desc,
                    video.create_time.date(),
                    video.stats.digg_count,
                    video.stats.share_count,
                    video.stats.comment_count,
                    video.stats.play_count,
                    [challenge.title for challenge in video.challenges]]
                )
                if (debug):
                    print("====================")
                    print("Scraping videos of " + account_name)
                    print("Video : " + str(counter))
                    print("Video desc : " + video.desc)
                    print("====================")
            except TikTokAPIError as e:
                print("An error has occurred during video collection")
                writer.writerow([
                    video_link(video_model.id),
                    "",
                    video_model.create_time.date(),
                    video_model.stats.digg_count,
                    video_model.stats.share_count,
                    video_model.stats.comment_count,
                    video_model.stats.play_count,
                    ""]
                )
                continue
        if (debug):
            print(counter)
        output.close()


with TikTokAPI(navigation_retries=5, headless=True, navigator_type="firefox", navigation_timeout=0,
               emulate_mobile=False, scroll_down_time=1) as api:
    # Main accounts of the principal french politicians
    accounts = {
        "philippe.poutou": "stats_poutou.csv",
        "nathaliearthaud": "stats_lo.csv",
        "yjadot": "stats_jadot.csv",
        "fabien_roussel": "stats_roussel.csv",
        "partisocialiste": "stats_ps.csv",
        "emmanuelmacron": "stats_macron.csv",
        "lesrepublicains": "stats_lr.csv",
        "jeanlassalleoff": "stats_lassalle.csv",
        "mlp.officiel": "stats_lepen.csv",
        "jlmelenchon": "stats_melenchon.csv",
        "particommuniste": "stats_pcf.csv",
        "dupontaignannicolas": "stats_dupont-aignan.csv",
        "zemmour_eric": "stats_zemmour.csv"
    }

    scrape_account(api, "zemmour_eric", "stats_zemmour.csv", debug=True)
