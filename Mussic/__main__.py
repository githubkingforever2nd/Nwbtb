import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Mussic import LOGGER, app, userbot
from Mussic.core.call import Mussicc
from Mussic.plugins import ALL_MODULES
from Mussic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Mussic").error(
            "String Error, Please Add a Pyrogram String"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Mussic").warning(
            "Could not Find Spotify Secret Please Add One."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Mussic.plugins." + all_module)
    LOGGER("Mussic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Mussicc.start()
    try:
        await Mussicc.stream_decall("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except:
        pass
    try:
        await Mussicc.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Mussic").error(
            "[ERROR] - \n\nSir, first open telegram and turn on voice chat."
        )
        sys.exit()
    except:
        pass
    await Mussicc.decorators()
    LOGGER("Mussic").info("Mussicc X Music")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Mussic").info("Stopping Music Bot...")
