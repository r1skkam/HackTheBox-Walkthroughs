### 18-Jan-24-Thu

https://app.hackthebox.com/machines/Bizness

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/610e0fac-f398-4c8f-86fe-5ef53cfe219a)

```
nmap -sC -sV -Pn -p- --open 10.129.53.236 -oN nmap.Bizness
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-18 11:35 EST
Nmap scan report for 10.129.53.236
Host is up (0.054s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
| ssh-hostkey: 
|   3072 3e:21:d5:dc:2e:61:eb:8f:a6:3b:24:2a:b7:1c:05:d3 (RSA)
|   256 39:11:42:3f:0c:25:00:08:d7:2f:1b:51:e0:43:9d:85 (ECDSA)
|_  256 b0:6f:a0:0a:9e:df:b1:7a:49:78:86:b2:35:40:ec:95 (ED25519)
80/tcp    open  http       nginx 1.18.0
|_http-title: Did not follow redirect to https://bizness.htb/
|_http-server-header: nginx/1.18.0
443/tcp   open  ssl/http   nginx 1.18.0
|_ssl-date: TLS randomness does not represent time
|_http-title: Did not follow redirect to https://bizness.htb/
| tls-nextprotoneg: 
|_  http/1.1
|_http-server-header: nginx/1.18.0
| ssl-cert: Subject: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=UK
| Not valid before: 2023-12-14T20:03:40
|_Not valid after:  2328-11-10T20:03:40
| tls-alpn: 
|_  http/1.1
35655/tcp open  tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 65.16 seconds
```

```
echo '10.129.53.236 bizness.htb' | tee -a /etc/hosts
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f8b7931e-6572-4339-80ac-28c0d7aacb70)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/07402c6b-76b1-46a5-93cc-90ef449afb77)

