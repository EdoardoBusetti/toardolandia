import json
import os
import sys
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'emoji_letters_map.json'
with open(file_location) as json_file:
    letters_map = json.load(json_file)

def make_letter(s:str,background_emoji:str = "🖤",characters_emoji:str = "💚") -> str:
    if background_emoji!= "💚":
        s = s.replace("🖤",background_emoji)
        s = s.replace("💚",characters_emoji)
    else:
        s = s.replace("💚","_____@@_____")
        s = s.replace("🖤",background_emoji)
        s = s.replace("_____@@_____",characters_emoji)
    return s

def make_word(input_str,background_emoji = "🔥",characters_emoji="💧",letters_map = letters_map):
    s = ""
    for i in input_str.lower():
        s+= make_letter(s=letters_map[i],background_emoji = background_emoji,characters_emoji=characters_emoji) + "\n"
    return s