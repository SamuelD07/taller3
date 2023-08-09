class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def mostrar_detalles(self):
        propietarios_str = ", ".join(self.propietarios)
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {propietarios_str}")
        print(f"Balance: {self.balance}")

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se depositaron {monto} en la cuenta. Nuevo balance: {self.balance}")
        else:
            print("El monto de depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print(f"Se retiraron {monto} de la cuenta. Nuevo balance: {self.balance}")
        else:
            print("Monto de retiro inválido o insuficiente fondos.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2%: {cuota}. Nuevo balance: {self.balance}")


#Así se podría usar#
cuenta = CuentaBancaria("123456789", ["John Doe", "Jane Smith"], 5000)

cuenta.mostrar_detalles()
cuenta.depositar(1000)
cuenta.mostrar_detalles()
