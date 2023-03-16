# youtube-notifier

A simple tool to send push notifications of new YouTube videos using [ntfy.sh](https://ntfy.sh/).

## Usage

Putting the application on the server and running it periodically using CRON to get new content from specified YouTube channels.

## Setup

1. Clone this repo.
2. Edit `config.json` as you want.
3. Install dependencies - `pip install -r requirements.txt`.
4. Configure CRON to run `python main.py`.
3. Subscribe your topic in ntfy.sh app.