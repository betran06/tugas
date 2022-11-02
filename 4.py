class Ayah:
    silsilah = "panbudi"

    def berjalan(self):
        print("Ayah berjalan jinjit")

class Anak(Ayah):

    def cetaksilsilah(self):
        print(self.silsilah)

    def anakberjalan(self):
        super().berjalan()
        print("anak berjalan lurus")

anak1 = Anak()
anak1.cetaksilsilah()
anak1.anakberjalan()
