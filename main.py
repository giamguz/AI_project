import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Fitness App")
ventana.geometry("1280x700")
ventana.configure(bg="#022e61")

# Crear frames para organizar los elementos
frame_central = tk.Frame(ventana, bg="#022e61", width=600, height=600)
frame_derecho = tk.Frame(ventana, bg="#022e61", width=500, height=600)

#frame_izquierdo.pack(side="left", fill="y")
frame_central.pack(side="left", expand=True, fill="both")
frame_derecho.pack(side="right", expand=True, fill="y")


# Configurar frame central (video con OpenCV)
video_label = tk.Label(frame_central, bg="black")
video_label.pack(pady=10)

# Inicializar OpenCV
cap = cv2.VideoCapture(0)  # Cámara predeterminada

def actualizar_video():
    ret, frame = cap.read()  # Leer el frame de la cámara
    if ret:
        # Convertir el frame de BGR a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convertir el frame en una imagen compatible con Tkinter
        frame_image = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
        # Actualizar la etiqueta con la nueva imagen
        video_label.config(image=frame_image)
        video_label.image = frame_image
    # Llamar a esta función nuevamente después de un corto retraso
    frame_central.after(10, actualizar_video)

# Configurar frame derecho
ejercicio = "Curl de biceps"
cant_reps = 0
ejercicio_label = tk.Label(frame_central, text=ejercicio,font=("Lato", 35, "bold"), bg="#022e61", fg="white")
ejercicio_label.pack(pady=30)
repeticiones_label = tk.Label(frame_derecho, text="Repeticiones", font=("Arial", 18, "bold"), bg="#022e61", fg="white")
repeticiones_label.pack(pady=20)
repeticiones_numero = tk.Label(frame_derecho, text=cant_reps, font=("Arial", 24, "bold"), bg="#022e61", fg="white")
repeticiones_numero.pack(pady=10)



# Botón de feedback
feedback_button = tk.Button(
    frame_derecho,
    text="View Feedback",
    font=("Arial", 12),
    bg="gray",
    fg="white",
    bd=0,
)
feedback_button.pack(pady=20, side="bottom")

# Iniciar actualización del video
actualizar_video()

# Iniciar el bucle de la ventana
ventana.mainloop()
