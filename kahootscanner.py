from kahoot import client
from kahootspammer import thread_spam

bot = client()
while True:
    for i in range(100000, 105000):
        a = bot.join(i, "aisfgjosafjasf")
        if a is None:
            thread_spam(i, "TRUMP 2020", 50, 10)
            print(f"Spamming {i}")

