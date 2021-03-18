# https://el.wikipedia.org/wiki/%CE%9A%CF%8E%CE%B4%CE%B9%CE%BA%CE%B1%CF%82_%CF%84%CE%BF%CF%85_%CE%9A%CE%B1%CE%AF%CF%83%CE%B1%CF%81%CE%B1
def encrypt_ceasar(plain_text,key):
    cipher_text=''

    for letter in plain_text:
        
        # μετατροπή του γράμματος σε αριθμό
        #((A=0,B=1,...Z=25)
        
        num=ord(letter) - ord("A")

        # δεξιά μετατόπιση του αριθμού κατά key θέσεις.
        met=(num+key)%26
        # met = (num-key)%26 για δεξιά μετατόπιση

        # μετατροπή του τελικού αριθμού σε γράμμα.
        # (0=Α,1=Β,...25=Ζ)
        
        ch = chr(met+ord('A'))

        # το τελικό κείμενο προκύπτει από την προσθήκη γραμμάτων
        cipher_text=cipher_text +ch
    # έξοδος από η συνάρτηση, επιστροφή του κρυπτογραφημένου κειμένου
    return cipher_text

def main():
    text=input("Give your plain text")
    key=int(input("give your key"))
    encrypted=encrypt_ceasar(text,key)
    print("The encrypted text is:",encrypted)

if __name__=='__main__':
    main()
    

######################### ΔΟΚΙΜΑΣΤΙΚΑ ΔΕΔΟΜΕΝΑ #########################3
#key=3
#text='ABC'     ->DEF
#ord(A)=65
#ord(A) - ord(A)=65-65=0
#ord(B)-ord(A)=66-65=1
#ord(C)-ord(A)=67-65=2

#met=(0+3)%26 = 3
#met=(1+3)% 26=4
#met=(2+3)%26=5  
