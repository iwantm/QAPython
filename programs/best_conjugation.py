import os


def dictionary():
    script_dir = os.path.dirname(__file__)
    rel_path = "wordlist.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    text_file = open(os.path.join(abs_file_path), "r")
    words = text_file.read().split("\n")
    return words


def sub(word):
    sub_strings = [word[i: j] for i in range(len(word))
                   for j in range(i + 1, len(word) + 1)]
    return sub_strings


def bc(s):
    valid_subs = []
    all_subs = sub(s)
    words = dictionary()
    for word in all_subs:
        if word.lower() in words:
            valid_subs.append(word)
    valid_subs = list(dict.fromkeys(valid_subs))
    valid_subs.remove(s)
    return valid_subs
