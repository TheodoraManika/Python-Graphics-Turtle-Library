import random

def select_word():
    with open("hanging_man/words.txt") as words:
        word_list = words.readlines()
    return random.choice(word_list).strip()

if __name__ == "__main__":   
    print(select_word())