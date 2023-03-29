#!/bin/sh

gpg --import $KEYS_PATH/signature.key

while true;
do
    date
    echo sleeping 1000s
    sleep 1000
done
