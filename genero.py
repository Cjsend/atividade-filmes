from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.app import App
import random

class MoviesRandom(App):
    def build(self):
        self.movies = {
    "Ação": [
        "Matrix", "Homem-Aranha - 2002", "Batman - 2022", "John Wick - 2014", 
        "Mad Max: Estrada da Fúria - 2015", "Velozes e Furiosos - 2001"
    ],
    "Animação": [
        "Toy Story - 1995", "O Rei Leão - 1994", "Procurando Nemo - 2003", 
        "Shrek - 2001", "Frozen - 2013", "Zootopia - 2016"
    ],
    "Ficção Científica": [
        "Avatar - 2009", "Blade Runner - 1982", "Interestelar - 2014", 
        "O Exterminador do Futuro - 1984", "Matrix Reloaded - 2003", "Duna - 2021"
    ],
    "Aventura": [
        "Maze Runner - 2014", "Harry Potter - 2001", "Os Goonies - 1985", 
        "As Crônicas de Nárnia - 2005", "Indiana Jones - 1981", "Jurassic Park - 1993"
    ],
    "Terror": [
        "Telefone Preto - 2020", "A Entidade - 2012", "O Iluminado - 1980", 
        "Invocação do Mal - 2013", "Hereditário - 2018", "Corra! - 2017"
    ]
}

        
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title_label = Label(text='App de Filmes', font_size=24, bold=True)
        self.title_label.bind(size=self.title_label.setter('text_size'))
        self.layout.add_widget(self.title_label)

        self.name_input = TextInput(hint_text='Digite seu nome', size_hint_y=None, height=40)
        self.layout.add_widget(self.name_input)

        self.genre_spinner = Spinner(
            text='Escolha o gênero',
            values=list(self.movies.keys()),
            size_hint_y=None,
            height=40
        )
        self.layout.add_widget(self.genre_spinner)

        self.button = Button(text='Sugerir filme', size_hint_y=None, height=40, background_color=(1, 0, 0, 1))
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        self.result_label = Label(text='', font_size=18)
        self.layout.add_widget(self.result_label)

        return self.layout

    def on_button_press(self, instance):
        nome = self.name_input.text.strip()
        genero = self.genre_spinner.text
        if not nome:
            self.result_label.text = "Digite seu nome!"
            return
        if genero == 'Escolha o gênero':
            self.result_label.text = "Escolha um gênero!"
            return
        filme = random.choice(self.movies[genero])
        self.result_label.text = f"{nome}, assista: {filme}"

if __name__ == '__main__':
    MoviesRandom().run()
