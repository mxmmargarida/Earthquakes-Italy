import urllib2  
website = urllib2.urlopen('http://cnt.rm.ingv.it/') 

from bs4 import BeautifulSoup
soup = BeautifulSoup(website)

f=open('teste.txt','w')
for string in soup.stripped_strings:
	f.write(repr(string))
f.close()
f=open('teste.txt','r')
a=f.readline()
f.close()

aux=a.find('Distretto Sismico')
a=a[aux+20:]
aux=a.find('u')
a=a[aux+2:]
# data 'u' hora 'u' lat 'u' long 'u' prof 'u' mag 'u' local
DADOS = []
for n in range(15):
  DADOS.append([])
  for m in range(7):
	if m==6:
		aux = a.find('722')
		DADOS[n].append(a[:aux-3])
		a=a[aux:]
		aux = a.find('u')
		a=a[aux+2:]
	else:
		aux = a.find('u')
		if m!=2 and m!=3:# remove lat and long information
			if m==1: # add 2 hours (hour in Italy)
				text = a[:aux-1]
				aux_text = (int(text[:2])+2)%24 
				# horas modulo 24
				if int(text[:2])+2>=24: # new day
					DADOS[n][0]=DADOS[n][0][:8]+str(int(DADOS[n][0][8:])+1) 
					# missing code to solve the issue of adding two hours to the last day of a certain month
				aux_text = str(aux_text)
				if len(aux_text)==1:
					aux_text='0'+aux_text
				text = aux_text+text[2:]
				DADOS[n].append(text)
			else:
				DADOS[n].append(a[:aux-1])
		a=a[aux+2:]
for i in range(15):	print DADOS[i] 
