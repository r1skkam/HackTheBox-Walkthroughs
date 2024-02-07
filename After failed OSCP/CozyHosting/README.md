### 07-Feb-24-Wed

[CozyHosting](https://app.hackthebox.com/machines/CozyHosting)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9d28374e-abe1-408f-b2b9-c83c240aa5ec)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1f8c588d-5c72-4756-ba35-2d561735d978)

http://cozyhosting.htb/login

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ef15c62a-8d95-4fa9-be26-07291d5fa76f)

http://cozyhosting.htb/usersettings.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/980f8307-5273-4fa7-8069-d284293325bc)

```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt:FUZZ -u 'http://cozyhosting.htb/FUZZ' -k
```

```
ffuf -w /usr/share/seclists/Discovery/Web-Content/spring-boot.txt:FUZZ -u 'http://cozyhosting.htb/FUZZ' -k
```

http://cozyhosting.htb/actuator/sessions

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/250d89d3-d19d-4eba-8e00-c94f7d4f001e)

**Session Hijacking**

```
{"C6EC972292B31D51DD6CC2D76BA4E9BF":"kanderson"}
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/43bca6c5-09f9-4775-98aa-4e0c8252574e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/640c0a61-77ab-40f0-af4a-c91ca5053414)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fb1b81ea-bca0-4a96-8da7-f5efe74273b6)

```
{
"CDC486FA769DCE00A7422B65FD5A5618":"kanderson",
"1110D4636DBA4E9EC20507C98FC4CB7B":"UNAUTHORIZED",
"26DCF14037C4D76F6281F3F0851114AA":"UNAUTHORIZED",
"C923353C76138AE7A68DB1541BAE9FFE":"UNAUTHORIZED",
"370A276B6C913E8E8B9867D8E3FA9B36":"UNAUTHORIZED"
}
```

http://cozyhosting.htb/admin

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/37b097e9-6acd-4129-a5aa-aca637d72194)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/16d90589-9867-4e3e-8a65-5e9e04da0beb)

