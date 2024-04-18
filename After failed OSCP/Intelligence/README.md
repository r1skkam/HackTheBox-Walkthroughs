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

http://intelligence.htb/documents/2020-01-01-upload.pdf

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6cd78017-4e8d-4c08-ae69-a147ed570204)

http://intelligence.htb/documents/2020-12-15-upload.pdf

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8eea40ea-d503-485e-9921-ee4374672e8a)

https://youtu.be/Jg_BjkxdtsE?t=351

https://www.youtube.com/@ippsec

```
date --date="1 day ago" +%Y-%m-%d-upload.pdf
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/414d971a-10b0-44da-992c-b633cd89ec48)

Date within 2020-01-01 and 2020-12-15

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6e75f8d6-6a82-4eb4-97b4-ed4b8c5ea88f)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bae32d59-c451-485c-8d0d-7e5435094ded)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ccfcbcf6-e7dc-4cef-8798-0ed20356c797)

```
ffuf -w date-based.txt:FUZZ -u 'http://intelligence.htb/documents/FUZZ' -mc 200 > uploaded-pdf.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e062e195-b6d4-4789-95ca-f23397be730b)

```
cat uploaded-pdf.txt | awk '{print $1}' > pdf.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b6bf8ec2-6d63-42c7-beef-5acf526d08fd)

```
for i in $(cat pdf.txt); do echo http://10.129.95.154/documents/$i; done
```

```
d=2020-01-01; while [ "$d" != `date -I` ]; do echo "http://10.129.95.154/documents/$dupload.pdf"; done | xargs -n 1 -P 20 wget < list 2>/dev/null
```

```
exiftool *.pdf
```

get-exiftool-creator.py
