### 17-Apr-24-Wed

[Intelligence | HackTheBox](https://app.hackthebox.com/machines/Intelligence)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c0bc425d-5177-4221-ba78-5f8c58c6bf9f)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ad99ed03-4ed8-4b8a-9332-413eb4fbd3bb)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1f003e13-d59c-41a0-b223-153d0bdae335)

http://intelligence.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5f22afe5-782c-4d9d-b28d-592462668bad)

```
gobuster dir -u http://intelligence.htb/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.txt -x txt,php,pdf
```

http://intelligence.htb/documents/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/75adf1b5-2687-4198-bbfa-73a1157267c3)

```
wget -c https://raw.githubusercontent.com/Septimus4/dateGenerator/master/date_generator.py
```

