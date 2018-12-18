#!/usr/bin/env bash
systemctl start rpcbind.service
systemctl start nfs.service
systemctl enable rpcbind.service
systemctl enable  nfs.service
cp /etc/exports /etc/exports.bak
cat>>/etc/exports<<EOF
/newusr 192.168.134.0/24(rw,sync,no_root_squash)
EOF
#service    nfs     restart   
#service    rpcbind   restart  
systemctl restart rpcbind.service
systemctl restart nfs.service
mkdir  /newusr
chmod  o+w    /newusr
