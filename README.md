# RSA-Data-Encryption

- Quick Overview
This project implements the RSA algorithm to encrypt/decrypt any given text in plaintext.txt to then the ciphertext in both binary_output.txt and integer_output.txt to then decrypt into decrypted.txt.

- How To Use
First off, this implementation uses block encryption with padding, I padded the data with a non-english character 'ÿ', so if you see that or a diamond with a question mark in it, you can ignore it as it was just to pad the blocks.

You can use this project in two different ways.
- Just encrypt and see decrypted text.
1. Put any standard input into the plaintext.txt file -> run encryption.py -> run decryption.py -> view decrypted.txt
   This allows you to see that your text was encrypted and decrypted successfully since they both contain the same contents.
   You may also take a look at the integer/binary output txt files to see what your data encrypted to.
   You can continue to follow this method over and over again by simply changing the text in the plaintext file.
- Change and generate new key values as you want to.
2. The project comes with default key values put in place, but if you want, you may generate new ones and replace the old ones.
   Follow this workflow: run key_generator.py -> View key value outputs in terminal -> Move to encryption.py and go to line 43 -> Take the first value of the public key terminal output, copy it, and replace the n variable       there -> Move to decryption.py and go to line 7 -> Replace the n value there with the exact same value as before(this will be the first value in both public and private key outputs) -> Now go to line 9 and replace the d      value there with the second value in the private key output.
   Now you can follow the first workflow of "Put any standard input into the plaintext.txt file -> run encryption.py -> run decryption.py -> view decrypted.txt" then you can repeat the previous steps to change the key values    at any time, just make sure to change all three spots each time you change any of them.
