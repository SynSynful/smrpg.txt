from atproto import Client
import os
import random

client = Client()
client.login(
    os.environ["USER_ACCOUNT"],
    os.environ["APP_PASSWORD"]
)

with open("smrpg.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

client.send_post(random.choice(lines))