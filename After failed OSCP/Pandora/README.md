### 2024-04-23-Tue

[Pandora](https://app.hackthebox.com/machines/Pandora)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9167d283-0b57-400f-8982-65b546218a9b)

# About Pandora

Pandora is an easy rated Linux machine. 
The port scan reveals a SSH, web-server and SNMP service running on the box. 
Initial foothold is obtained by enumerating the SNMP service, which reveals cleartext credentials for user `daniel`. 
Host enumeration reveals Pandora FMS running on an internal port, which can be accessed through port forwarding. 
Lateral movement to another user called `matt` is achieved by chaining SQL injection &amp;amp;amp;amp; RCE vulnerabilities in the PandoraFMS service. 
Privilege escalation to user `root` is performed by exploiting a SUID binary for PATH variable injection. 

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f18f3c19-5a5f-412d-882e-125ced8b78b2)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0e75a982-762c-4a4b-af22-a995f79768d4)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9d561722-3de0-4852-bf58-96305bbb16fd)

```
snmpwalk -v 1 -c public 10.129.208.20
```

```
snmpbulkwalk -c public -v2c 10.129.208.20 .
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/969cebc7-68dd-4fd8-aa3c-2c21e497d54d)

```
hydra -L usernames.txt -P passwords.txt ssh://10.129.208.20:22 -t 4 -V
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/95ab69a1-3e37-4409-b5c4-647716eb0384)

*daniel:HotelBabylon23*

```
ssh daniel@10.129.208.20
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/15f34ff8-76da-47c4-a626-4d9277740848)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3c13332f-2de9-415b-af61-fe3ad30a7b79)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e20092e7-311f-40a7-b2c1-831af7ab4235)

```
ssh -D 9090 daniel@10.129.208.20
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/12c7d28f-dd61-4a2d-b67c-16ab73bdcff0)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/473f940d-4e3f-41d6-97c1-aa23e92bf018)

*v7.0NG.742_FIX_PERL2020*

