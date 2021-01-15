#!/bin/bash

for File in * 
do
    echo "****************************" 
    echo "File:" $File
    echo "****************************" 
    strings $File | grep "^NS"   
done
