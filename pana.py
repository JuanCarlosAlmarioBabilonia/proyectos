pan=tuple(("PAN BLANCO", "PAN INTEGRAL", "PAN DE CENTENO", "BAGUETTES", "PANECILLOS", "PAN DE AJO", "PAN DE OLIVA", "PAN DE MAIZ", "PAN ARABE", "PAN ESPELTA", "NINGUNO"))
prec_pan=tuple((2500, 2800, 3200, 3500, 4500, 2300, 3500, 4300, 4000, 2500, 0))
bolleria=tuple(("DONAS", "CROISSANTS", "NAPOLITANAS", "CARACOLA", "CRESTA", "TARTEL", "MARAÑUELA", "MUJI", "TRENZA", "CONSAIMADA", "NINGUNO"))
prec_boll=tuple((3500, 2000, 3400, 2800, 4500, 3600, 2700, 3000, 3200, 2100, 0))
tartas=tuple(("TARTA MOUSSE DE CHOCOLATE", "TARTA DE FRESA", "CHEESECAKE DE NUTELLA","TORTA HOJALDRE CON FRESA", "BANANA CREAM PIE", "CHEESECAKE DE JENGIBRE", "TARTA DE TRES CHOCOLATES", "TARTA FINA DE MANZANA", "TARTA ARABE", "TARTA DE PERAS", "NINGUNO"))
prec_tarta=tuple((6500, 8000, 7500, 8400, 9000, 14000, 7500, 8700, 12000, 6300, 0))
print ("Estas en la categoria PAN, ingresa el numero del producto que deseas adquirir. En caso contrario, digite (10)")
for i, val in enumerate(pan):
    print(f"{i}. {val} ${prec_pan[i]}")
xd=int(input())
print ("¿Cuantas unidades de este producto deseas adquirir? Si su respuesta anterior fue NINGUNO, digite (0)")
canp=int(input())
precp=prec_pan[xd]*canp
desc=int((prec_pan[3]*canp)*0.1)
vdes=int((precp-desc))
descp=int((prec_pan[8]*canp)*0.15)
vdesp=int((precp-descp))
print (f"Has adquirido",canp,f"unidades de {pan[xd]} con un valor de $",precp)
if xd==3:
    print(f"Has obtenido un descuento de 10% en {pan[3]}, el precio con descuento de este producto es $", vdes)
    precp=vdes
if xd==8:
    print(f"Has obtenido un descuento de 15% en {pan[8]}, el precio con descuento de este producto es $", vdesp)
    precp=vdesp
print ("Estas en la categoria BOLLERIA, ingresa el numero del producto que deseas adquirir. En caso contrario, digite (10)")
for i, val in enumerate(bolleria):
    print(f"{i}. {val} ${prec_boll[i]}")
xs=int(input())
print ("¿Cuantas unidades de este producto deseas adquirir? Si su respuesta anterior fue NINGUNO, digite (0)")
cano=int(input())
preco=prec_boll[xs]*cano
desa=int((prec_boll[1]*cano)*0.2)
vdesa=int((preco-desa))
desb=int((prec_boll[5]*cano)*0.4)
vdesb=int((preco-desb))
print (f"Has adquirido",cano,f"unidades de {bolleria[xs]} con un valor de $",preco)
if xs==1:
    print(f"Has obtenido un descuento de 20% en {bolleria[1]}, el precio con descuento de este producto es $", vdesa)
    preco=vdesa
if xs==5:
    print(f"Has obtenido un descuento de 40% en {bolleria[5]}, el precio con descuento de este producto es $", vdesb)
    preco=vdesb
    
print ("Estas en la categoria TARTAS, ingresa el numero del producto que deseas adquirir. En caso contrario, digite (10)")
for i, val in enumerate(tartas):
    print(f"{i}. {val} ${prec_tarta[i]}")
xm=int(input())
print ("¿Cuantas unidades de este producto deseas adquirir? Si su respuesta anterior fue NINGUNO, digite (0)")
cand=int(input())
precd=prec_tarta[xm]*cand
desy=int((prec_tarta[9]*cand)*0.25)
vdesy=int((precd-desy))
desx=int((prec_tarta[4]*cand)*0.35)
vdesx=int((precd-desx))
print (f"Has adquirido",cand,f"unidades de {tartas[xm]} con un valor de $",precd)
if xm==1:
    print(f"Has obtenido un descuento de 25% en {tartas[9]}, el precio con descuento de este producto es $", vdesy)
    precd=vdesy
if xm==5:
    print(f"Has obtenido un descuento de 35% en {tartas[5]}, el precio con descuento de este producto es $", vdesx)
    precd=vdesx
cuenta=precp+preco+precd
print ("Su cuenta da un total de $",cuenta)
dinero=int(input("Ingrese la cantidad de dinero que posee "))
vueltos=dinero-cuenta
if dinero>=cuenta:
    print("Recibe de vueltos $",vueltos)
else:
    print(f"Su dinero no alcanza, le faltan $ {-vueltos}")