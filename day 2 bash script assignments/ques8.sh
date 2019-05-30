#!/bin/bash
declare -a arr
declare -a prime
arr=()
for value in {1..100}
do 
  arr+=( 1 )
done
for i in {2..100}
do 
  if [ ${arr[$i]} -eq 1 ]
  then
     ((k=2*i))
      for ((j=k; j<=100; j+=i))
     do
       ((arr[$j]=0))
     done
   fi
done
for i in {2..100} 
do
 if [ ${arr[$i]} -eq 1 ]
 then
    echo $i
 fi
done 
