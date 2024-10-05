# A Mass SSH Scanner
Scan SSH opened IPs and check their login

# Usage
```
 ___    ___  _____  __ __     __ ___  __     __________  ___  __________ 
||=||   || \/ ||=||(( ((     (( ((||==||    (((  ||=|||\\|||\\|||==||_// 
|| ||   ||    || |\_)\_))   \_)\_)||  ||   \_)\\_|| ||| \||| \|||__|| \\

usage: main.py [-h] [--targets TARGETS] [--max-rate MAX_RATE] [--disable-combo] [--disable-user-pass] [--worker-size WORKER_SIZE] [--output OUTPUT]

A Mass SSH Scanner

options:
  -h, --help            show this help message and exit
  --targets TARGETS     A path to targets file (default is targets.txt)
  --max-rate MAX_RATE   Max rate of packets per second (default is 1000)
  --disable-combo       If combo will be used to dictionary attack
  --disable-user-pass   If user:pass from user.txt and password.txt will be used to dictionary attack
  --worker-size WORKER_SIZE
                        Worker size for dictionary attacking (default is 50)
  --output OUTPUT       output (default is True)
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
