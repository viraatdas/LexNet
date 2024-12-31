import os


root_dir = "../data"

processed = []

with open("scraped.txt", "r") as file:
    content = file.read()
    processed = [line.strip() for line in content.splitlines()]
  


for dirpath, dirnames, filenames in os.walk(root_dir):
    pass