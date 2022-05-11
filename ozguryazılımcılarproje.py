import random
def toplanan():
    b_t=random.randint(1,100)#b_t birinci toplanan           
    i_t=random.randint(1,100)#i_t ikinci toplanan  
    u_t=random.randint(1,100)#u_t üçüncü toplanan
    h_p=b_t+i_t+u_t #h_p harcadığı para
    t_p=random.randint(h_p,300)#t_p toplam para
    iListe=["Kerem","Mete","Ayşe","Çınar","Serkan"]#iListe anlamı isim listesi
    b_i=random.choice(iListe)#birinci isim
    aListe=["Manga","Anime CD","Harry Potter Kitabı","Oyun Karakteri Aksiyon Figürü","Pokemon T-shirt"]#alınanlar listesi
    b_a=random.choice(aListe)#birinci alınan
    aListe.remove(b_a)
    i_a=random.choice(aListe)#ikinci alınan
    aListe.remove(i_a)
    u_a=random.choice(aListe)#üçüncü alınan
    print("{0}'in cüzdanında {1} TL vardır.".format(b_i,t_p))
    print("{0} TL ile {3}, {1} TL ile {4}, {2} TL ile {5} aldı.".format(b_t,i_t,u_t,b_a,i_a,u_a))
    print("{0}'in cüzdanında kaç TL kalmıştır?".format(b_i))
