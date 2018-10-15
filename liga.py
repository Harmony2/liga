import requests
import re
#import sys

total = 0
ind = []
notf = []

def getprice(card):
	global notf
	global total
	global ind
	card = card.replace(' ','+')
	r = requests.get("https://ligamagic.com.br/?view=cards%"+"2Fsearch&card=%s"%card)
	s = r.text
	price = re.search(r"precos-menor'>R\$ (.*?) <", s)
	try:
		p = price[1]
		p = p.replace(',','.')
		total += float(p)
		ind.append([card,p])
		return(p)
	except:
		notf.append(card)

def getlist(arq):
	f = open(arq,'r')
	s = f.read()
	f.close()
	s = s.split('\n')
	return s

lista = getlist('deck.txt')
c = 1
for i in lista:
	print('%s/%s'%(c,len(lista)))
	getprice(i)
	c+=1
print('\ntotal price: R$:%s'%total)

for i in ind:
	print(i[0], i[1])
print('\nNot found:')
for i in notf:
	print(i)

def ask():
	if input('\n\nquit? (y)\n') == "y":
		quit()
	else:
		ask()
ask()