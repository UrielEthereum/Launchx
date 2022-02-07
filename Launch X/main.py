# program.py
from datetime import date


sum = 1 + 2
print(sum)

print('Hola desde la consola')
# Impresión en pantalla print('Hola desde la consola')

sum = 1 + 2 # 3
product = sum * 2
print(product)

# Tu turno, prueba el fragmento de código anterior

planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

print(planetas_en_el_sistema_solar)

print(distancia_a_alfa_centauri)

print(puede_despegar,transbordador_que_aterrizo_en_la_luna)

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)

from datetime import date
print(date.today())

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())
print(f"Today's date is:{date.today()}")