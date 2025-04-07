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


def sorteerimine(p: list, i: list)-> any:
    v=input("Vali märk: > (kasvav) vöi (kahanev)")#try except? koos while true'ga
    for i in range(0, len(i)):
        for i in range(n, len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

def võrdsed_palgad(p:list, i: list):
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"saab kätte {i[ind]}")
                ind+=1

