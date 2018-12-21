#! /bin/bash
#
to=$1
subject=$2
body=$3
/usr/local/bin/sendEmail  -f q865158909@163.com -t "$to" -s smtp.163.com -u "$subject" -o message-content-type=html -o message-charset=utf8 -xu q865158909@163.com -xp wb513692 -m "$body"
