# A Mass SSH Scanner
Scan SSH opened IPs and check their login

# Usage
```
 ___    ___  _____  __ __     __ ___  __     __________  ___  __________ 
||=||   || \/ ||=||(( ((     (( ((||==||    (((  ||=|||\\|||\\|||==||_// 
|| ||   ||    || |\_)\_))   \_)\_)||  ||   \_)\\_|| ||| \||| \|||__|| \\

usage: main.py [-h] [--targets TARGETS] [--max-rate MAX_RATE] [--disable-combo] [--disable-user-pass] [--worker-size WORKER_SIZE]
               [--disable-output] [--error-verbose] [--discord-webhook DISCORD_WEBHOOK]

A Mass SSH Scanner

options:
  -h, --help            show this help message and exit
  --targets TARGETS     A path to targets file (default is targets.txt)
  --max-rate MAX_RATE   Max rate of packets per second (default is 1000)
  --disable-combo       If combo will be used to dictionary attack
  --disable-user-pass   If user:pass from user.txt and password.txt will be used to dictionary attack
  --worker-size WORKER_SIZE
                        Worker size for dictionary attacking (default is 50)
  --disable-output      output (default is True)
  --error-verbose       error verbose (default is True)
  --discord-webhook DISCORD_WEBHOOK
                        discord webhook to send hit notification
```

# Samples
### Default config
```
main.py
```
### Disable user/pass attacking and speicfy the path to target list
```
main.py --disable-user-pass --targets test.txt
```
### Send discord notification via webhook on hit
```
main.py --discord-webhook "https://discord.com/api/webhooks/..."
```

# Requirements
- masscan
- Python 3.12.1 (TESTED)
