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
ldapsearch -H ldaps://10.129.227.113:636/ -x -s base -b '' "(objectClass=*)" "*" +
```

