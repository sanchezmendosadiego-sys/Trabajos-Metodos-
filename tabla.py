# Pedir los valores al usuario en la terminal
precio_venta = float(input("Ingresa el PRECIO DE VENTA POR UNIDAD: "))
costo_fijo = float(input("Ingresa el COSTO FIJO: "))
costo_variable = float(input("Ingresa el COSTO VARIABLE: "))
unidades = float(input("Ingresa el NUMERO DE UNIDADES: "))

# Calcular la Ganancia
ganancia = (precio_venta * unidades) - (costo_fijo + costo_variable * unidades)

# Calcular el Punto de Equilibrio (con validación para evitar división por cero)
if (precio_venta - costo_variable) != 0:
    punto_equilibrio = costo_fijo / (precio_venta - costo_variable)
else:
    punto_equilibrio = "Indefinido"

# Formatear e imprimir la tabla
print("\n" + f"{'':<28} | {'VALORES':<10} | {'GANANCIA':<10} | {'PUNTO DE EQUILIBRIO'}")
print("-" * 75)
print(f"{'PRECIO DE VENTA POR UNIDAD':<28} | {precio_venta:<10} | {ganancia:<10} | {punto_equilibrio}")
print(f"{'COSTO FIJO':<28} | {costo_fijo:<10} | {'':<10} | {''}")
print(f"{'COSTO VARIABLE':<28} | {costo_variable:<10} | {'':<10} | {''}")
print(f"{'NUMERO DE UNIDADES':<28} | {unidades:<10} | {'':<10} | {''}\n")
