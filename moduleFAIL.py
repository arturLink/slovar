import os
from gtts import gTTS
import random

def failist_lugemine(f:str,l:list):
	fail=open(f,"r",encoding="utf-8-sig") #encoding="utf-8-sig"
	for rida in fail:
		l.append(rida.strip()) #"\n"
	fail.close()
	return l

def failisse_salvestamine(f:str,l:list):
	fail=open(f,"w",encoding="utf-8-sig")
	for el in l:
		fail.write(el+"\n")
	fail.close()

def rida_salvestamine(f:str,rida:str):
	fail=open(f,"a",encoding="utf-8-sig")
	fail.write(rida+"\n")
	fail.close()

def uus_sona(f:str,rida:str)->list:
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")
	l=failist_lugemine(f) #mozet stro4ki ubrat
	return l

def tolkimine(l1:list,l2:list):
	sona=input("Translate?: ")
	if sona in l1:
		tolk=l2[l1.index(sona)]
		print(sona+"-"+tolk)
	elif sona in l2:
		tolk=l1[l2.index(sona)]
		print(sona+"-"+tolk)
	else:
		print("This word is missing from dictionary")

def heli(text:str,keel:str):
	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
	os.system("heli.mp3")

def correction(sona:str,l:list):
	for i in range(len(l)):
		if l[i]==sona:
			uus_sona=sona.replace(sona,input("Uus sona"))
			l.insert(i,uus_sona)
			l.remove(sona)
	return l


def cntr_trnsl(word:str,spisk:list):
	a=True
	if word not in spisk:
		a=False
	return a