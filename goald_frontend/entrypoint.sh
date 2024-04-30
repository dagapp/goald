#!/bin/bash

# nginx stuff
nginx

if [ $# -ne 0 ]
then
    npm run srv &
    exec "$@"
else
    npm run srv
fi
