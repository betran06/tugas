class mobilelegend:
    silsilah = "hybrid"
    diamond = 1000

    def login(self):
        print("mobilelegend login")
        
class Nickname(mobilelegend):
     def cetaksilsilah(self):
         print(self.silsilah)

class Gift(mobilelegend):
    def kirim(self, jl_kirim):
        return self.diamond - jl_kirim

nickname1 = Nickname()
nickname1.cetaksilsilah()
nickname1.login()

gift1 = Gift()
sisadiamond = gift1.kirim(500)
print(sisadiamond)
