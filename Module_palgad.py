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
            Lisa_andmed(palgad,inimesed)
