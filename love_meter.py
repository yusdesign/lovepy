# love_meter.py
import random
import pyjokes
import json
import os
from datetime import datetime
from pathlib import Path

def love_meter():
    """Your exact 3-tier logic, GitHub optimized"""
    chance = random.random()
    
    # First joke (printed)
    joke1 = pyjokes.get_joke()
    print(f"😂 Joke #1: {joke1}")
    
    # Second joke (for message)
    joke2 = pyjokes.get_joke()
    
    # Your original logic
    if chance > 0.7:
        message = "💖 Python loves you unconditionally! ❤️"
        emoji = "💖"
        level = "LOVE"
        extra = f"Extra joke: {joke2}"
    elif chance > 0.3:
        message = "🤝 Python kinda likes you... but needs more indentations."
        emoji = "🤝"
        level = "LIKE"
        extra = f"Joke: {joke2}"
    else:
        message = "💔 Python's heart is currently segfaulting. Try again later."
        emoji = "💔"
        level = "SEGFAULT"
        extra = f"Funny: {joke2}"
    
    # Print result (goes to GitHub Actions log)
    print(f"\n{emoji} {message}")
    print(f"🎲 Chance: {chance:.1%}")
    print(f"⏰ Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"\n📊 Level: {level}")
    
    # Save to files
    result = f"""{emoji} Python Love Meter
{message}

🎲 Chance: {chance:.1%}
😂 {extra}
⏰ {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}
🔗 https://github.com/{os.getenv('GITHUB_REPOSITORY', 'user/repo')}
"""
    
    # Write to result.txt
    with open("result.txt", "w") as f:
        f.write(result)
    
    # Write JSON for APIs
    with open("love_result.json", "w") as f:
        json.dump({
            "level": level,
            "chance": chance,
            "emoji": emoji,
            "message": message,
            "joke": joke2,
            "timestamp": datetime.utcnow().isoformat(),
            "repository": os.getenv("GITHUB_REPOSITORY"),
            "run_id": os.getenv("GITHUB_RUN_ID")
        }, f, indent=2)
    
    return level, chance

if __name__ == "__main__":
    level, chance = love_meter()
    
    # Set GitHub outputs (for workflow)
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"level={level}\n")
            f.write(f"chance={chance}\n")
