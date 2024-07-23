# Análisis Básico de Redes con Tkinter
## Introducción
Este proyecto es una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter. 
Su propósito es ofrecer una interfaz gráfica simple para realizar análisis básicos de redes como comando de ping 
Es una herramienta útil para la práctica y el aprendizaje en el campo del hacking ético y el análisis de redes.

## Desarrollo

La aplicación está construida utilizando Python y Tkinter para la interfaz gráfica de usuario. 
El proyecto emplea la biblioteca subprocess para ejecutar comandos de red y capturar sus resultados y socket para obtener del domino su direccion ip. 
La interfaz permite al usuario ingresar direcciones IP o dominios y ver los resultados directamente en la aplicación.

### Estructura del Proyecto

**Pantalla Principal**

Navega entre diferentes funcionalidades: Ping, Traceroute, Escaneo de Puertos.

#### Funcionalidad PING

Permite al usuario ingresar una dirección IP o dominio y ejecutar el comando ping.
Muestra los resultados del ping en un área de texto.

## Ping

### Entrada:

Comando Ejecutado: ping <dirección IP o dominio>
Salida: Resultados del comando ping, incluyendo tiempos de respuesta y posibles pérdidas de paquetes.
Traceroute

Salida: Resultados del escaneo de los dispositivos activos

## Cómo Usar
Clona el Repositorio

```bash 
git clone https://github.com/3eze3/Interfaz-Gestion-Redes.git
cd analisis-basico-redes
```
Instala Dependencias

Asegúrate de tener Python instalado. Luego, instala las dependencias necesarias:

```bash
pip install tkinter
```

Ejecuta la Aplicación
**Ejecuta el script principal de la aplicación:**

```bash
python main.py
```

- Para Ping: Ingresa una dirección IP o dominio en el campo de texto y haz clic en "OK".

# Ver Resultados

**Los resultados se mostrarán en el área de texto correspondiente en la interfaz de la aplicación.**
