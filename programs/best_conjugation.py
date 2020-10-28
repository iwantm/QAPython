def dictionary():
    text_file = open("wordlist.txt", "r")
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
