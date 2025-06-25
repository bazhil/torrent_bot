# Torrent Bot

**ATTENCION:** This code is a prototype with minimal functionality.

A Telegram bot for managing and interacting with rutracker.org dump from 2014 year. This bot is built using Python.
Note, that using information from rutracker.org can be illegal in some countries and don't use it for outlaw activity.
This is educatable project, which can be used as prototype of something better.

For this project was user rutracker dump of torrents:
- https://habr.com/ru/articles/357530/
- https://rutracker.org/forum/viewtopic.php?t=4824458

**PS: This is my very old pet project, which can be better. But it is not my primary idea and current functionality in not full. If you have any experience in aiogram and telegram bots - you are welcome for made pull requests.**

## Features

- **Search**: Search torrent information by query

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bazhil/torrent_bot.git
   cd torrent_bot
   ```

2. Create .env
    ```bash
    mv .env.example .env
    ```
    
3. Fill .env:
    ```bash
    TELEGRAM_TOKEN=
    
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=
    POSTGRES_PORT=
    POSTGRES_DB=
    
    TORRENT_FOLDER_PATH=
    ```
   
4. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

5. Configure the database:
   - Download rutracker dump, set path of folder in .env `TORRENT_FOLDER_PATH=<path>`
   - Run the database setup script:
     ```bash
     python -m bot/async_filling_postgres.py
     ```

### Running the Bot

To run the bot, execute one of the following commands based on the library you want to use:

- For `python-telegram-bot`:
    ```bash
    cd bot
    python -m main
    ```

### Docker Deployment

**ATTENCION:** current docker setup is not tested correctly.

To deploy the bot using Docker:

1. Build the Docker image:
    ```bash
    docker-compose build
    ```

2. Start the container:
    ```bash
    docker-compose up
    ```

## Logs

Logs are stored in the `torrent_importer.log` for import-related logs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.