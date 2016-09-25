import re
import sys


def load_blacklist(filepath):
    with open(filepath, 'r', encoding="utf8") as file:
        blacklist = file.read().split()
    return blacklist


def get_password_strength(password, blacklist):
    if password in blacklist:
        return 0
    score = 1

    if len(password) < 5:
        return -2
    elif 8 <= len(password) <= 10:
        score += 1
    elif 11 <= len(password) <= 14:
        score += 2
    else:
        score += 3

    if re.search('[А-Яа-яA-Za-z]', password):
        score += 1
    else:
        return -1

    if re.search('\d', password):
        score += 1
    if re.search('\W', password):
        score += 2
    if not (password.isupper() or password.islower()):
        score += 2
    return score


def print_result(score):
    if score == 10:
        result = 'Score: 10. Your password is perfect!'
    elif score == 0:
        result = 'Score: 1. Your password was found in blacklist'
    elif score == -1:
        result = 'Score: 1. Your password has to include at least one letter '
    elif score == -2:
        result = 'Score: 1. Your password has to include at least 5 characters'
    elif 0 < score < 6:
        result = 'Score: ' + str(score) + '. Your password is not strong enough. You should choose another one'
    else:
        result = 'Score: ' + str(score) + '. Your password is quite good :)'
    print(result)


if __name__ == '__main__':
    filepath = sys.argv[1]
    password_list = load_blacklist(filepath)
    password = input('Type your password:\n')
    score = get_password_strength(password, password_list)
    print_result(score)
