from functools import wraps
from info import ADMINS

def is_admin(func):
    @wraps(func)
    async def wrapper(client, message):
        if message.from_user.id not in ADMINS:
            return await message.reply('ᴏɴʟʏ ᴛʜᴇ ʙᴏᴛ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ... 😑')
        return await func(client, message)
    return wrapper
