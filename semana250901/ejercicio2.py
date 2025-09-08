# Ejercicio 2 
# Realizar la implementación de la clase Libro, que contenga información de su 
# autor, título del libro, género y cantidad de páginas. Incluir todos los comandos 
# de consulta y modificación de atributos. Dibujar el diagrama correspondiente. 
# Implementar los métodos de equals, copy y clone. Mostrar ejemplos de uso de 
# cada uno para verificar el correcto funcionamiento.

class Libro:
    def __init__(self, autor, titulo, genero, pag):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.pag = pag

    def get_autor(self):
        return self.autor

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_genero(self):
        return self.genero
    def get_pag(self):
        return self.pag

    def set_pag(self, nueva_pag):
        if nueva_pag > 0:
            self.pag = nueva_pag

        else:
            print("El libro debe tener alguna pagina")
#Metodo Equals
    def equals(self, otro_libro):
        return (
                self.autor == otro_libro.autor and
                self.titulo == otro_libro.titulo and
                self.genero == otro_libro.genero and
                self.pag == otro_libro.pag
        )
#Metodo Copy
### corregir
    def copy(self):
        return Libro(
            autor=self.autor,
            titulo=self.titulo,
            genero=self.genero,
            pag=self.pag
        )
# Metodo Clone

    def clone(self):
        mi_clone = Libro(
            self.autor,
            self.titulo,
            self.genero,
            self.pag
        )
        return mi_clone