# nfcauthentication
API for Authentication using NFC.

NO HARDWARE IMPLEMENTATION AS OF NOW, WILL BE IMPLEMENTED IN COMING RELEASES.

DEPENDENCIES: Crypto.Cipher - AES , sqlite3, pyqt

The API is open sourced and works across platforms
Registers new users
-Creates ‘rid’ and saves it, ‘uid’ of the NFC tag and encrypted user details into the database

Writes into the NFC tags
-Transmitter/Receiver writes the generated ‘rid’ into the tag

Reads and authenticates tags
-Reads tag and compares ‘rid’ with the maintained database
-If match occurs, user data in the database corresponding to the user is decrypted and passed on further

Encryption using AES CFB-Cipher Feedback

sqlite3 for databases

Demonstration GUI is made using Qt 
