# Sistema de Gestión de Biblioteca

Este proyecto implementa un sencillo sistema de gestión de inventario para una biblioteca utilizando Python y Tkinter para la interfaz gráfica. Permite registrar libros, buscarlos, y marcar su estado de disponibilidad (prestado/devuelto). Los datos se guardan persistentemente en un archivo JSON.

---
Funcionamiento del Programa


Interfaz Principal

Al iniciar la aplicación, verás la ventana principal con los botones de operación y la lista de libros cargados.
![ddf](https://github.com/user-attachments/assets/6d4a002a-3ed8-47d2-bd12-5f1e68b330a6)



Registrar un Libro

Haz clic en "Registrar Libro" para añadir un nuevo ejemplar al inventario. Se te pedirá el título, autor y categoría.

![fffg](https://github.com/user-attachments/assets/9fba1b35-1d5b-4633-8d50-b73bc0651a7d)


### Buscar un Libro

Usa la opción "Buscar Libro" para encontrar ejemplares por título o autor. Los resultados se mostrarán en la lista principal.

![ddfdf](https://github.com/user-attachments/assets/6c4971cb-69ad-4212-8ff8-c4419c1fbd4f)


Marcar Prestado/Devuelto

Con la opción "Marcar Prestado/Devuelto", puedes cambiar el estado de disponibilidad de un libro.

![dddf](https://github.com/user-attachments/assets/73e1ea98-2e2a-4026-b5f2-32dba6e12102)

![ftyt](https://github.com/user-attachments/assets/db73c133-b46b-4ed2-bc20-205f287f6945)
Estructuras de Datos y Funciones Implementadas

Estructuras de Datos

libros` (Lista de Diccionarios):** La colección principal de datos. Cada libro se representa como un diccionario con las siguientes claves:valor
  titulo: El título del libro.
  autor: El autor del libro.
  categoria: La categoría a la que pertenece el libro (igeeria, "Ciencia", "Literatura").
  disponible": True si el libro está disponible, False si está prestado.
  ARCHIVO_DATOS: Constante que define el nombre del archivo JSON para la persistencia de datos.
  CATEGORIAS` (list):Lista de cadenas que define las categorías permitidas para los libros.

Funciones y Métodos Clave

cargar_datos():Lee y carga los datos de los libros desde el archivo JSON (`data.json`). Si el archivo no existe, devuelve una lista vacía.
guardar_datos(libros): Escribe la lista actual de libros en el archivo JSON, asegurando el formato y la codificación correctos.
agregar_libro(libros, titulo, autor, categoria)`:Añade un nuevo diccionario de libro a la lista, inicializándolo como disponible.
buscar_libros(libros, termino):Filtra la lista de libros y devuelve aquellos cuyo título o autor coincida (insensible a mayúsculas/minúsculas) con el término de búsqueda.
cambiar_estado(libros, titulo):Busca un libro por su título y alterna su estado `disponible` (de `True` a `False` o viceversa). Maneja la búsqueda de título sin distinción de mayúsculas/minúsculas.


---

Justificación Técnica de Decisiones de Diseño

elección del Método de Persistencia (JSON)

Simplicidad:Para una aplicación de este tamaño y complejidad, JSON es un formato ideal. Es fácil de leer y escribir tanto para humanos como para máquinas.
* **Estructura de Datos Nativa:JSON mapea directamente a las estructuras de datos de Python (listas y diccionarios), lo que simplifica la serialización y deserialización de objetos. No requiere una base de datos compleja para un inventario sencillo.
  Portabilidad:Los archivos JSON son de texto plano y ampliamente compatibles, lo que facilita el intercambio de datos entre diferentes plataformas o lenguajes si el proyecto escalara.

Elección de la Librería GUI (Tkinter)
Tkinter viene incluido con Python, lo que significa que no se requiere ninguna instalación adicional para ejecutar la aplicación. Esto simplifica la distribución y el inicio rápido del parcial.


---

Análisis de Dificultades y Posibles Mejoras

Dificultades Encontradas

Gestión del Estado de la GUI: Asegurar que la lista de libros mostrada se actualice consistentemente después de cada operación (registrar, buscar, marcar) requirió una función centralizada (`actualizar_lista`) y asegurarse de que siempre se llamara en el momento adecuado.
Validación de Entradas:Implementar una validación básica (no campos vacíos, categoría válida) requirió lógica condicional y mensajes de error específicos, lo que añade líneas de código para cada entrada.
defiir las fuciones corrrectamenete

Posibles Mejoras Futuras

Funcionalidad de Eliminar/Editar Libros:** Añadir opciones para eliminar un libro o editar sus detalles existentes (título, autor, categoría).
Visualización Mejorada:
  usar firebase en el trabajo ya que es mejor para la persistencia de datos
Validación de Entradas Más Robusta:
Añadir una verificación para evitar duplicados exactos (mismo título y autor) al registrar un nuevo libro.
Considerar la validación de formato (ej. si se introdujera un número donde se espera texto).
Reportes Básicos: Funcionalidad para generar una lista de libros disponibles o prestados.
Interfaz de Búsqueda Mejorada: Un campo de búsqueda persistente que no requiera abrir un `simpledialog` cada vez.
Manejo de Errores Más Específico:*Capturar y manejar excepciones específicas (ej., errores de escritura/lectura de archivos) para mostrar mensajes más útiles al usuario.
Pruebas Unitarias:Implementar pruebas unitarias para las funciones lógicas (agregar, buscar, cambiar estado) para asegurar su correcto funcionamiento.

