#!/usr/bin/python
# -*- coding: utf-8 -*-
import secrets
import pyperclip

secretsGenerator = secrets.SystemRandom()
password = ""
inc = 0
long = input("Longueur du mot de passe : ")

while inc != int(long):
    random_number = secretsGenerator.randint(0, 110000)  # Generate a random number beetween 0 and 110 000
    if chr(random_number).isprintable():  # Check if the generated charactere is printable
        password += chr(random_number)
        inc += 1

pyperclip.copy(password)
print("Votre mot de passe est :", password, "\nIl a été copié dans le presse papier \nN'oubliez pas de le stocker dans un gestionnaire de mot de passe tel que Bitwarden, Keepass ou Nextcloud Password")
