from tiktokapipy.api import TikTokAPI
import csv
import datetime
import os
import io
import aiohttp


# Uncomment this if you have trouble with playwright install in a venv
# os.system("playwright install")

def scrape_account(api, account_name, output_path, debug=False, opening_mode="w"):
    user = api.user(account_name, video_limit=0, scroll_down_time=30)
    with open("./data/" + output_path, opening_mode, newline='', encoding="utf_16") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(
            ["Author", "Description", "Creation time", "Diggs", "Shares", "Comments", "Play count", "Challenges"])
        counter = 0
        for video in user.videos:
            counter += 1
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
                print("Video : " + str(counter))
                print("====================")
        if (debug):
            print(counter)
        output.close()

def save_video(video):
    with aiohttp.ClientSession() as session:
        with session.get(video.video.download_addr) as resp:
            return io.BytesIO(await resp.read())

with TikTokAPI(navigation_retries=5, headless=True, navigator_type="firefox", navigation_timeout=0,
               emulate_mobile=False, scroll_down_time=1) as api:
    # Main accounts of the principal french politicians
    accounts = {
        "philippe.poutou": "stats_poutou.csv",
        "nathaliearthaud": "stats_lo.csv",
        "jlmelenchon": "stats_melenchon.csv",
        "yjadot": "stats_jadot.csv",
        "fabien_roussel": "stats_roussel.csv",
        "particommuniste": "stats_pcf.csv",
        "partisocialiste": "stats_ps.csv",
        "emmanuelmacron": "stats_macron.csv",
        "lesrepublicains": "stats_lr.csv",
        "dupontaignannicolas": "stats_dupont-aignan.csv",
        "jeanlassalleoff": "stats_lassalle.csv",
        "mlp.officiel": "stats_lepen.csv",
        "zemmour_eric": "stats_zemmour.csv"
    }

    scrape_account(api, "philippe.poutou", "stats_poutou.csv", True)
