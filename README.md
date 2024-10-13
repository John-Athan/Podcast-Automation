# Podcast Automation

This repository contains a Python project for automating the creation of podcast episodes. The project synthesizes audio from text scripts, merges audio files, uploads the final podcast episode to Google Drive, and emails the link.

## Features

- Text-to-Speech (TTS) synthesis
- Audio file merging
- Google Drive upload
- Email notification

## Requirements

- Python 3.9+
- pip

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/John-Athan/podcast-automation.git
    cd podcast-automation
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Fetch content and generate the script:
    ```sh
    python podcast.py
    ```

2. The script will:
    - Fetch content
    - Select topics for domains
    - Generate a text script
    - Synthesize audio from the script
    - Merge audio files into a single podcast episode
    - Upload the episode to Google Drive
    - Email the link to the specified recipients

## Project Structure

- `podcast.py`: Main script to run the entire process.
- `audio.py`: Contains functions for audio synthesis and merging.
- `drive.py`: Handles uploading files to Google Drive.
- `input.py`: Fetches content for the podcast.
- `mail.py`: Sends email notifications with the podcast link.
- `text.py`: Generates the script and selects topics.

## Configuration

- Ensure you have the necessary API keys and credentials for Google Drive and email services.
- Place the content for the script in `example_data/script.json`.
