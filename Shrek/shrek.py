import pyautogui, time
# Puedes cambiar el valor de sleep() por
# la cantidad de segudos de tu preferencia.
time.sleep(10)

f = open("ShrekSpam", 'r')

# Ejecuta el programa, abre la página web de tu servicio
# de mensajeria favorito, selecciona el cuadro para
# ingresar texto y espera a que el script haga su travesura.
# Se enviarán 1601 mensajes así que tomará unos 5 minutos en
# terminar de ejecutarse. Elige el guión que quieras y diviértete.
# :-)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

