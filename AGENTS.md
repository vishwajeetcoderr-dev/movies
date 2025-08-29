This document provides instructions and guidelines for developing this Telegram bot.

## Project Structure

The project is structured as follows:

- `bot.py`: The main entry point of the bot.
- `info.py`: Contains configuration variables for the bot.
- `Script.py`: Contains the text and templates used by the bot.
- `plugins/`: Contains the plugins for the bot.
- `database/`: Contains the database models and functions.
- `utils.py`: Contains utility functions.

### Plugins

The `plugins/` directory is where the bot's command handlers are located. The commands are split into the following files:

- `plugins/admin.py`: Contains admin-only commands.
- `plugins/user.py`: Contains user-facing commands.
- `plugins/utils.py`: Contains utility commands.

## Admin Checks

To check if a user is an admin, use the `@is_admin` decorator from `plugins.helper.admin_check`.

Example:
```python
from plugins.helper.admin_check import is_admin

@Client.on_message(filters.command("admin_command"))
@is_admin
async def admin_command(client, message):
    # This command can only be used by admins
    ...
```

This is the preferred way to handle admin checks. Avoid using `if message.from_user.id not in ADMINS:` directly in the command handlers.
