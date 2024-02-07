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

