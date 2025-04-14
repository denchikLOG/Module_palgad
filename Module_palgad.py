1
p=[]
i=[]
def Lisa_andmd(p: list,i: list):
    try:
        nimi=input("nimi: ")
        if nimi.isalpha():
            try:
                palk=float(input("Palk: "))
            except:
                print("palk on arv!")
            p.append(palk)
            i.appned(palk)
            print("andmet on lisatud")
    except:
        print("Kirjuta ainult tähtede kasutades")
2
from Module_palgad import *
palgad=[1200,2500,750,395,1300]
inimesed=["A","B","C","D","E"]

while True:
    print("andmed:")
    print(inimesed)
    print(palgad)
    print("vajuta:\n1-Andmete lisameks\n2-Andmete kustutamiseks nime järgi")
    v=int(input())
    if v==1:
        k=int(input("mitu inimest? "))
        for i in range(k):
            lisa_andmed(palgad,inimesed)

3
def sorteerimine(p: list, i: list)-> any:
    v=input("Vali märk: > (kasvav) vöi (kahanev)")#try except? koos while true'ga
    for i in range(0, len(i)):
        for i in range(n, len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

4
töötajad=[("Martin",3000),("Irina",4000),("Oleg",2500),("Aleks",3500)]
madalaim_palk=töötajad[0]
for nimi,palk in töötajad:
    if palk<madalaim_palk[1]:
        madalaim_palk=(nimi,palk)
print(f"Madalaim palk on {madalaim_palk[0]}: {madalaim_palk[1]}")

5

töötajad=[("Martin",3000),("Irina",4000),("Oleg",2500),("Aleks",3500)]
töötajad_asc=sorted(töötajad,key=lambda x:x[1])
töötajad_desc=sorted(töötajad,key=lambda x:x[1],reverse=True)
print("Kasvavas järjekorras:")
for nimi,palk in töötajad_asc:
    print(f"{nimi}:{palk}")
print("\nKahanevas järjekorras:")
for nimi,palk in töötajad_desc:
    print(f"{nimi}:{palk}")

#12
def võrdlus(nimi):
    return nimi.lower()
def sorteeri(järjend,suund):
    if suund=="A":
        return sorted(järjend,key=võrdlus)
    elif suund=="Y":
        return sorted(järjend,key=võrdlus,reverse=True)
    else:
        print("Vale valik")
        return järjend
nimed=[]
for i in range(5):
    nimedd=input("Sisesta nimed: ")
    nimed.append(nimedd)
print("Sorteerimisviisid:")
print("A - A-st Y-ni")
print("Y - Y-st A-ni")
valik=input("Sisesta valik (A/Y):")
tulemus=sorteeri(nimed,valik)
print("Tulemus:")
for n in tulemus:
    print(n)

#15

def arvuta_palk(palk, aastad):
    protsent=0.05
    for _ in range(aastad):
        palk=palk*(1+protsent)
    return palk
algne=float(input("Sisesta töötaja algne palk: "))
t=int(input("Mitu aastat edasi soovid arvutada?: "))
uus_palk=arvuta_palk(algne, t)
print("Palk",t,"aasta pärast on:",uus_palk,"eurot")


#18


nimed=["Mati","Mari","Marko","Anna","Andres","Jüri","Maarja"]
palgad=[1200,1350,1500,1250,1400,1600,1100]
täht=input("Sisesta täht, millega nimi peab algama: ").capitalize()
leitud=False
for i in range(len(nimed)):
    if nimed[i].startswith(täht):
        print(nimed[i]+"-"+str(palgad[i])+"€")
        leitud=True
if not leitud:
    print("Nimesid, mis algavad tähega", täht, "ei leitud.")

#8

nimed=["Mati","Mari","Marko","Anna","Andres","Jüri","Maarja"]
palgad=[2200,3350,500,1250,5400,1600,1100]
piir=float(input("Sisesta palga piirsumma:"))
valik=input("Kas soovid näha neid, kes saavad rohkem (>) või vähem (<)? (>, <):")
leitud=False
for i in range(len(nimed)):
    if valik==">" and palgad[i]>piir:
        print(nimed[i]+" - "+str(palgad[i])+"€")
        leitud=True
    elif valik=="<" and palgad[i]<piir:
        print(nimed[i]+" - "+str(palgad[i])+"€")
        leitud=True
if not leitud:
    print("Ei leitud ühtegi töötajat selle tingimuse alusel.")


