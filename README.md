# Jameh
```
Danilo Vaz - UNK
danilovazb@gmail.com
http://unk-br.blogspot.com
https://twitter.com/unknownantisec
```
### DESCRIPTION
```
Jameh, que na verdade se escreve e se lê 'Jamé' que do Tupi Guarani significa oculto, 
misterioso, tem como objetivo realizar um brute-force em hash de senhas contidas no /etc/shadow,
passando o salt do hash e a senha criptografada ele tenta por meio de dicionário quebrar a 
senha.
```
### REQUERIMENTS
```
 ----------------------------------------------------------
Import:
threading
time
crypt
argparse
sys
subprocess

permission          Reading & Writing
User                root privilege, or is in the sudoers group
Operating system    LINUX
Python              2.7
 ----------------------------------------------------------
```
### INSTALL
```
git clone http://github.com/danilovazb/jameh
```
### HELP
```
usage: jameh.py [-h] [-t 10] -f word_list.txt -s '$6$DgAOLzvU' -ha
                '$xw5oqFEZw30SSCdgD9KOiK2BG1J.O135BowUgdsUZB3ErEeZii6s1vC07BcBoPY06iNcJpxhQYTwzBpjVj7oq.'

optional arguments:
  -h, --help        show this help message and exit
  -t 10, --threads 10
                    Threads
  -f word_list.txt, --file word_list.txt
                    Opens file with passwords
  -s '$6$DgAOLzvU', --salt '$6$DgAOLzvU'
                    Salt, '$6$DgAOLzvU'
  -ha '$xw5oqFEZw30SSCdgD9KOiK2BG1J.O135BowUgdsUZB3ErEeZii6s1vC07BcBoPY06iNcJpxhQYTwzBpjVj7oq.', --hash '$xw5oqFEZw30SSCdgD9KOiK2BG1J.O135BowUgdsUZB3ErEeZii6s1vC07BcBoPY06iNcJpxhQYTwzBpjVj7oq.'
                    hash, '$xw5oqFEZw30SSCdgD9KOiK2BG1J.O135BowUgdsUZB3ErEeZii
                    6s1vC07BcBoPY06iNcJpxhQYTwzBpjVj7oq.'

```
### EXAMPLE
```
SENHA: s3nh42015!@#

~# cat /etc/shadow
root:!:16440:0:99999:7:::
daemon:*:16273:0:99999:7:::
bin:*:16273:0:99999:7:::
sys:*:16273:0:99999:7:::
sync:*:16273:0:99999:7:::
games:*:16273:0:99999:7:::
man:*:16273:0:99999:7:::
lp:*:16273:0:99999:7:::
mail:*:16273:0:99999:7:::
news:*:16273:0:99999:7:::
uucp:*:16273:0:99999:7:::
proxy:*:16273:0:99999:7:::
www-data:*:16273:0:99999:7:::
backup:*:16273:0:99999:7:::
list:*:16273:0:99999:7:::
irc:*:16273:0:99999:7:::
gnats:*:16273:0:99999:7:::
nobody:*:16273:0:99999:7:::
libuuid:!:16273:0:99999:7:::
syslog:*:16273:0:99999:7:::
messagebus:*:16273:0:99999:7:::
usbmux:*:16273:0:99999:7:::
dnsmasq:*:16273:0:99999:7:::
avahi-autoipd:*:16273:0:99999:7:::
kernoops:*:16273:0:99999:7:::
rtkit:*:16273:0:99999:7:::
saned:*:16273:0:99999:7:::
whoopsie:*:16273:0:99999:7:::
speech-dispatcher:!:16273:0:99999:7:::
avahi:*:16273:0:99999:7:::
lightdm:*:16273:0:99999:7:::
colord:*:16273:0:99999:7:::
hplip:*:16273:0:99999:7:::
pulse:*:16273:0:99999:7:::
danilo:$6$DgAOLzvU$Mt0WllW7AFJt5eFk0HPzjQNes/vvPkHaVmPIaWEb7K64uayPJ3CrEW8gjlBinh9Dzqj4RZXfRAN45XxrpWYjX.:16440:0:99999:7:::


~# python jameh.py --file wl.txt --threads 10 --salt '$6$DgAOLzvU' --hash '$Mt0WllW7AFJt5eFk0HPzjQNes/vvPkHaVmPIaWEb7K64uayPJ3CrEW8gjlBinh9Dzqj4RZXfRAN45XxrpWYjX.'


       _                      _     
      | |                    | |    
      | | __ _ _ __ ___   ___| |__  
  _   | |/ _` | '_ ` _ \ / _ \ '_ \ 
 | |__| | (_| | | | | | |  __/ | | |
  \____/ \__,_|_| |_| |_|\___|_| |_|
                                    
[+] Author: Danilo Vaz a.k.a. UNK
[+] http://github.com/danilovazb
[+] http://unk-br.blogspot.com.br

PASS: s3nh42015!@#
Terminado
```
