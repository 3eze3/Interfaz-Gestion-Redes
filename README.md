# Análisis Básico de Redes con Tkinter
## Introducción
Este proyecto es una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter. Su propósito es ofrecer una interfaz gráfica simple para realizar análisis básicos de redes, como comandos de ping, traceroute y escaneo de puertos. Es una herramienta útil para la práctica y el aprendizaje en el campo del hacking ético y el análisis de redes.

## Desarrollo
La aplicación está construida utilizando Python y Tkinter para la interfaz gráfica de usuario. El proyecto emplea la biblioteca subprocess para ejecutar comandos de red y capturar sus resultados. La interfaz permite al usuario ingresar direcciones IP o dominios y ver los resultados directamente en la aplicación.

### Estructura del Proyecto
**Pantalla Principal**

Navega entre diferentes funcionalidades: Ping, Traceroute, Escaneo de Puertos.
Funcionalidad Ping

Permite al usuario ingresar una dirección IP o dominio y ejecutar el comando ping.
Muestra los resultados del ping en un área de texto.
Funcionalidad Traceroute

Permite al usuario ingresar una dirección IP o dominio y ejecutar el comando traceroute.
Muestra los resultados del traceroute en un área de texto.
Funcionalidad Escaneo de Puertos

Permite al usuario ingresar una dirección IP o dominio y un rango de puertos para escanear.
Ejecuta un escaneo de puertos utilizando nmap y muestra los resultados en un área de texto.
Características
Ping

### Entrada:

Comando Ejecutado: ping <dirección IP o dominio>
Salida: Resultados del comando ping, incluyendo tiempos de respuesta y posibles pérdidas de paquetes.
Traceroute

### Entrada:

Comando Ejecutado: traceroute <dirección IP o dominio>
Salida: Resultados del comando traceroute, mostrando la ruta que sigue el paquete hasta llegar al destino.
Escaneo de Puertos

### Entrada:

Campo de texto para ingresar la dirección IP o dominio.
Campo de texto para ingresar el rango de puertos (por ejemplo, 1-1024).
Comando Ejecutado: nmap -p <rango de puertos> <dirección IP o dominio>

Salida: Resultados del escaneo de puertos, mostrando puertos abiertos y su estado.

## Cómo Usar
Clona el Repositorio

```bash 
git clone https://github.com/tu_usuario/analisis-basico-redes.git
cd analisis-basico-redes
```
Instala Dependencias

Asegúrate de tener Python instalado. Luego, instala las dependencias necesarias:

```bash
pip install tkinter
```
# Nota: nmap puede necesitar ser instalado por separado
Ejecuta la Aplicación
Ejecuta el script principal de la aplicación:

```bash
Copy code
python app.py
```

- Para Ping: Ingresa una dirección IP o dominio en el campo de texto y haz clic en "Ejecutar".
- Para Traceroute: Ingresa una dirección IP o dominio en el campo de texto y haz clic en "Ejecutar".
- Para Escaneo de Puertos: Ingresa una dirección IP o dominio y el rango de puertos en los campos de texto, luego haz clic en "Ejecutar".

# Ver Resultados

**Los resultados se mostrarán en el área de texto correspondiente en la interfaz de la aplicación.**
