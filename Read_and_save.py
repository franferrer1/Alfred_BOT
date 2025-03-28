from pywinauto import Desktop
from pywinauto.application import Application


# Función para obtener los mensajes
def get_messages(wa_window):
    messages = []
    for item in wa_window.descendants():  # Recorrer todos los elementos de la ventana
        if item.window_text():  # Si el item tiene texto (mensaje)
            messages.append(item.window_text())  # Guardar el texto del mensaje
    return messages

def read_and_save_messages():
    windows = Desktop(backend="uia").windows()

    whatsapp_window = None
    for win in windows:
        if "WhatsApp" in win.window_text():
            whatsapp_window = win
            break

    if whatsapp_window:
        app = Application(backend="uia").connect(handle=whatsapp_window.handle)
        wa_window = app.window(handle=whatsapp_window.handle)

        messages = []
        for item in wa_window.descendants():
            if item.window_text():
                messages.append(item.window_text())

        with open("whatsapp_messages.txt", "a", encoding="utf-8") as f:
            for msg in messages:
                f.write(msg + "\n")
        print("Mensajes guardados exitosamente en 'whatsapp_messages.txt'.")
    else:
        print("No se encontró la ventana de WhatsApp.")