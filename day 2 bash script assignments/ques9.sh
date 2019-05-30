#!/bin/bash
echo Enter the three sides
read x y z
if  (( $x+ $y< $z )) || (( $y + $z< $x )) || (( $z + $x < $y ))
then 
   echo not a triangle
elif [ $x -eq $y ] && [ $y -eq $z ]
then
   echo equilateral triangle
elif [ $x -eq $y ] || [ $x -eq $z ] || [ $y -eq $z ]
then
   echo isoceles triangle
else
   echo scalene triangle
fi
     
