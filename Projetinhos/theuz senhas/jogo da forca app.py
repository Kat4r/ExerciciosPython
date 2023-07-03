from random import choice
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class JogoForca(App):
    def build(self):
        self.palavra = choice(['anfitria', 'computador', 'kocho', 'desemprego'])
        self.vidas = 6
        self.palavraSecreta = "_" * len(self.palavra)
        self.letrasListas = list(self.palavraSecreta)

        layout = BoxLayout(orientation='vertical')

        self.label_forca = Label(text=self.criar_forca(), font_size=20)
        layout.add_widget(self.label_forca)

        self.label_palavra = Label(text="Palavra secreta: " + "".join(self.letrasListas), font_size=20)
        layout.add_widget(self.label_palavra)

        self.input_chute = TextInput(multiline=False)
        layout.add_widget(self.input_chute)

        btn = Button(text="Chutar", on_press=self.verificar_chute)
        layout.add_widget(btn)

        return layout

    def criar_forca(self):
        forca = f'  ______\n' \
                f' |      |\n' \
                f' |      {"O" if self.vidas < 6 else ""}\n' \
                f' |     {"|" if self.vidas < 5 else ""}{"|" if self.vidas < 4 else ""}\n' \
                f' |      {"|" if self.vidas < 3 else ""}\n' \
                f' |     {"| " if self.vidas < 2 else ""}{"|" if self.vidas < 1 else ""}\n' \
                f'=============='
        return forca

    def verificar_chute(self, instance):
        chute = self.input_chute.text.lower()

        if not chute.isalpha() or len(chute) != 1:
            print("Somente uma LETRA por vez. ")
            self.input_chute.text = ""
            return

        encontrado = False
        for pos, letra in enumerate(self.palavra):
            if letra == chute:
                encontrado = True
                self.letrasListas[pos] = letra

        if not encontrado:
            self.vidas -= 1
            self.label_forca.text = self.criar_forca()
            self.label_palavra.text = "Palavra secreta: " + "".join(self.letrasListas)
            print(f'Vidas restantes: \033[31m{self.vidas}\033[m')

        if "_" not in self.letrasListas:
            print('\n\033[1:32mParabéns, você venceu!!\033[m')
            print(f'A palavra era \033[34m{self.palavra.upper()}\033[m!!')
            exit()

        self.input_chute.text = ""

if __name__ == "__main__":
    JogoForca().run()
