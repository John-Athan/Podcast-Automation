import os
from audio import generate_audio
from drive import upload_to_google_drive
from input import fetch_content
from mail import email_link
from text import generate_script, select_topics_for_domains


if __name__ == "__main__":
    if not os.path.exists("example_data"):
        os.makedirs("example_data")
    fetch_content()
    select_topics_for_domains()
    generate_script()
    generate_audio()
    upload_to_google_drive()
    email_link()
    print("Done!")
