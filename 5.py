class kendaraan:
    silsilah = "honda"
    
    def berjalan(self):
        print("kendaraan berjalan")

class Mobil(kendaraan):
    def cetaksilsilah(self):
        print(self.silsilah)

mobil1 = Mobil()
mobil1.cetaksilsilah()
mobil1.berjalan()
