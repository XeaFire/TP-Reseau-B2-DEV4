# Plop bienvenue sur le TP 4 DEV

## I. Simple bs program

**Le serveur a comme ip : 5.5.5.11**
**Le client a comme ip : 5.5.5.12**

### 🌞 Commandes...

``` bash
[tristan@server TP-Reseau-B2-DEV4]$ git clone https://github.com/XeaFire/TP-Reseau-B2-DEV4.git 
```

```bash 
[tristan@server TP-Reseau-B2-DEV4]$ sudo firewall-cmd --add-port=13337/tcp --permanent 
```

```bash 
[tristan@server TP-Reseau-B2-DEV4]$ sudo firewall-cmd --reload
```

```bash
[tristan@server TP-Reseau-B2-DEV4]$ python bs_server_I1.py
Connected by ('5.5.5.12', 47428)
Données reçues du client : b'Meowwwww'
```

```bash
[tristan@client TP-Reseau-B2-DEV4]$ python bs_client_I1.py
b'Hi mate !'
```

```bash
[tristan@server TP-Reseau-B2-DEV4]$ ss -lnpt | grep "13337"
LISTEN 0      1           5.5.5.11:13337      0.0.0.0:*    users:(("python",pid=14610,fd=3))
```