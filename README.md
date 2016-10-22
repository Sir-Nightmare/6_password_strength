# 6_password_strength

This script checks how strong your password is.

You can run it by the command: `python lang_frequency.py <path_to_blacklist>`

You can download your own password list from here:
[link1]( https://github.com/danielmiessler/SecLists/tree/master/Passwords) 
[link2]( https://dazzlepod.com/site_media/txt/passwords.txt) 
[link3]( https://forum.antichat.ru/threads/281655/)

Password requirements and scores for each characteristic:

* inclusion at least 5 characters
    5 <= n <= 7: **+0**
    8 <= n <= 10 **+1**
    11 <= n <= 14 **+2**
    n => 15: **+3**
* the use of both upper-case and lower-case letters (case sensitivity) **+2**
* inclusion of one or more numerical digits **+2**
* inclusion of special characters, such as @, #, $ **+2**
* prohibition of words found in a password blacklist - score = **1**