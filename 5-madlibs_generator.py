"""A simple madlibs generator"""
from typing import Set, Dict

with open("story.txt", "r") as f:
    story = f.read()

words: Set[str] = set()
start_word = -1
start_target = "<"
end_target = ">"

for i, char in enumerate(story):
    if char == start_target:
        start_word = i

    if char == end_target and start_word != -1:
        words.add(story[start_word : i + 1])
        start_word = -1

answer: Dict[str, str] = {}

for word in words:
    answer[word] = input(f"Enter {word}: ")

for word in words:
    story = story.replace(word, answer[word])

print(story)
