def load_data(filepath):
    data = ""
    with open(filepath, 'r', encoding="utf8") as file:
        data = file.read()
    return data


def get_password_strength(password, blacklist):
    if password in blacklist:
        return 'Score: 1. Your password was found in blacklist'





if __name__ == '__main__':
    list_of_passwords = 'blacklist.txt'
    if input('Do you want to use your own password list? (y/n)').lower() == 'y':
        list_of_passwords = input('Type path to the file:\n')
    password_list = load_data(list_of_passwords)
    password = input('Type your password:\n')
    print(get_password_strength(password, password_list))
