import asyncio

from tiktokapipy.async_api import AsyncTikTokAPI
from tiktokapipy.api import TikTokAPI

import aiohttp
import io

from tiktokapipy.models.video import Video

async def save_video(video: Video):
    async with aiohttp.ClientSession() as session:
        async with session.get(video.video.download_addr) as resp:
            return io.BytesIO(await resp.read())

async def download_video(link, counter):
    async with AsyncTikTokAPI(scroll_down_time=1, headless=True, navigator_type="firefox", navigation_timeout=10000000) as api:
        video_bytes = await save_video(await api.video(link=link))
        with open("video" + str(counter), "wb") as output:
            output.write(video_bytes)
            output.close()

async def main():
    async with AsyncTikTokAPI(scroll_down_time=1, headless=True, navigator_type="firefox", navigation_timeout=0) as api:
        user = await api.user("philippe.poutou", scroll_down_time=10)
        counter = 0
        async for video in user.videos:
            await download_video(video.video.download_addr, counter)
            counter += 1

asyncio.run(main())