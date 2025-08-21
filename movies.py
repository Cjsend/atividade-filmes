from kivy.uix.boxlayout import BoxLayout # Layout para organizar os widgets
from kivy.uix.button import Button # Botão para interação
from kivy.uix.label import Label # Rótulo para exibir a piada
from kivy.uix.textinput import TextInput # Campo de entrada de texto
from kivy.app import App # Classe principal do aplicativo
import random  # Para consumir a API


class MoviesRandom(App):
    def build(self):
        self.movies = [
            {"Matrix-1999"},
            {"Toy Story-1995"},
            {"Avatar-2009"},
            {"O Rei Leão-1994"},
            {"Homem-Aranha-2002"},
            {"Inception-2010"},
            {"Titanic-1997"}
        ]

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title_label = Label(text='App de Filmes', 
        font_size=24, 
        bold=True
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        self.layout.add_widget(self.title_label)

        self.name_input = TextInput(
            hint_text='Digite seu nome',
            size_hint_y=None,
            height=40
        )

        self.layout.add_widget(self.name_input)

        self.button = Button(
            text='Sugerir filme',
            size_hint_y=None,
            height=40,
            background_color=(1, 0, 0, 1)
        )
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        self.result_label = Label(
            text='',
            font_size=18
        )
        self.layout.add_widget(self.result_label)

        return self.layout

    def on_button_press(self, instance):
        nome = self.name_input.text.strip()
        if not nome:
            self.result_label.text = "Digite seu nome!"
            return
        filme = random.choice(self.movies)
        self.result_label.text = f"{nome}, assista: {filme}"

if __name__ == '__main__':
    MoviesRandom().run()