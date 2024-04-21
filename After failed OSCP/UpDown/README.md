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
