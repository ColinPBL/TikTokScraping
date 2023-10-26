from tiktokapipy import TikTokAPIError
from tiktokapipy.api import TikTokAPI
import os
import csv

from tiktokapipy.models.video import video_link


# Uncomment this if you have trouble with playwright install in a venv
# os.system("playwright install")

def scrape_challenge(api: TikTokAPI, challenge: str, output_path: str, video_limit=-1, debug=False, opening_mode="w"):
    """
    Get video statistics from trending TikTok videos associated to a specific hashtag.
    :param api: The TikTokAPI class instance used in the program
    :param challenge: The challenge (hashtag) to find videos
    :param output_path: The name of the file where the information will be written. The data is meant to be written to a
    csv file, in a data folder in the same directory as where the code is run
    :param video_limit: The maximum number of videos to be scrapped. Default value scraps all videos
    :param debug: Whether to print debug information, useful to know if the program is stuck
    :param opening_mode: By default, the output file is overwritten. Change to "a" to append to an existing file
    :return: None
    """
    trending = api.challenge(challenge, video_limit=video_limit)
    with open("./data/" + output_path, opening_mode, newline='', encoding="utf_16") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(
            ["Author", "Description", "Creation time", "Duration", "Diggs", "Shares", "Comments", "Play count",
             "Challenges"])
        counter = 0
        for video_model in trending.videos:
            counter += 1
            try:
                video = api.video(video_link(video_model.id))
                # Get video information
                row = [
                    video.author.unique_id,
                    video.desc,
                    video.create_time.date(),
                    video.video.duration,
                    video.stats.digg_count,
                    video.stats.share_count,
                    video.stats.comment_count,
                    video.stats.play_count]
                # Check if video has challenges, and add them if it is the case
                challenges = video.challenges
                if challenges:
                    row.append("".join([challenge.title for challenge in challenges]))
                # Append an empty string to preserve csv integrity
                else:
                    row.append("")

                # Write row to output
                writer.writerow(row)
                if debug:
                    print("====================")
                    print("Scraping videos of " + challenge)
                    print("Video : " + str(counter))
                    print("Video desc : " + video.desc)
                    print(f"Video challenges : {video.challenges}")

            except TikTokAPIError as e:
                # Sometimes, videos will return an error
                # In that case, we catch the error and write whatever info has been collected, and the video link so we
                # can manually collect the info
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
        output.close()


def scrape_account(api: TikTokAPI, account_name: str, output_path: str, video_limit=-1, debug=False, opening_mode="w"):
    """
    Get video statistics from a TikTok account
    :param api: The TikTokAPI class instance used in the program
    :param account_name: The account that is to be scrapped. Expects a handle
    :param output_path: The name of the file where the information will be written. The data is meant to be written to a
    csv file
    :param video_limit: The maximum number of videos to be scrapped. Default value scraps all videos
    :param debug: Whether to print debug information, useful to know if the program is stuck
    :param opening_mode: By default, the output file is overwritten. Change to "a" to append to an existing file
    :return: None
    """
    user = api.user(account_name, video_limit=video_limit)
    with open("./data/" + output_path, opening_mode, newline='', encoding="utf_16") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(
            ["Author", "Description", "Creation time", "Duration", "Diggs", "Shares", "Comments", "Play count",
             "Challenges"])
        counter = 0
        for video_model in user.videos:
            counter += 1
            try:
                video = api.video(video_link(video_model.id))
                # Get video information
                row = [
                    video.author.unique_id,
                    video.desc,
                    video.create_time.date(),
                    video.video.duration,
                    video.stats.digg_count,
                    video.stats.share_count,
                    video.stats.comment_count,
                    video.stats.play_count]
                # Check if video has challenges, and add them if it is the case
                challenges = video.challenges
                if challenges:
                    row.append("".join([challenge.title for challenge in challenges]))
                # Append an empty string to preserve csv integrity
                else:
                    row.append("NO CHALLENGE")

                # Write row to output
                writer.writerow(row)
                if debug:
                    print("====================")
                    print("Scraping videos of " + account_name)
                    print("Video : " + str(counter))
                    print("Video desc : " + video.desc)
                    print(f"Video challenges : {video.challenges}")

            except TikTokAPIError as e:
                # Sometimes, videos will return an error
                # In that case, we catch the error and write whatever info has been collected, and the video link so we
                # can manually collect the info
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
        output.close()


with TikTokAPI(navigation_retries=5, headless=True, navigation_timeout=0) as api:
    # Main accounts of the principal french politicians
    accounts = {
        "philippe.poutou": "stats_poutou.csv",
        "nathaliearthaud": "stats_lo.csv",
        "yjadot": "stats_jadot.csv",
        "fabien_roussel": "stats_roussel.csv",
        "partisocialiste": "stats_ps.csv",
        "emmanuelmacron": "stats_macron.csv",
        "parti_renaissance": "stats_renaissance.csv",
        "lesrepublicains": "stats_lr.csv",
        "jeanlassalleoff": "stats_lassalle.csv",
        "mlp.officiel": "stats_lepen.csv",
        "jlmelenchon": "stats_melenchon.csv",
        "particommuniste": "stats_pcf.csv",
        "dupontaignannicolas": "stats_dupont-aignan.csv",
        "zemmour_eric": "stats_zemmour.csv",
        "vpecresse": "stats_pecresse.csv"
    }

    scrape_account(api, "jeanlassalleoff", "stats_lassalle.csv", debug=True, video_limit=5)
