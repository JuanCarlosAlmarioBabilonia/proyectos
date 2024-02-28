inicio=dict({
    "PANES":{
        "Producto":list([
           {"Nombre": "PAN BLANCO", "cuesta":3200}, 
           {"Nombre": "PAN INTEGRAL", "cuesta":2800}, 
           {"Nombre": "PAN DE CENTENO", "cuesta":3500}, 
           {"Nombre": "BAGUETTES", "cuesta":2400}, 
           {"Nombre": "PAN PANECILLOS", "cuesta":1000}, 
           {"Nombre": "PAN DE AJO", "cuesta":4000}, 
           {"Nombre": "PAN DE OLIVA", "cuesta":4500},
           {"Nombre": "PAN DE MAIZ", "cuesta":5500}, 
           {"Nombre": "PAN ARABE", "cuesta":5000}, 
           {"Nombre": "PAN ESPELTA", "cuesta":5700}, 
        ]),
        "Promociones":list([
           {"Codigo": 4, "descuento": "Descuento A", "valor":0.2}, 
           {"Codigo": 8, "descuento": "Descuento B", "valor":0.15},
        ]),
    },
    "BOLLERIA":{
        "Producto":list([
           {"Nombre": "DONAS", "cuesta":2500},
           {"Nombre": "CROAISSANTS", "cuesta":2800},
           {"Nombre": "NAPOLITANAS", "cuesta":3300},
           {"Nombre": "CARACOLA", "cuesta":4500},
           {"Nombre": "CRESTA", "cuesta":4000},
           {"Nombre": "TARTEL", "cuesta":5000},
           {"Nombre": "MARAÑUELA", "cuesta":4800},
           {"Nombre": "MUJI", "cuesta":3700},
           {"Nombre": "TRENZA", "cuesta":3100},
           {"Nombre": "CONSAIMADA", "cuesta":4200},
        ]),
        "Promociones":list([
           {"Codigo": 1, "descuento": "Descuento C", "valor":0.18},
           {"Codigo": 4, "descuento": "Descuento D", "valor":0.2}, 
        ]),
    },
    "TARTAS":{
        "Producto":list([
           {"Nombre": "TARTA MOUSSE DE CHOCOLATE", "cuesta":14000},
           {"Nombre": "TARTA DE FRESA", "cuesta":12000},
           {"Nombre": "CHEESECAKE DE NUTELLA", "cuesta":9000},
           {"Nombre": "TORTA DE HOJALDRE CON FRESA", "cuesta":7500},
           {"Nombre": "BANANA CREAM PIE", "cuesta":8300},
           {"Nombre": "CHEESECAKE DE JENGIBRE", "cuesta":9000},
           {"Nombre": "TARTA DE TRES CHOCOLATES", "cuesta":13000},
           {"Nombre": "TARTA FINA DE MANZANA", "cuesta":15000},
           {"Nombre": "TARTA ARABE", "cuesta":10000},
           {"Nombre": "TARTA DE PERAS", "cuesta":12000},
          ]),
          "Promociones":list([
           {"Codigo": 7, "descuento": "Descuento E", "valor":0.1},
           {"Codigo": 9, "descuento": "Descuento F", "valor":0.25}, 
        ]),
    },
})

print ("Seleccione la categoria en la que desea comprar: ")
listac=list(inicio.keys())
for i, val in enumerate(inicio.keys()):
    print(f"{i}. {val}")
opcion=int(input())
datosc=inicio.get(listac[opcion])
productos=datosc.get("Producto")
print (f"Seleccione el producto de la categoria {listac[opcion]} en la que desea comprar: ")
for i, val in enumerate(productos):
    name=val["Nombre"]
    value=val["cuesta"]
    print(f"{i} {name} con precio de ${value}")
op_pr=int(input())
mostrarn = productos[op_pr].get("Nombre")
datosc=inicio.get(listac[opcion])
promociones=datosc["Promociones"]
print ("¿Cuantas unidades del producto deseas comprar?")
cant=int(input())
promo=list()
for val in promociones:
    if (val.get("Codigo") == op_pr):
        promo.append(val)
desc=val["descuento"]
vale=val["valor"]
code=val["Codigo"]
ds=int(vale*100)
mul=value*cant
prec_a=mul * vale
prec_b=mul - prec_a
if (len(promo)== 0):
    print (f"No hay promociones disponibles para {mostrarn}")
    print ("VALOR A PAGAR : $",mul)
else:
    print(f"El producto {mostrarn} tiene {desc} del",ds,"% de descuento")
    print("Valor regular: $",mul,)
    print("VALOR A PAGAR CON DESCUENTO: $",int(prec_b))
    mul=int(prec_b)

dinero=int(input ("Ingrese la cantidad de dinero que tiene para pagar $"))
vueltosn=dinero-mul
vueltosd=dinero-int(prec_b)
if dinero>=mul:
     print("Recibe de vueltos $",vueltosn)
else:
    print(f"Su dinero no alcanza, le faltan $ {-vueltosn}")