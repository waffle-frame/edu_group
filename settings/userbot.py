from telethon import TelegramClient

from utils.config import Userbot


# Authorization and session file generation
def setup_userbot(conf: Userbot) -> TelegramClient:
    client = TelegramClient(
        f'session_{conf.phone_number}', conf.api_id, conf.api_hash
    )

    return client