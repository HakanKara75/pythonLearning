class HarfSayaci:
    def __init__(self):
        self.sesli_harfler="aeıioöuü"
        self.sayac=0

        def kelime_sor(self):
            return input("bir kelime girin: ")
        def seslidir(self, harf):
            return harf in self.sesli_harfler
        def sessizdir(self, harf):
            return harf in self.sessiz_harfler
        def artif(self):
            for harf in self.kelime:
             if self.seslidir(harf):
                self.sayac+=1
                if self.sessizdir(harf):
                    self.sayac_sessiz+=1
                return (self.sayac_sesli, self.sayac_sessiz)

            def ekrana_yaz(self):
                mesaj="{} kelimesinde {} sesli harf var."
                sesli_harf_sayisi=self.artir()
                print(mesaj.format(self.kelime, sesli_harf_sayisi))

                def calistir(self):
                    self.kelime=self.kelime_sor()
                    self.ekrana_yaz()

                    if __name__=="__main__":
                        sayac=HarfSayaci()
                        sayac.calistir()