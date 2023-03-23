#!/bin/sh

KEYRING=8E097DDB13F0722F
RECIPIENT=marc@marcpartensky.com

gpg --import /root/signature.key

7z a $1.7z $1
gpg --always-trust --yes --sign --encrypt --recipient $RECIPIENT $1.7z
rm $1.7z
