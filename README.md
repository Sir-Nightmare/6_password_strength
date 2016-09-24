# 6_password_strength

You can download your own password list from here:
https://github.com/danielmiessler/SecLists/tree/master/Passwords
https://dazzlepod.com/site_media/txt/passwords.txt
https://forum.antichat.ru/threads/281655/

password requirements:

inclusion at least 5 characters
5 <= n <= 7: +0
8 <= n <= 10 +1
11 <= n <= 14 +2
n => 15: +3
the use of both upper-case and lower-case letters (case sensitivity) +2
inclusion of one or more numerical digits +2
inclusion of special characters, such as @, #, $ +2
prohibition of words found in a password blacklist - score = 1