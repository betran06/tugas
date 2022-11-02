class Uang:
    def __init__(self,nominal):
        self._nominal = nominal

    def _belanja (self,totalBelanja):
        print("terima kasih. sisa uang anda adalah:")
        print(self._nominal - totalBelanja)

class Koin(Uang):
    def __init__(self,bahan):
        self.bahan = bahan
        
    def beli(self, totalBeli):
        print("terima kasih. sisa uang anda adalah:")
        print(self._nominal - totalBeli)


uang1 = Uang(10000)
uang1._belanja(5000)
koin1 = Koin("logam")
koin1._nominal = 1000
koin1.beli(500)
