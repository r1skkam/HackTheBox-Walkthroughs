### 06-Feb-24-Tue

[Keeper](https://app.hackthebox.com/machines/Keeper)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/07a2a3c4-6356-42c0-ab77-ad4109be4406)

```
echo '10.129.45.173 keeper.htb' | sudo tee -a /etc/hosts
```

```
echo '10.129.45.173 tickets.keeper.htb' | sudo tee -a /etc/hosts
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/61867277-f9e1-4ce7-80d0-6402650fe193)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0936c08e-d417-42de-acc2-1dd4acdfbc97)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/29957c86-b387-4604-9cf8-7a8889df4c99)

*rt 4.4.4+dfsg-2ubuntu1 Default Credentials*

https://docs.bestpractical.com/rt/4.4.3/README.html

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fa756420-9b50-4ea9-8930-b18b53441d7f)

```
Username - root
Password - password
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c3500a67-6d45-475f-8e1e-f77eba26bb1c)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3b1cdc6b-bbd4-44d7-b684-86959cac6997)

http://tickets.keeper.htb/rt/Admin/Scrips/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ee76b2e6-24b1-47c6-abef-8fbfb89d765e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a3c07c8c-0f58-429d-9f16-d743313f0205)

http://10.10.14.18/nmap.txt

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8e111ffd-d3f2-4a78-8f96-bcdaf29c0106)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4555ae21-c310-4f7c-8241-a88cccdbecaa)

```
Possible cross-site request forgery

RT has detected a possible cross-site request forgery for this request, because the Referrer header supplied by your browser (tickets.keeper.htb:80) is not allowed by RT's configured hostname (keeper.htb:80). A malicious attacker may be trying to modify RT's configuration on your behalf. If you did not initiate this request, then you should alert your security team.

If you really intended to visit http://keeper.htb/rt/Admin/Scrips/Create.html and modify RT's configuration, then [click here to resume your request](http://keeper.htb/rt/Admin/Scrips/Create.html?CSRF_Token=1d8803b9dea385749b3aeb84b6548148).
```

http://keeper.htb/rt/Admin/Scrips/Create.html?CSRF_Token=1d8803b9dea385749b3aeb84b6548148

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2f9dca7c-694f-4722-9987-0d1f86609fb9)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b8bf789b-50dd-482a-ac0c-63ba16d9a756)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/87ea19bc-67f1-4373-84b5-d2791b224822)

```

Real Name Enoch Root
Email Address root@localhost
Name root
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2db23ef9-6d99-420b-9090-c975ed207998)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/457c8906-210b-4895-9b8d-599598ebfa7d)

```
New user. Initial password set to Welcome2023!
```

```
Welcome2023!
```

```
ssh lnorgaard@keeper.htb
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/aa7fe83e-e005-47fb-a19e-e395861b67d3)

```
c36f37ff41cf1f84e1a68f1ed87dd595
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b3663274-c2b7-4d6a-aca2-33cbe9fab4ec)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/954cf585-5b0b-4a95-8691-acdfb7cd06a5)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/de9d61c1-de14-406d-89d5-d41971363a6c)

http://tickets.keeper.htb/rt/Ticket/ShowEmailRecord.html?id=300000&Transaction=37&Attachment=5

```
Email Source for Ticket 300000, Attachment 5
From: "Enoch Root" <rt@keeper.htb>
In-Reply-To:
Precedence: bulk
Content-Type: multipart/alternative; boundary="----------=_1684924638-1803-2"
X-RT-Loop-Prevention: tickets.keeper.htb
X-Managed-BY: RT 4.4.4+dfsg-2ubuntu1 (http://www.bestpractical.com/rt/)
Subject: [tickets.keeper.htb #300000] Issue with Keepass Client on Windows
X-RT-Originator: root@localhost
References: <RT-Ticket-300000@keeper.htb>
Date: Wed, 24 May 2023 12:37:18 +0200
MIME-Version: 1.0
Reply-To: rt@keeper.htb
Content-Transfer-Encoding: 8bit
X-RT-Ticket: tickets.keeper.htb #300000
Message-ID: <rt-4.4.4+dfsg-2ubuntu1-1803-1684924638-1810.300000-8-0@keeper.htb>
To: lnorgaard@keeper.htb
Content-Length: 0

RT-Attach-Message: yes
Content-Type: text/plain; charset="utf-8"
X-RT-Original-Encoding: utf-8
Content-Length: 453

Wed May 24 12:37:18 2023: Request 300000 was acted upon by root.

Transaction: Ticket created by root
Queue: General
Subject: Issue with Keepass Client on Windows
Owner: lnorgaard
Requestors: webmaster@keeper.htb
Status: new
Ticket URL: http://keeper.htb/rt/Ticket/Display.html?id=300000



Lise,

Attached to this ticket is a crash dump of the keepass program. Do I need to
update the version of the program first...?

Thanks! 
Content-Type: text/html; charset="utf-8"
X-RT-Original-Encoding: utf-8
Content-Length: 954

<b>Wed May 24 12:37:18 2023: Request <a href="http://keeper.htb/rt/Ticket/Display.html?id=300000">300000</a> was acted upon by root.</b>
<br>
<table border="0">
<tr><td align="right"><b>Transaction:</b></td><td>Ticket created by root</td></tr>
<tr><td align="right"><b>Queue:</b></td><td>General</td></tr>
<tr><td align="right"><b>Subject:</b></td><td>Issue with Keepass Client on Windows </td></tr>
<tr><td align="right"><b>Owner:</b></td><td>lnorgaard</td></tr>
<tr><td align="right"><b>Requestors:</b></td><td>webmaster@keeper.htb</td></tr>
<tr><td align="right"><b>Status:</b></td><td>new</td></tr>
<tr><td align="right"><b>Ticket URL:</b></td><td><a href="http://keeper.htb/rt/Ticket/Display.html?id=300000">http://keeper.htb/rt/Ticket/Display.html?id=300000</a></td></tr>
</table>
<br/>
<br/>
Lise,<br>
<br>
Attached to this ticket is a crash dump of the keepass program. Do I need to update the version of the program first...?<br>
<br>
Thanks!
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3de67945-041b-41d4-98fb-ad286890a370)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0b96f509-929e-45f0-aa35-ab1ffc0418fc)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b47f888a-6f83-4a76-99f0-cd2f530c943b)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4babad08-d984-4e92-a79e-58926251ac30)

https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-8.0.101-linux-x64-binaries

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b19708a8-70fc-4c31-99ad-703f8601ed61)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4f3e64e7-aadb-497e-a225-f23fdab52bf1)

```
M}dgrød med fløde
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5fc803c6-469e-4759-a449-dfd271524593)

```
rødgrød med fløde
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0034ba62-151b-429e-93a9-b1002d566eab)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7dac7c8c-3f61-4e67-a536-67e989d0d98c)

```
PuTTY-User-Key-File-3: ssh-rsa
Encryption: none
Comment: rsa-key-20230519
```

*Public-Lines: 6*

```
AAAAB3NzaC1yc2EAAAADAQABAAABAQCnVqse/hMswGBRQsPsC/EwyxJvc8Wpul/D
8riCZV30ZbfEF09z0PNUn4DisesKB4x1KtqH0l8vPtRRiEzsBbn+mCpBLHBQ+81T
EHTc3ChyRYxk899PKSSqKDxUTZeFJ4FBAXqIxoJdpLHIMvh7ZyJNAy34lfcFC+LM
Cj/c6tQa2IaFfqcVJ+2bnR6UrUVRB4thmJca29JAq2p9BkdDGsiH8F8eanIBA1Tu
FVbUt2CenSUPDUAw7wIL56qC28w6q/qhm2LGOxXup6+LOjxGNNtA2zJ38P1FTfZQ
LxFVTWUKT8u8junnLk0kfnM4+bJ8g7MXLqbrtsgr5ywF6Ccxs0Et
```

*Private-Lines: 14*

```
AAABAQCB0dgBvETt8/UFNdG/X2hnXTPZKSzQxxkicDw6VR+1ye/t/dOS2yjbnr6j
oDni1wZdo7hTpJ5ZjdmzwxVCChNIc45cb3hXK3IYHe07psTuGgyYCSZWSGn8ZCih
kmyZTZOV9eq1D6P1uB6AXSKuwc03h97zOoyf6p+xgcYXwkp44/otK4ScF2hEputY
f7n24kvL0WlBQThsiLkKcz3/Cz7BdCkn+Lvf8iyA6VF0p14cFTM9Lsd7t/plLJzT
VkCew1DZuYnYOGQxHYW6WQ4V6rCwpsMSMLD450XJ4zfGLN8aw5KO1/TccbTgWivz
UXjcCAviPpmSXB19UG8JlTpgORyhAAAAgQD2kfhSA+/ASrc04ZIVagCge1Qq8iWs
OxG8eoCMW8DhhbvL6YKAfEvj3xeahXexlVwUOcDXO7Ti0QSV2sUw7E71cvl/ExGz
in6qyp3R4yAaV7PiMtLTgBkqs4AA3rcJZpJb01AZB8TBK91QIZGOswi3/uYrIZ1r
SsGN1FbK/meH9QAAAIEArbz8aWansqPtE+6Ye8Nq3G2R1PYhp5yXpxiE89L87NIV
09ygQ7Aec+C24TOykiwyPaOBlmMe+Nyaxss/gc7o9TnHNPFJ5iRyiXagT4E2WEEa
xHhv1PDdSrE8tB9V8ox1kxBrxAvYIZgceHRFrwPrF823PeNWLC2BNwEId0G76VkA
AACAVWJoksugJOovtA27Bamd7NRPvIa4dsMaQeXckVh19/TF8oZMDuJoiGyq6faD
AF9Z7Oehlo1Qt7oqGr8cVLbOT8aLqqbcax9nSKE67n7I5zrfoGynLzYkd3cETnGy
NNkjMjrocfmxfkvuJ7smEFMg7ZywW7CBWKGozgz67tKz9Is=
```

*Private-MAC: b0a0fd2edf4f0e557200121aa673732c9e76750739db05adc3ab65ec34c55cb0*

```
F4><3K0nd!
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/35aac3ab-7dac-40b1-9f69-402ec69bb778)

```
puttygen keeper.ppk -O private-openssh -o id_rsa
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8948cd8c-4dca-4207-80f2-b154c22afbf7)

```
ssh root@keeper.htb -i id_rsa
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/69f0169e-4f77-43c9-8ee1-306d7fe5dea3)

```
bcbb3f1619eafa809339023dc9ca962f
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ddcc6f52-59b4-4d9e-9ae8-b2dd713d800d)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d5bd6b66-54b2-4f77-afa1-136fae6bb636)

Walkthrough/Writeup - https://medium.com/@li_allouche/hack-the-box-keeper-writeup-56644dc6a55f
