class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo, clave, autentificado):
        self.numeroCuenta = numeroCuenta
        self.titular      = titular
        self.clave        = clave
        self.saldo        = saldo               # al momento de crear la cuenta esta en 0
        self.autentificado= False              # hasta no empezar a operar, no se autentific
    #metodos de consulta
    def getNumeroCuenta(self):
        return  self.numeroCuenta
    def getTitular(self):
        return  self.titular
    def getClave(self):
        return  self.clave
    def getSaldo(self):
        return  self.saldo
    def getAutentificado(self):
        return  self.autentificado
    
    #print("Debug: Cuenta creada")

    #metodos de modificacio de titular y clave (con restricciones)

    def modificarTitular(self):
        ingreso = input("Ingrese su nombre actual como titular: ")
        if ingreso == self.titular:
            nuevo_nombre = input("Ingrese el nuevo nombre de titular: ")
            self.titular = nuevo_nombre
            print("El nuevo titular es:", self.titular)
        else:
            print("Titular ingresado incorrecto.")

