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
	l=failist_lugemine(f)
	return l
