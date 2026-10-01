<div align="justify">
  
# RESTURANTE_SEMANA_16

# Universidad Estatal Amazonica (UEA)

# Sistema de Gestión de Restaurante - Manejo de eventos aplicado a la gestión de usuarios

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

---

## Descripción General del Sistema

Este proyecto consiste en una aplicación de escritorio desarrollada en **Python** que utiliza **Tkinter** para crear la interfaz gráfica y archivos **JSON** para conservar la información del sistema, permitiendo administrar diferentes operaciones de un restaurante de manera organizada, entre ellas el registro y control de productos, la consulta de usuarios y el procesamiento de ventas, además el sistema incorpora un control de acceso mediante roles para diferenciar las funciones disponibles para administradores y clientes, mientras que el stock se actualiza automáticamente cada vez que se realiza una venta.

---

## Estructura del Proyecto

El sistema mantiene una organización modular que permite separar las responsabilidades de cada componente, donde **assets/** contiene los recursos gráficos utilizados en la interfaz, **datos/** almacena los archivos **JSON** con la información del sistema, **modelos/** contiene las clases principales, **servicios/** administra la lógica de negocio y la persistencia, mientras que **ui/** contiene las vistas gráficas desarrolladas con **Tkinter**, finalmente **main.py** funciona como punto de entrada y coordina la ejecución y navegación de la aplicación.

```text
restaurante_app/
│
├── assets/
│   ├── app_icon.ico
│   ├── logo.png
│   ├── icon_producto.png
│   ├── icon_usuario.png
│   └── icon_venta.png
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
```

---
## Componentes Técnicos Aplicados
---

## Responsabilidad de las Clases y Módulos

Las clases **Producto**, **Usuario** y **Venta** representan las principales entidades del sistema y contienen los datos necesarios para administrar **productos**, **usuarios** y **transacciones**, mientras que **archivo_servicio.py** se encarga de leer y guardar la información en los archivos **JSON**, por otra parte, **restaurante_servicio.py** concentra las reglas de negocio, las validaciones de acceso, el control del stock y el procesamiento de las ventas, finalmente **login_view.py** administra el inicio de sesión y **main_view.py** presenta las diferentes funciones disponibles según el rol del usuario.

---

## Funcionalidades Principales

El sistema permite realizar diferentes operaciones desde la interfaz gráfica, comenzando con el inicio de sesión, donde el usuario ingresa sus datos y el sistema determina las opciones disponibles según su rol, posteriormente los usuarios regulares pueden seleccionar productos y registrar compras, mientras que los administradores cuentan con funciones adicionales para crear, consultar, actualizar y eliminar productos, además pueden consultar la información de los usuarios registrados, de esta manera cada usuario accede únicamente a las funciones correspondientes a su nivel de autorización.

---

## Registro de Ventas y Control de Stock

El registro de ventas permite seleccionar el cliente y el producto mediante controles de la interfaz, posteriormente el sistema verifica que el producto exista y que la cantidad solicitada se encuentre disponible en el inventario, si la operación es válida se registra la venta y se disminuye automáticamente el stock correspondiente, además se almacena la fecha y hora de la transacción para mantener un historial organizado, finalmente la información actualizada se guarda en los archivos **JSON** para conservar los cambios realizados.

## Persistencia de Datos

La información del sistema se conserva mediante tres archivos **JSON** ubicados en la carpeta **datos/**, donde **productos.json** almacena los productos junto con sus precios y cantidades disponibles, **usuarios.json** mantiene los datos de clientes y administradores, mientras que **ventas.json** conserva el historial de las transacciones realizadas, de esta manera los datos pueden recuperarse cuando la aplicación vuelve a ejecutarse y se evita perder la información registrada durante una sesión anterior.

---

## Reflexión Final

El desarrollo de la Semana 16 permite integrar los conocimientos adquiridos durante las diferentes etapas del proyecto, combinando **Programación Orientada a Objetos (POO)**, interfaces gráficas, persistencia de datos, control de acceso y gestión de ventas dentro de una misma aplicación, además la separación entre modelos, servicios e interfaz facilita la comprensión y mantenimiento del código, mientras que el uso de archivos **JSON** permite conservar la información de manera sencilla, de esta forma **restaurante_app** cuenta con una estructura organizada que puede continuar ampliándose con nuevas funcionalidades en futuras versiones.

<div>
