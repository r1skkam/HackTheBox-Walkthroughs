### 2024-04-19

[Soccer | HackTheBox](https://app.hackthebox.com/machines/Soccer)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e3962273-55a8-424a-846b-3a22b1de7da8)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/01eb3854-8a08-432b-b96f-da07e468877c)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/97837b89-a423-4bf7-9ff8-15e8b0a58b31)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fd003883-4abd-46de-a45b-09e9a883063b)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/283a5fb5-3bb3-4f5a-985e-552b181e405c)

http://soccer.htb/tiny/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/c0abbdcc-bf62-49d9-a520-da2678d5a3e5)

https://tinyfilemanager.github.io/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a12b5c36-a21c-4c65-b469-26df88fa9ba3)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/d1a03218-7c1c-4ba1-b4bb-1646b2310101)

**admin:admin@123**

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/4b715836-d82c-4ea5-9dbf-95ab9dbadfa6)

http://soccer.htb/tiny/tinyfilemanager.php?p=

**user:12345**

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/576dfd30-5d9a-4fd6-9a52-35651a165ffb)

http://soccer.htb/tiny/tinyfilemanager.php?p=tiny%2Fuploads

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f115d39f-b164-4da2-9b39-abb2d80fb875)

http://soccer.htb/tiny/tinyfilemanager.php?p=tiny&view=tinyfilemanager.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/09f48646-41e5-45a4-888e-31ab38062dfe)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e6bf6ffd-563e-4d6c-aeaa-6383c9f3f05c)

```
searchsploit 'tiny file manager'
```

```
searchsploit -m 50828
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/100bfbb8-c7b7-4450-829c-3431857e1a6d)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/7f70c8e8-edd9-4b4e-ab03-6221c00dc211)

http://soccer.htb/tiny/tinyfilemanager.php?p=tiny%2Fuploads&view=php-reverse-shell.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/110f739d-2947-462e-b5fc-bff884d68fda)

http://soccer.htb/tiny/tinyfilemanager.php?p=tiny%2Fuploads&view=aaa.php

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1bdec955-f60c-487d-823a-4f400fa50828)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ea2ebdbf-737d-4505-974c-c4909041f14e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ffc19f49-68d8-4a86-bc62-9afd0fa00c5c)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9fbdcf57-f2c8-406b-b8f5-5adead166536)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e5c6b863-d516-4703-9fa5-3eb272101cb5)

```
cat /etc/nginx/sites-available/soc-player.htb
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1884319a-769b-473e-9056-813d1536a295)

```
server {
        listen 80;
        listen [::]:80;

        server_name soc-player.soccer.htb;

        root /root/app/views;

        location / {
                proxy_pass http://localhost:3000;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection 'upgrade';
                proxy_set_header Host $host;
                proxy_cache_bypass $http_upgrade;
        }

}
```

```
echo '10.129.208.236 soc-player.soccer.htb' |sudo tee -a /etc/hosts
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e04dc9c1-8b47-4e5b-a923-2ab19548393d)

http://soc-player.soccer.htb/

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/ed5df05c-fc0a-4e36-b5c8-41994eebedd7)
