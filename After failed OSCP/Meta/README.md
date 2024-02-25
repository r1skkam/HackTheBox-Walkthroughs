### 25-Feb-24-Sun

[Meta](https://app.hackthebox.com/machines/Meta)

```
echo "10.129.225.157 artcorp.htb" |sudo tee -a /etc/hosts
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/20730a7c-a6c4-4467-a147-0927224866d2)

http://artcorp.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3503350a-703b-4115-8ece-1bb6196442c6)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c9f94486-be2b-4948-83e4-b3220701feb2)

```
gobuster dns -d artcorp.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt -q -r 8.8.8.8 -t 4 --delay 1s -o subdomains.txt
```

```
gobuster vhost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://artcorp.htb/ -o gobuster-vhost-subdomains.txt
```

