# FTPcrack

## This is a script for cracking passwords on an FTP server, built for learning purposes.

### How it works:

First, the script asks for the IP address of the FTP server and the username for the account you're trying to get into, as well as the path to a password list.

The first try block will attempt to use each password in the selected list to log in. Using strip() removes trailing newline characters.

The second try block uses ftplib to connect to the server using the IP address provided by the user and then try the next password in the list.

The successful password will be printed to the screen if the user and password combo is successful.