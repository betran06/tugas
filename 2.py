class orang:
    nama = "budi"
    
    def __init__(self):
        print('ini adalah constructior')
        
    def berjalan(self, nama):
        print(self.nama,"berjalan")
        print(nama,"berjalan")

person1 = orang()


