import os
import shutil

# --- 1. Delete unwanted folders/files ---
unwanted = ['streak.py', 'tests', '.github']
for item in unwanted:
    if os.path.isfile(item):
        os.remove(item)
        print(f"Deleted file: {item}")
    elif os.path.isdir(item):
        shutil.rmtree(item)
        print(f"Deleted folder: {item}")

# --- 2. Create required folders/files ---
# index.html
with open('index.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
    <title>IITM TDS Sample App</title>
</head>
<body>
    <h1>App will appear here</h1>
</body>
</html>""")
print("Created index.html")

# README.md
with open('README.md', 'w') as f:
    f.write("""# IITM TDS Sample App

## Summary
This is a placeholder app for Round 1.

## Setup
Open `index.html` in a browser.

## Usage
Currently just displays placeholder text.

## License
MIT""")
print("Created README.md")

# LICENSE (MIT template)
with open('LICENSE', 'w') as f:
    f.write("""MIT License

Copyright (c) 2025 <Your Name>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")
print("Created LICENSE")

# attachments folder
if not os.path.exists('attachments'):
    os.mkdir('attachments')
    print("Created attachments/ folder")

print("\nRound 1 repo structure ready!")
print("Next: git add, commit, and push to GitHub.")
