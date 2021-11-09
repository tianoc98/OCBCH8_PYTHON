
def konversi1(suhu,celvin = 273):
    '''
    Function ini untuk conversi kelvin ke celcius
    '''
    celcius = suhu - celvin
    print(celcius, " Celcius")
    print(suhu , " Kelvin ")
    return celcius
    
    
def konversi2(suhu,tipe):
    '''
    Function ini untuk conversi celvin / celcius ke fahrenheit
    '''
    print(konversi1.__doc__)
    tipe = tipe.lower()
    if tipe == "k":
        suhu = konversi1(suhu)
        suhuf = (9/5 * suhu) + 32
    elif tipe == "c":
        suhu = konversi1(suhu+273)
        suhuf = (9/5 * suhu) + 32
    else:
        print("Salah Input")
    return suhuf

def konversi3(suhu, tipe ,celvin = 273,celcius = 5/9 ):
    '''
    Function ini untuk conversi fahrenheit dari function konversi2() ke  celvin dan celcius
    '''
    suhuf = konversi2(suhu,tipe)
    print(konversi2.__doc__)
    print(suhuf , " Fahrenheit")
    print("==========================================================")
    print("CONVERTER FAHRENHEIT !")
    celcius = celcius * (suhuf -32)
    celvin = celcius + celvin
    print (celcius, " Celcius")
    print (celvin, " Kelvin")

print("MASUKAN SUHU : ")
suhu = int(input())
print("\n MASUKAN TIPE suhu yang di inputkan Celcius Atau Kelvin ( C/ K ) ")
tipe = input()
konversi3(suhu,tipe)
print(konversi3.__doc__)


