#from pykeyboard import PyKeyboardEvent


class KeyboardListener(PyKeyboardEvent):
    """
    Cette classe permet de regarder qu'elles sont les touches qui sont
    pressées ou relâchée par l'utilisateur.
    """
    def __init__(self):
        super(KeyboardListener, self).__init__()

    def tap(self, keycode, character, press):
        """
        Cette fonction détermine l'action a effectuer en fonction
        de la touche pressée ou relâchée.

        Args:
            keycode (int): Code du touche.
            character (str): Nom de la touche.
            press (bool): True si la touche est pressée, False si relachée.

        """
        if press:
            print("La touche", character, "est pressée.")
        else:
            print("La touche", character, "est relâchée.")


# Création de l'espion et lancement de l'écoute
keyboard = KeyboardListener()
keyboard.run()