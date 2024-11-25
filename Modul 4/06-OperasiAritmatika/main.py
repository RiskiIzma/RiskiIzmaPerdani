# Operasi aritmatika

a = 10
b = 3

# operasi penjumlahan (TAMBAH)
print("====TAMBAH====")
hasil = a + b
print(a,"+",b,"=",hasil)

# Operasi pengurangan (KURANG)
print("====KURANG====")
hasil = a - b
print(a,"-",b,"=",hasil)

# Operasi perkalian (KALI)
print("====KALI====")
hasil = a * b
print(a,"*",b,"=",hasil)

# Operasi pembagian (BAGI)
print("====BAGI====")
hasil = a / b
print(a,"/",b,"=",hasil)

# Operasi pemangkatan (EXPONENTIAL)
print("====PANGKAT====")
hasil = a ** b
print(a,"**",b,"=",hasil)

# Operasi sisa pembagian (MODULUS)
print("====MODULUS====")
hasil = a % b
print(a,"%",b,"=",hasil)

# Operasi floor devision
print("====FLOOR DEVISION====")
hasil = a // b
print(a,"//",b,"=",hasil)

# prioritas perhitungan (operasi)
"""
    1.()
    2.perkalian, pembagian, dll */**%//
    3.penjumlahan dan pengurangan +-
"""

x = 3
y = 4
z = 2

hasil = x**z * y + x /z - z % y // x
print(x, "**" ,z, "*" ,y, "+" ,x, "/" ,z, "-" ,z, "%" ,y, "//" ,x, "=" , hasil)

hasil = x + y * z
print(x, "+" ,y, "*",z, "=", hasil)
hasil = (x + y) * z
print("(,x, "+",y,)","*",z, "=", hasil )
"""
"""