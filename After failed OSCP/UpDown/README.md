### 2024-04-21-Sun

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

