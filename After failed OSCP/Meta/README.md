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

```
gobuster dns -d artcorp.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2080d1c9-5599-4f1a-9c3c-06192b50255a)

```
gobuster vhost -u artcorp.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

*All are 400 status code*

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f6689000-b402-4ec7-a9cd-a6a5b4b5dfe3)

```
wfuzz -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u artcorp.htb -H "Host: FUZZ.artcorp.htb" --hh 0
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2ad074d7-3fd8-42a9-aa51-93af0bd2bc19)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7a2eab22-c1a5-40fa-96d5-86f3113c2338)

http://dev01.artcorp.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6dacf4d0-f498-447e-a773-34fbbee851be)

http://dev01.artcorp.htb/metaview/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/31d09160-5942-4766-ac3e-c44cfd192693)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8878f584-f7fd-453c-a40b-8ea1de0ce5d4)

