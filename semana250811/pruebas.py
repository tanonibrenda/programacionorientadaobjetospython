from clasePersona import *

yo = Persona(30,"Carlos")
otraPersona = Persona(34,"Sofia")
# quiero consultar mi saldo, ¿como lo hago?
print(f'Mi saldo es: {yo.getSaldo()}')
print(yo.getNombre()) # forma correcta
"""print(yo._nombre)     # forma incorrecta
print(yo.__dict__)    # forma incorrecta
yo.apellido = "Caseres"# forma incorrecta
print(yo.__dict__)   # forma incorrecta"""
yo.setNombre("Pepe")
print(yo.getNombre()) # forma correcta
print("prueba de edad...")
print(yo.getEdad())
yo.cumplirAnios()
print(yo.getEdad())
yo.ingresarDinero(1000)
print(f'Mi saldo es: {otraPersona.getSaldo()}')
operacion = yo.retirarDinero(5000)
if operacion:
    print(f"Operacion exitosa..su saldo actual es de {yo.getSaldo()}")
else:
    print(f"Saldo insuficiente..su saldo actual es de {yo.getSaldo()}")

