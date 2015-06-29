# -*- coding: utf-8 -*-
 
import threading,time,crypt,argparse,sys,subprocess
 
def decrypt_hash(senha,salt,p_hash):
	hash_full = "%s%s" % (salt,p_hash)
	temp_pass = crypt.crypt(senha,salt)
	if hash_full == temp_pass:
		print "PASS: %s" % senha
		subprocess.call("pkill -f 'jameh.py'", shell=True)  
	else:
		pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog='jameh.py', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=20))
	parser.add_argument("-t","--threads", help = "Threads", metavar= "10", default=1)
	parser.add_argument("-f","--file", help = "Opens file with passwords", metavar = "word_list.txt", required=True)
	parser.add_argument("-s","--salt", help = "Salt, \'$6$DgAOLzvU\'", metavar = "\'$6$DgAOLzvU\'", required=True)
	parser.add_argument("-ha","--hash", help = "hash, \'$xw5oqFEZw30SSCdgD9KOiK2BG1J.O135BowUgdsUZB3ErEeZii6s1vC07BcBoPY06iNcJpxhQYTwzBpjVj7oq.\'", metavar = "\'$xw5oqFEZw30SSCdgD9KOiK2BG1J.O135BowUgdsUZB3ErEeZii6s1vC07BcBoPY06iNcJpxhQYTwzBpjVj7oq.\'", required=True)
	args = parser.parse_args()
	threads = args.threads
	arquivo = args.file
	salt = args.salt
	p_hash = args.hash
	print """
       _                      _     
      | |                    | |    
      | | __ _ _ __ ___   ___| |__  
  _   | |/ _` | '_ ` _ \\ / _ \\ '_ \\ 
 | |__| | (_| | | | | | |  __/ | | |
  \\____/ \\__,_|_| |_| |_|\\___|_| |_|
                                    
[+] Author: Danilo Vaz a.k.a. UNK
[+] http://github.com/danilovazb
[+] http://unk-br.blogspot.com.br
"""
	lista_threads = []
	with open(arquivo, 'rb') as arquivo:
		for linha in arquivo:
	    		senha = linha.strip()
	        	while threading.active_count() > threads:
		        	time.sleep(1)
		        thread = threading.Thread(target=decrypt_hash, args=(senha,salt,p_hash,))
		        lista_threads.append(thread)
		        thread.start()
	 
	for thread in lista_threads:
		thread.join()
