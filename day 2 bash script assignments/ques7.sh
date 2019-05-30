#!/bin/bash
echo enter the number
read n
ans=1
while [ $n -gt 0 ]
do
  ((ans*=n))
  ((n--)) 
done
echo $ans

