#! /bin/bash
#随机生成八位含数字大小写的密码

for i in range {1..10}
do
n1=` head -c 500 /dev/urandom |tr -dc a-zA-Z | tr [a-z] [A-Z]|head -c 1`
n2=`head -c 500 /dev/urandom | tr -dc a-z0-9A-Z | head -c 6`
n3=`echo $RANDOM |cut -c 2`
echo $n1$n2
done
