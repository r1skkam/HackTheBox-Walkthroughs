### 09-Feb-24-Fri

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

