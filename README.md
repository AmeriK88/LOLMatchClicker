# LOLMatchclicker
Auto clicker para partidas de league of legends.


### Mobile App Simulator
Este es un simulador básico de aplicación móvil creado con Python y la biblioteca Tkinter. El objetivo de esta aplicación es simular la interacción de un usuario con league of legends, buscando un botón de aceptar en la ventana y haciendo clic en él. Ya no rechazarás ninguna partida!

## 1. Requisitos:
   
Python 3.x
Bibliotecas: 
      -tkinter
      -pyautogui


## 2. Instalación:

Clona este repositorio en tu máquina local:
git clone https://github.com/tu_usuario/mobile-app-simulator.git

Instala las dependencias con pip:
pip install -r requirements.txt

## 3. Uso:
Ejecuta el script app.py:
              -python app.py

La ventana de la aplicación se abrirá, simulando la pantalla de un teléfono móvil.
Haz clic en el botón "Start App" para iniciar la aplicación.
La aplicación buscará un botón de aceptar (representado por una imagen llamada accept.png en el directorio) en la pantalla y hará clic en él automáticamente si se encuentra.

## Funcionalidades:
Simula una aplicación móvil básica.
Busca y hace clic en un botón de aceptar automáticamente.
Muestra una animación de un círculo giratorio mientras busca el botón.


## Licencia
Este proyecto está bajo la Licencia MIT.

PD: Puedes generar un ejecutable con pyinstaller para no tener que abrir tu editor de código cada vez. Recuerda adjuntar la imagen al ejecutar el comando pyinstaller (--add-data)
