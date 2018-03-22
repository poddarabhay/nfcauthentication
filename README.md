# nfcauthentication
API for Authentication using NFC.


The API is open sourced and works across platforms
Registers new users
-Creates ‘rid’ and saves it, ‘uid’ of the NFC tag and encrypted user details into the database

Writes into the NFC tags
-Transmitter/Receiver writes the generated ‘rid’ into the tag

Reads and authenticates tags
-Reads tag and compares ‘rid’ with the maintained database
-If match occurs, user data in the database corresponding to the user is decrypted and passed on further

Demonstration GUI is made using Qt 
