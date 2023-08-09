class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def __str__(self):
        propietarios_str = ", ".join(self.propietarios)
        return f"Número de cuenta: {self.numero_cuenta}\nPropietarios: {propietarios_str}\nBalance: {self.balance}"

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Se depositaron {monto} en la cuenta. Nuevo balance: {self.balance}")
        else:
            print("El monto de depósito debe ser mayor que cero.")



cuenta = CuentaBancaria("123456789", ["John Doe", "Jane Smith"], 5000)

print(cuenta)
cuenta.depositar(1000)
print(cuenta)
cuenta.depositar(-200)
