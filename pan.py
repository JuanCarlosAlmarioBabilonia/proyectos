inicio=dict({
    "PANES":{
        "Producto":list([
           {"Nombre": "PAN BLANCO", "$":3200}, 
           {"Nombre": "PAN INTEGRAL", "$":2800}, 
           {"Nombre": "PAN DE CENTENO", "$":3500}, 
           {"Nombre": "BAGUETTES", "$":2400}, 
           {"Nombre": "PAN PANECILLOS", "$":1000}, 
           {"Nombre": "PAN DE AJO", "$":4000}, 
           {"Nombre": "PAN DE OLIVA", "$":4500},
           {"Nombre": "PAN DE MAIZ", "$":5500}, 
           {"Nombre": "PAN ARABE", "$":5000}, 
           {"Nombre": "PAN ESPELTA", "$":5700}, 
        ]),
        "Promociones":list([
           {"Codigo": 4, "Informacion": "Compre 4", "$":8000}, 
           {"Codigo": 8, "Informacion": "Compre 3", "$":14000},
        ]),
    },
    "BOLLERIA":{
        "Producto":list([
           {"Nombre": "DONAS", "$":2500},
           {"Nombre": "CROAISSANTS", "$":2800},
           {"Nombre": "NAPOLITANAS", "$":3300},
           {"Nombre": "CARACOLA", "$":4500},
           {"Nombre": "CRESTA", "$":4000},
           {"Nombre": "TARTEL", "$":5000},
           {"Nombre": "MARAÑUELA", "$":4800},
           {"Nombre": "MUJI", "$":3700},
           {"Nombre": "TRENZA", "$":3100},
           {"Nombre": "CONSAIMADA", "$":4200},
        ]),
        "Promociones":list([
           {"Codigo": 1, "Informacion": "Compre 3", "$":6500},
           {"Codigo": 4, "Informacion": "Compre 2", "$":8000}, 
        ]),
    },
    "TARTAS":{
        "Producto":list([
           {"Nombre": "TARTA MOUSSE DE CHOCOLATE", "$":14000},
           {"Nombre": "TARTA DE FRESA", "$":12000},
           {"Nombre": "CHEESECAKE DE NUTELLA", "$":9000},
           {"Nombre": "TORTA DE HOJALDRE CON FRESA", "$":7500},
           {"Nombre": "BANANA CREAM PIE", "$":8300},
           {"Nombre": "CHEESECAKE DE JENGIBRE", "$":9000},
           {"Nombre": "TARTA DE TRES CHOCOLATES", "$":13000},
           {"Nombre": "TARTA FINA DE MANZANA", "$":15000},
           {"Nombre": "TARTA ARABE", "$":10000},
           {"Nombre": "TARTA DE PERAS", "$":12000},
          ]),
          "Promociones":list([
           {"Codigo": 7, "Informacion": "Compre 2", "$":20000},
           {"Codigo": 9, "Informacion": "Compre 2", "$":15000}, 
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
    print(f"{i}. {val}")
op_pr=int(input())
datosc=inicio.get(listac[opcion])
promociones=datosc["Promociones"]
promo=list()
for val in promociones:
    if (val.get("Codigo") == opcion):
        promo.append(val)
        
if (len(promociones)== 0):
    print (f"No hay promociones disponibles para {datosc['Producto'][op_pr]}")
else:
    print(f"Promociones del producto{datosc['Producto'][op_pr]}")
    print(promociones)
