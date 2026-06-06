class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = 0
        self.set_temperatura(temperatura)

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Temperatura inválida")

    def status(self):
        if self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"


sensor = Sensor(25)
print(sensor.status())

sensor.set_temperatura(90)
print(sensor.status())

sensor.set_temperatura(130)
print(sensor.status())

sensor.set_temperatura(-10)
print(sensor.status())
