pan=tuple(("PAN BLANCO", "PAN INTEGRAL", "PAN DE CENTENO", "BAGUETTES", "PANECILLOS", "PAN DE AJO", "PAN DE OLIVA", "PAN DE MAIZ", "PAN ARABE", "PAN ESPELTA"))
prec_pan=tuple((2500, 2800, 3200, 3500, 4500, 2300, 3500, 4300, 4000, 2500))
bolleria=tuple(("DONAS", "CROISSANTS", "NAPOLITANAS", "CARACOLA", "CRESTA", "TARTEL", "MARAÑUELA", "MUJI", "TRENZA", "CONSAIMADA"))
prec_boll=tuple((3500, 2000, 3400, 2800, 4500, 3600, 2700, 3000, 3200, 2100))
tartas=tuple(("TARTA MOUSSE DE CHOCOLATE", "TARTA DE FRESA", "CHEESECAKE DE NUTELLA","TORTA HOJALDRE CON FRESA", "BANANA CREAM PIE", "CHEESECAKE DE JENGIBRE", "TARTA DE TRES CHOCOLATES", "TARTA FINA DE MANZANA", "TARTA ARABE", "TARTA DE PERAS"))
prec_tarta=tuple((6500, 8000, 7500, 8400, 9000, 14000, 7500, 8700, 12000, 6300))

print ("Estas en la categoria PAN, ingresa el numero del producto que deseas adquirir")
for i, val in enumerate(pan):
    print(f"{i}. {val} ${prec_pan[i]}")
xd=int(input())
desc=int((prec_pan[3]*0.1))
vdes=int((prec_pan[3]-desc))
descp=int((prec_pan[8]*0.15))
vdesp=int((prec_pan[8]-descp))
print (f"Has adquirido {pan[xd]} con un valor de ${prec_pan[xd]}")
if xd==3:
    print(f"Has obtenido un descuento de 10% en {pan[3]}, el precio con descuento de este producto es $", vdes)
if xd==8:
    print(f"Has obtenido un descuento de 10% en {pan[8]}, el precio con descuento de este producto es $", vdesp)


print ("Estas en la categoria BOLLERIA, ingresa el numero del producto que deseas adquirir")
for i, val in enumerate(bolleria):
    print(f"{i}. {val} ${prec_boll[i]}")
xs=int(input())
desa=int((prec_boll[1]*0.2))
vdesa=int((prec_boll[1]-desa))
desb=int((prec_boll[5]*0.4))
vdesb=int((prec_boll[5]-desb))
print (f"Has adquirido {bolleria[xs]} con un valor de ${prec_boll[xs]}")
if xs==1:
    print(f"Has obtenido un descuento de 20% en {bolleria[1]}, el precio con descuento de este producto es $", vdesa)
if xs==5:
    print(f"Has obtenido un descuento de 40% en {bolleria[5]}, el precio con descuento de este producto es $", vdesb)


print ("Estas en la categoria TARTAS, ingresa el numero del producto que deseas adquirir")
for i, val in enumerate(tartas):
    print(f"{i}. {val} ${prec_tarta[i]}")
xm=int(input())
desy=int((prec_tarta[9]*0.25))
vdesy=int((prec_tarta[9]-desy))
desx=int((prec_tarta[4]*0.35))
vdesx=int((prec_tarta[4]-desx))
print (f"Has adquirido {tartas[xm]} con un valor de ${prec_tarta[xm]}")
if xm==1:
    print(f"Has obtenido un descuento de 25% en {tartas[9]}, el precio con descuento de este producto es $", vdesy)
if xm==5:
    print(f"Has obtenido un descuento de 35% en {tartas[5]}, el precio con descuento de este producto es $", vdesx)
cuenta=prec_boll[xs]+prec_pan[xd]+prec_tarta[xm]
print ("Su cuenta da un total de $",cuenta)
dinero=int(input("Ingrese la cantidad de dinero que posee "))
vueltos=dinero-cuenta
if dinero>=cuenta:
    print("Recibe de vueltos $",vueltos)
else:
    print(f"Su dinero no alcanza, le faltan $ {-vueltos}")