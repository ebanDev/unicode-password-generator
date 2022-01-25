#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import secrets
import pyperclip

MAX_NUM_RANGE = 110000

password_manager = {
    "Bitwarden": "https://bitwarden.com/",
    "KeePass": "https://keepass.info/",
    "NextCloud Password": "https://apps.nextcloud.com/apps/passwords"
}

secretsGenerator = secrets.SystemRandom()
password = ""
long = 0

# If the user does not insert a number
while True:
    user_input = input("Longueur du mot de passe : ")
    try:
        long = int(user_input)

        if long <= 0:
            print("Veuillez inserer un nombre positif superieur à 0.")
            continue
        
        break
    except ValueError:
        print("Veuillez insérer un nombre valide.")

for _ in range(long):
    random_number = secretsGenerator.randint(0, MAX_NUM_RANGE)  # Generate a random number beetween 0 and 110 000
    if chr(random_number).isprintable():  # Check if the generated charactere is printable
        password += chr(random_number)

pyperclip.copy(password)

print("\nVotre mot de passe est : %s\n"
      "Il a été copié dans le presse papier.\n" % password)

print("N'oubliez pas de le stocker dans un gestionnaire de mot de passe tel que:")

for k,v in password_manager.items():
    print(" - %s: %s" % (k, v))

