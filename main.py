import tkinter as tk
import pyautogui
import time
import threading
import math

def click_accept_button(root):
    try:
        button_location = None

        print("Looking for button...")
        while button_location is None:
            try:
                # Busca imagines similares con una tolerancia del 0.7
                button_location = pyautogui.locateOnScreen('accept.png', confidence=0.7)
            except pyautogui.ImageNotFoundException:
                print("Button not found. Retrying...")
                time.sleep(1)

        print("Button found!")
        accept_button_center = pyautogui.center(button_location)
        pyautogui.click(accept_button_center)

        print("Match accepted! Exiting...")
        time.sleep(5)
        root.destroy() # This will close the Tkinter window
        exit() # This will close the cmd

    except Exception as e:
        print(f"An error occurred: {e}")

def start_app(root):
    # Crea un nuevo hilo para ejecutar la función click_accept_button function
    t = threading.Thread(target=click_accept_button, args=(root,))
    t.setDaemon(True)  # Establecer el hilo como un hilo demonio
    t.start()

    # Añadir un lienzo (canvas) para la animación del círculo giratorio
    waiting_canvas = tk.Canvas(root, width=120, height=150)
    waiting_canvas.pack()

    # Crear una animación de círculo giratorio
    def animate_waiting(angle):
        waiting_canvas.delete("all")
        x, y = 60, 60
        radius = 25
        arc_start = math.degrees(angle)
        arc_extent = 50  # Adjust the extent for faster/slower rotation
        waiting_canvas.create_arc(x - radius, y - radius, x + radius, y + radius,
                                  start=arc_start, extent=arc_extent, outline="blue", width=2, style=tk.ARC)
        root.after(60, animate_waiting, angle + 0.2)

    animate_waiting(0)

# Crear una ventana similar a la de un móvil
root = tk.Tk()
root.title("Mobile App Simulator")
root.geometry("360x640")  # Set dimensions to mimic a phone screen

# Crear un botón para iniciar la aplicación
start_button = tk.Button(root, text="Start App", command=lambda: start_app(root), bg="#4CAF50", fg="white", font=("Helvetica", 16))
start_button.pack(pady=20)

# Añadir una imagen
app_image = tk.PhotoImage(file="app_icon.png")
image_label = tk.Label(root, image=app_image)
image_label.pack()

root.mainloop()





