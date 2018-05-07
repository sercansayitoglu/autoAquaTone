#!/bin/sh

#this script is  for starting  autoAquaTone.py as a background process

echo 1 >  engine.cfg

./autoAquaTone.py > /dev/null 2>&1 &

