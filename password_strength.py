import re


def load_data(filepath):
    data = ""
    with open(filepath, 'r', encoding="utf8") as file:
        data = file.read().split()
    return data


def get_password_strength(password, blacklist):
    if password in blacklist:  # check blacklist
        return 0
    score = 1

    if len(password) < 5:  # check password length +3
        return -2
    elif 8 <= len(password) <= 10:
        score += 1
    elif 11 <= len(password) <= 14:
        score += 2
    else:
        score += 3

    if re.search('[А-Яа-яA-Za-z]', password):  # check letters +1
        score += 1
    else:
        return -1

    if re.search('\d', password):  # check digits +1
        score += 1
    if re.search('\W', password):  # check special characters +2
        score += 2
    if not (password.isupper() or password.islower()):  # check upper and lowercase +2
        score += 2
    return score


if __name__ == '__main__':

    filepath = 'blacklist.txt'
    if input('Do you want to use your own password list? (y/n)\n').lower() == 'y':
        filepath = input('Type path to the file:\n')
    password_list = load_data(filepath)
    password = input('Type your password:\n')

    score = get_password_strength(password, password_list)

    result = ''
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
