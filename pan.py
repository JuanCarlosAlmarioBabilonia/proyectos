pan=tuple(("PAN BLANCO", "PAN INTEGRAL", "PAN DE CENTENO", "BAGUETTES", "PANECILLOS", "PAN DE AJO", "PAN DE OLIVA", "PAN DE MAIZ", "PAN ARABE", "PAN ESPELTA"))
prec_pan=tuple((2500, 2800, 3200, 3500, 4500, 2300, 3500, 4300, 4000, 2500))
bolleria=tuple(("DONAS", "CROISSANTS", "NAPOLITANAS", "CARACOLA", "CRESTA", "TARTEL", "MARAÑUELA", "MUJI", "TRENZA", "CONSAIMADA"))
prec_boll=tuple((3500, 2000, 3400, 2800, 4500, 3600, 2700, 3000, 3200, 2100))
tartas=tuple(("TARTA MOUSSE DE CHOCOLATE", "TARTA DE FRESA", "CHEESECAKE DE NUTELLA","TORTA HOJALDRE CON FRESA", "BANANA CREAM PIE", "CHEESECAKE DE JENGIBRE", "TARTA DE TRES CHOCOLATES", "TARTA FINA DE MANZANA", "TARTA ARABE", "TARTA DE PERAS"))
prec_tarta=tuple((6500, 8000, 7500, 8400, 9000, 14000, 7500, 8700, 12000, 6300))


op=int(input("¿A que categoria te interesa entrar? Ingrese (1) para PAN, ingrese (2) para BOLLERIA o ingrese (3) para TARTAS: "))
if op==1:
    print ("PAN")
for i, val in enumerate(pan):
    print(f"{i}. {val} ${prec_pan[i]}")
de =int(input("¿Te gustaria comprar algun producto de esta lista?(Digite (1) para SI, digite (2) para NO "))
if de==1:
    print ("¿Ingresa el numero del producto que deseas adquirir?")
    xd=int(input())
elif de==2:
    print ("Ok")
opc=int(input("¿A que categoria te interesa entrar? Ingrese (1) para PAN, ingrese (2) para BOLLERIA o ingrese (3) para TARTAS"))  
for i, val in enumerate(bolleria):
    print(f"{i}. {val} ${prec_boll[i]}")
dec=int(input("¿Te gustaria comprar algun producto de esta lista?(Digite (1) para SI, digite (2) para NO "))
if dec==1:
    print ("¿Cual te gustaria comprar?")
elif dec==2:
    print ("Ok")
opz=int(input("¿A que categoria te interesa entrar? Ingrese (1) para PAN, ingrese (2) para BOLLERIA o ingrese (3) para TARTAS"))
for i, val in enumerate(tartas):
    print(f"{i}. {val} ${prec_tarta[i]}")
deb=int(input("¿Te gustaria comprar algun producto de esta lista?(Digite (1) para SI, digite (2) para NO "))
if deb==1:
    print ("¿Cual te gustaria comprar?")
elif deb==2:
    print ("Ok")