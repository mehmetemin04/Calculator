
def calculator ():
    
      
    try: 
        islemSayisi = int(input("İşlem sayısı: "))
    
    except:
        raise TypeError("Lütfen programı yeniden başlatıp geçerli bir sayı giriniz.")
        
    
    c = 0 
    while c < islemSayisi :
        
        
            islem = input("işlem giriniz (+-*/): ")  
        
            if islem not in ("+","-","*","/"):
                print("Lütfen geçerli bir işlem giriniz.")
                continue
            
            a = int(input("İlk sayıyı giriniz: "))
            b = int(input("İkinci sayıyı giriniz: "))
        
        
            if islem == "+":
                print(str(a) + " + " + str(b) + " = " + str(a+b))
            elif islem == "-":
                print(str(a) + " - " + str(b) + " = " + str(a-b))
            elif islem == "*":
                print(str(a) + " * " + str(b) + " = " + str(a*b))
            elif islem == "/":  
                if b == 0:
                    print("Sayılar 0'a bölünmez.")
                else:
                    print(str(a) + " / " + str(b) + " = " + str(a/b))

            c += 1
    
calculator()    
    
    
    
    
