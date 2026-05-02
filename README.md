# ZallyMusicBot

Advanced Telegram music player bot built with Pyrogram + Py-TgCalls. Supports YouTube, Spotify, Apple Music, SoundCloud, Resso, and Telegram audio.

## Features
- High-quality voice/video chat streams
- Playlist support (YouTube, Spotify, Apple Music)
- Multi-language strings (`strings/langs/`)
- Admin controls: skip, pause, resume, loop, seek, speed, shuffle, stop
- Broadcast, autoleave, watcher, seeker
- Auto-update from upstream repo

## Requirements
- Python 3.10+
- ffmpeg
- MongoDB cluster (free tier works — https://cloud.mongodb.com)
- Telegram bot token (@BotFather)
- Pyrogram v2 string session (@StringFatherBot) for the assistant account

## Quick Start (local)
```bash
git clone https://github.com/rajasharmajii566-dev/ZallyMusicBot.git
cd ZallyMusicBot
cp .env.example .env
# Edit .env with your values
pip install -r requirements.txt
bash start
```

## Deploy on Railway
1. Fork or clone this repo to your GitHub
2. Create a new project on https://railway.app → Deploy from GitHub repo
3. In the **Variables** tab, paste these (one per line in Raw Editor):

```
API_ID=
API_HASH=
BOT_TOKEN=
LOGGER_ID=
MONGO_DB_URI=
OWNER_ID=
STRING_SESSION=
```

Important notes for Railway variables:
- `API_ID` — numeric only, no quotes
- `LOGGER_ID` — must start with `-100` for supergroups/channels (e.g. `-1001234567890`)
- `OWNER_ID` — your numeric Telegram user id
- `MONGO_DB_URI` — full `mongodb+srv://...` string
- `STRING_SESSION` — long Pyrogram v2 string

4. Railway auto-detects the `Dockerfile` and starts the worker. Watch the deploy logs — you should see "PritiMusic" startup banner.

## Deploy on Heroku
Click the deploy button (after configuring `app.json` heroku button) or:
```bash
heroku create your-app-name --stack container
git push heroku main
heroku config:set API_ID=... API_HASH=... BOT_TOKEN=... ...
```

## Deploy on VPS (Docker)
```bash
docker build -t zallymusicbot .
docker run -d --env-file .env --name zally zallymusicbot
```

## Project Structure
```
PritiMusic/
├── core/         # bot, userbot, mongo, call manager, git auto-update
├── platforms/    # YouTube, Spotify, Apple, SoundCloud, Resso, Telegram, Carbon
├── plugins/      # admins, bot, misc, play, sudo, tools commands
├── utils/        # decorators, helpers, queue, formatters
└── logging.py
strings/langs/    # Multi-language UI text
config.py         # Env-driven config
Dockerfile        # nikolaik/python-nodejs:3.10 + ffmpeg
start             # bash start → python3 -m PritiMusic
```

## Security
- `.env` is `.gitignore`d — never commit it
- All secrets must be set via environment variables
- Rotate `BOT_TOKEN` and `STRING_SESSION` if leaked

## Credits
Original codebase: PritiMusic / LuckyX team. Re-packaged for clean deployment.
