class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo, clave, autentificado):
        self._numeroCuenta = numeroCuenta
        self._titular      = titular
        self._clave        = clave
        self._saldo        = saldo               # al momento de crear la cuenta esta en 0
        self._autentificado= False              # hasta no empezar a operar, no se autentific
        self._historial    = []
    #metodos de consulta
    def getNumeroCuenta(self):
        return  self._numeroCuenta
    def getTitular(self):
        return  self._titular
    def getClave(self):
        return  self._clave
    def getSaldo(self):
        return  self._saldo
    def getAutentificado(self):
        return  self._autentificado
    def getHistorial(self):
        return self._historial
    
    #print("Debug: Cuenta creada")

    #metodos de modificacio de titular y clave (con restricciones)

    #para esto vamos a autentificar al cliente
    def autentificar(self):
        validarNombre = input("Ingrese el nombre del titular: ")
        if validarNombre == self._titular:
            validarClave = input("Ingrese su clave: ")
            if validarClave == self._clave:
                self._autentificado = True
                print("Usuario validado correctamente.")
            else:
                print("Clave incorrecta.")
        else:
            print("Titular ingresado incorrecto.")


    def modificarTitular(self):
        print(" Para modificar sus datos, volvamos a autenfiticar su identidad")
        self.autentificar()

        if self._autentificado:
            nuevo_nombre = input("Ingrese el nuevo nombre de titular: ")
            if nuevo_nombre.isalpha():
                self._titular = nuevo_nombre
                print(" El nuevo titular es:", self._titular)
            else:
                print("El nombre solo debe contener letras")
        else:
            print(" No se pudo modificar el titular. Autenticación fallida.")

