1 - ldapsearch -H ldap:$addr -U $user -b 'DC=$DC,DC=$LOCAL' | grep -i sid | awk '{print $2}' > FILE.txt



2 - ex: python script.py FILE.txt
