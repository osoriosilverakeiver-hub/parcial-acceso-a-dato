# Parcial — Detector de Transmisiones Sospechosas

Nombre:  Keiver Osorio Silvera 
Código:  
Grupo: 4E 

## 1. ¿Qué debe hacer el programa?
---
Este proograma debera tener un registro de las transacciones, Guardarlas temporalmente en una lista mientras que el programa este encendido, Analizar el riesgo de cada operacion, Asignar una clasificacion segun el riesgo, Guardar los datos en un archivo JSON. Y por ultimo pero no menos importante leer ese JSON para recuperar las transacciones.
---

## 2. Clase `Transaccion`

La clase tendrá los siguientes atributos:

- `id`: identificador unico de la transaccion
- `titular`: Nombre de la persona que realiza la transaccion
- `valor`: valor de la operacion
- `hora`: hora en la que se realiza
- `pais`: pais desde donde realiza
- `dispositivo_conocido`: indicara si el dispositivo es conocido(true) o si no, (false)
- `clasificacion`: resultado de la clasificacion del riesgo


---

## 3. Métodos

### `analizar()`

Responsabilidad: Analizar el mensaje de la transaccion, buscar palabras sospechosas y asignar puntos de riesgo.

### `clasificar()`

Responsabilidad: Determinar la clasificacion de la transaccion segun el puntaje obtenido.

### `to_dict()`

Responsabilidad: Convertir el objeto transaccion en un diccionario para poder guardarlo en un archivo JSON.

### `from_dict()`

Responsabilidad: Crear una transaccion a partir de los datos almacenados en un diccionario.

---

## 4. Algoritmo de análisis

Complete el siguiente pseudocódigo:

```text
puntaje = 0

SI el valor es mayor o igual a 2.000.000
    sumar 30 puntos

SI la hora esta entre 0 y 5 
    sumar 20 puntos

SI el pais es diferente de colombia 
    sumar 25 puntos

SI el dispositivo No es conocido
    sumar 30 puntos


```

---

## 5. Persistencia

Explique brevemente qué ocurre al iniciar el programa:

```text
JSON
 ↓
Diccionarios
 ↓
Objetos de transaccion
```

Explique qué ocurre al guardar:

```text
Objetos
 ↓
Diccionarios
 ↓
JSON
```

---

## 6. Menú


### Opción 1 — Registrar transmisión

1. solicitar los datos de la transaccion.
2. Crear un objeto transaccion.
3. agragar el objeto a la lista y calcular automaticamente su riesgo.



### Opción 2 — Listar transmisiones

1. recorrer la lista de objetos. 
2.  mostrar ID, titular, puntaje de riesgo y clasificacion

### Opción 3 — Salir

Acción: guardar las transacciones en transacciones.json y finalizar el programa.

---

## Nota

Este archivo debe completarse durante los primeros 15 minutos del parcial, antes de comenzar la implementación.