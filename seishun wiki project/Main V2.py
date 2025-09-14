import webbrowser
import os
import keyboard
import time

print("Index: Mai, Koga, Futaba, Nodoka, Kaede, Shoko")
wikiRequest = input("Enter name of character: ").lower()

base_dir = os.path.dirname(os.path.abspath(__file__))
print(os.path.abspath(__file__))
print(base_dir)


paths = {
    "kaede": "kaede/kaedewiki.html",
    "mai": "mai/maiwiki.html",
    "shoko": "shoko/shokowiki.html",
    "koga": "koga/kogawiki.html",
    "nodoka": "nodoka/nodokawiki.html",
    "futaba": "futaba/futabawiki.html",
    }
    
filepath = paths.get(wikiRequest)
print(filepath)

if filepath:
    full_path = os.path.join(base_dir, filepath)
    print(full_path)
    webbrowser.open(f"file:///{full_path}")
    time.sleep(1)
    keyboard.press_and_release('f11')
else:
    print("Character not found!")
