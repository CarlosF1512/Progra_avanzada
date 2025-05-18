# Ejercicio 2 - Práctica 2
import datetime

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Información personal; Nombre: {self.nombre}, Edad: {self.edad}"
    
class Huesped(Persona):
    def __init__(self, nombre, edad, habitacion, RFC, num_cuenta, dt_ingreso, b_hospedado, servicio):
        super().__init__(nombre, edad)
        self.habitacion = int(habitacion)
        self.RFC = str(RFC)
        self.num_cuenta = float(num_cuenta)
        self.dt_ingreso = dt_ingreso
        self.b_hospedado = bool(b_hospedado)
        self.servicio = servicio  

    def __str__(self):
        return (f"Información del huésped:\n"
                f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad}\n"
                f"Habitación: {self.habitacion}\n"
                f"RFC: {self.RFC}\n"
                f"Número de cuenta: {self.num_cuenta}\n"
                f"Fecha de ingreso: {self.dt_ingreso}\n"
                f"¿Sigue hospedado?: {self.b_hospedado}\n"
                f"Servicios: {self.servicio}")

    def costo_servicio(self):
        return sum(self.servicio.values())

    def costo_servicio_individual(self, nombre_servicio):
        return self.servicio.get(nombre_servicio, 0)

    def costo_total(self):
        total_t = 0
        if self.b_hospedado:
            dias = (datetime.date.today() - self.dt_ingreso).days
            total_t = dias * 1000
            print(f"Total de días hospedado: {dias}")
        return total_t + self.costo_servicio()

# Ejemplo de uso
huesped1 = Huesped("Juan", 30, 101, "RFC123", 123456, datetime.date(2025, 5, 10), True, {"Gimnasio": 200, "Spa": 300})
print(huesped1, "\n")
print("Costo total de los servicios: $", huesped1.costo_servicio())
print("Costo total de la habitación: $", huesped1.costo_total(),'\n')

# huesped1.servicio = {"Gimnasio": 200, "Spa": 300}
# print("Costo total de los servicios: ", huesped1.costo_servicio(),'\n')
# print("Costo total de la habitación: ", huesped1.costo_total(),'\n')
