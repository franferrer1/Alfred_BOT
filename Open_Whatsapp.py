from pywinauto import Desktop
from pywinauto.application import Application
import time
import os


def open_wpp():
    # Ruta de acceso de la aplicación de WhatsApp
    whatsapp_path = r"C:\Users\INGENIERIA\Desktop\WhatsApp - Acceso directo.lnk"

    # Abre la aplicación de WhatsApp
    os.startfile(whatsapp_path)
    print("Abriendo WhatsApp...")
    time.sleep(5) #Espera a que inicie la aplicación

def search_wpp():
    """
    Función para buscar la ventana de WhatsApp exacta.
    """
    # Obtener todas las ventanas abiertas
    windows = Desktop(backend="win32").windows()

    # Buscar la ventana de WhatsApp exacta
    whatsapp_window = None
    for win in windows:
        # Obtener el texto de la ventana
        title = win.window_text()

        # Verificar si 'WhatsApp' es exactamente la única palabra que aparece en el título
        if "WhatsApp" in title and len(title.split()) == 1:  # Si solo hay una palabra "WhatsApp"
            whatsapp_window = win
            print(f"Ventana de WhatsApp encontrada: {title}")
            break

    if whatsapp_window:
        app = Application(backend="win32").connect(handle=whatsapp_window.handle)
        wa_window = app.window(handle=whatsapp_window.handle)
        # Realiza las operaciones que necesitas con wa_window
    else:
        print("No se encontró la ventana de WhatsApp.")
    if wa_window:
        wa_window.set_focus()  # Llevar WhatsApp al frente
        time.sleep(5)  # Espera 5 segundos para iniciar
    else:
        print("No se pudo enfocar la ventana de WhatsApp.")
    return wa_window


