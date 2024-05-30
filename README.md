1 - ldapsearch -H ldap://dc1.scrm.local -U $user -b 'DC=SCRM,DC=LOCAL' | grep -i sid | awk '{print $2}' > FILE.txt



2 - ex: python script.py FILE.txt
