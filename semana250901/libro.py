#viene de ejercicio 2
from ejercicio2 import Libro

don_quijote = Libro(
    autor="Miguel de Cervantes",
    titulo="Don Quijote de la Mancha",
    genero="Novela",
    pag=863
)
print("Primer Obejeto Creado")
print("Mostrar objeto 1 con metodo get")
print("Título:", don_quijote.get_titulo())
print("Autor:", don_quijote.get_autor())
print("Género:", don_quijote.get_genero())
print("Paginas:", don_quijote.get_pag())
print("--- + ---")
print("Metodo Set - Esta version al tener graficos tiene mas paginas")
don_quijote.set_pag(1000)
print("Mostrar objeto 1 con metodo get")
print("Título:", don_quijote.get_titulo())
print("Autor:", don_quijote.get_autor())
print("Género:", don_quijote.get_genero())
print("Paginas:", don_quijote.get_pag())
print("--- + ---")
print("Equals - Primero creamos un segundo libro")
cien_anios = Libro(
    autor="Gabriel Garcia Marquez",
    titulo="Cien Años de Soledad",
    genero="Novela",
    pag=1039
)
print("Título:", cien_anios.get_titulo())
print("Autor:", cien_anios.get_autor())
print("Género:", cien_anios.get_genero())
print("Paginas:", cien_anios.get_pag())
igual_libro = don_quijote.equals(cien_anios)
if igual_libro:
    print(f"{don_quijote.get_titulo()} y {cien_anios.get_titulo()}, son iguales")
else:
    print(f"{don_quijote.get_titulo()} y {cien_anios.get_titulo()}, son distintos")

print("----- :) ------")
print("Metodo Copy. Hacemos una copia del libro del Quijote")

don_quijote_copia = don_quijote.copy()
print(" Autor: ", don_quijote_copia.get_autor())
print(" Título:", don_quijote_copia.get_titulo())
print(" Género:", don_quijote_copia.get_genero())
print(" Páginas:", don_quijote_copia.get_pag())

print("--- x:) ---")
print("Metodo Clonar. Hacemos un clone")
cien_anios_clon = cien_anios.clone()
print(" Autor: ", cien_anios_clon.autor)
print(" Título:", cien_anios_clon.get_titulo())

print(" Género:", cien_anios_clon.get_genero())
print(" Páginas:", cien_anios_clon.get_pag())
