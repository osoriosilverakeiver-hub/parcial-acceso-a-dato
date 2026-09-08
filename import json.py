import json
import os


class Transaccion:

    def __init__(self, id, titular, valor, hora, pais, dispositivo_conocido):

        # Validaciones
        if not titular.strip():
            raise ValueError("El titular no puede estar vacio.")

        if valor <= 0:
            raise ValueError("El valor debe ser mayor que cero.")

        if hora < 0 or hora > 23:
            raise ValueError("La hora debe estar entre 0 y 23.")

        if not pais.strip():
            raise ValueError("El país no puede estar vacio.")

        if not isinstance(dispositivo_conocido, bool):
            raise ValueError(
                "dispositivo_conocido debe ser True o False."
            )

        self.id = id
        self.titular = titular
        self.valor = valor
        self.hora = hora
        self.pais = pais
        self.dispositivo_conocido = dispositivo_conocido

        self.puntaje_riesgo = self.calcular_riesgo()
        self.clasificacion = self.clasificar()

    def calcular_riesgo(self):
        puntaje = 0

        if self.valor >= 2000000:
            puntaje += 30

        if 0 <= self.hora <= 5:
            puntaje += 20

        if self.pais.strip().lower() != "colombia":
            puntaje += 25

        if not self.dispositivo_conocido:
            puntaje += 30

        return puntaje

    def clasificar(self):

        if self.puntaje_riesgo <= 29:
            return "NORMAL"

        elif self.puntaje_riesgo <= 59:
            return "SOSPECHOSA"

        else:
            return "ALTO RIESGO"

    def to_dict(self):

        return {
            "id": self.id,
            "titular": self.titular,
            "valor": self.valor,
            "hora": self.hora,
            "pais": self.pais,
            "dispositivo_conocido": self.dispositivo_conocido,
            "puntaje_riesgo": self.puntaje_riesgo,
            "clasificacion": self.clasificacion
        }

    @classmethod
    def from_dict(cls, datos):

        return cls(
            datos["id"],
            datos["titular"],
            datos["valor"],
            datos["hora"],
            datos["pais"],
            datos["dispositivo_conocido"]
        )



def cargar_transacciones():

    if not os.path.exists("transacciones.json"):
        return []

    try:
        with open("transacciones.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Transaccion.from_dict(dato) for dato in datos]

    except (json.JSONDecodeError, KeyError, TypeError):
        print("Error al leer el archivo JSON.")
        return []



def guardar_transacciones(transacciones):

    datos = []

    for transaccion in transacciones:
        datos.append(transaccion.to_dict())

    with open("transacciones.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)



def mostrar_transaccion(transaccion):

    print("----------------------------------------")
    print("ID:", transaccion.id)
    print("Titular:", transaccion.titular)
    print("Valor:", transaccion.valor)
    print("Hora:", transaccion.hora)
    print("País:", transaccion.pais)
    print("Dispositivo conocido:", transaccion.dispositivo_conocido)
    print("Puntaje de riesgo:", transaccion.puntaje_riesgo)
    print("Clasificación:", transaccion.clasificacion)



def registrar_transaccion(transacciones):

    try:
        print("\n--- REGISTRAR TRANSACCIÓN ---")

        id = int(input("ID: "))
        titular = input("Titular: ")

        valor = float(input("Valor: "))

        hora = int(input("Hora (0-23): "))

        pais = input("Pais: ")

        dispositivo = input(
            "¿El dispositivo es conocido? (si/no): "
        ).strip().lower()

        if dispositivo == "si":
            dispositivo_conocido = True

        elif dispositivo == "no":
            dispositivo_conocido = False

        else:
            print("Debe escribir 'si' o 'no'.")
            return

        nueva_transaccion = Transaccion(
            id,
            titular,
            valor,
            hora,
            pais,
            dispositivo_conocido
        )

        transacciones.append(nueva_transaccion)

        print("\nTransacción registrada correctamente.")
        print("Puntaje de riesgo:", nueva_transaccion.puntaje_riesgo)
        print("Clasificación:", nueva_transaccion.clasificacion)

    except ValueError as error:
        print("Error:", error)



def listar_transacciones(transacciones):

    print("\n--- LISTA DE TRANSACCIONES ---")

    if len(transacciones) == 0:
        print("No hay transacciones registradas.")
        return

    for transaccion in transacciones:
        mostrar_transaccion(transaccion)


transacciones = cargar_transacciones()

while True:

    print("\n================================")
    print("       SISTEMA ANTIFRAUDE")
    print("================================")
    print("1. Registrar transaccion")
    print("2. Listar transacciones")
    print("3. Salir")
    print("================================")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        registrar_transaccion(transacciones)
        guardar_transacciones(transacciones)

    elif opcion == "2":

        listar_transacciones(transacciones)

    elif opcion == "3":

        guardar_transacciones(transacciones)

        print("\nTransacciones guardadas correctamente.")
        print("Programa finalizado.")
        break

    else:

        print("\nOpcion inválida. Intente nuevamente.")