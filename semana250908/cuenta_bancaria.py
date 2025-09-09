from tp3 import CuentaBancaria

cliente0001 = CuentaBancaria(
    numeroCuenta="0001",
    titular="yo",
    clave="1234",
    saldo=10,
    autentificado=False
)

print("Se ha creado una nueva cuenta bancaria")
print("Bienvenido", cliente0001.titular)
print("Ahora cambiemos el nombre del titular")
ingreso = input("Ingrese el nombre titular actual: ")
print("Ingresaste:", ingreso)
cliente0001.modificarTitular()