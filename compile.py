#!/usr/bin/env python3


import subprocess
import os

if __name__ == "__main__":
    try:
        os.remove("./pbrain-curry.exe")
    except:
        pass
    subprocess.call(["pyinstaller", "--onefile", "main.py", "AI.py", "Board.py", "Game.py"])
    try:
        os.rename("./dist/main.exe", "./pbrain-curry.exe")
    except:
        pass
