from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.app import App
import random
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        self.name_input = TextInput(hint_text='Digite seu nome', size_hint_y=None, height=40)
        self.layout.add_widget(self.name_input)
        self.continue_button = Button(text='Continuar')
        self.continue_button.bind(on_press=self.go_to_suggestion)
        self.add_widget(self.continue_button)
        class SuggestionScreen(Screen):
            def __init__(self, **kwargs):
                super(SuggestionScreen, self).__init__(**kwargs)
                self.welcome_label = Label(text='Bem-vindo(a)!')
                self.add_widget(self.welcome_label)
                self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
                self.title_label = Label(text='App de Filmes', font_size=24, bold=True)
                self.title_label.bind(size=self.title_label.setter('text_size'))
                self.layout.add_widget(self.title_label)
                self.genre_spinner = Spinner(
                    text='Escolha o gênero',
                    values=list(self.movies.keys()),
                    size_hint_y=None,
                    height=40
                )
                self.layout.add_widget(self.genre_spinner)
                self.limpar_button = Button(text='Limpar', size_hint_y=None, height=40, background_color=(0, 0, 1, 1))
                self.limpar_button.bind(on_press=self.on_button_limpar)
                self.layout.add_widget(self.limpar_button)
                self.button = Button(text='Sugerir filme', size_hint_y=None, height=40, background_color=(1, 0, 0, 1))
                self.button.bind(on_press=self.on_button_press)
                self.layout.add_widget(self.button)
                self.result_label = Label(text='', font_size=18)
                self.layout.add_widget(self.result_label)
                return self.layout
            def on_button_press(self, instance):
                genero = self.genre_spinner.text
                
                if genero == 'Escolha o gênero':
                    self.result_label.text = "Escolha um gênero!"
                    return
                filme = random.choice(self.movies[genero])
                self.result_label.text = f"{nome}, assista: {filme}"
            def on_button_limpar(self, instance):
                    self.name_input.text = ''
                    self.genre_spinner.text = 'Escolha o gênero'
                    self.result_label.text = ''
            def suggest_movie(self):
                self.movies = {
                                "Ação": [
                        "Matrix - 1999", "Homem-Aranha - 2002", "Batman - 2022", "John Wick - 2014", 
                        "Mad Max: Estrada da Fúria - 2015", "Velozes e Furiosos - 2001",
                        "Gladiador - 2000", "Missão: Impossível - 1996", "Duro de Matar - 1988",
                        "Pantera Negra - 2018", "Capitão América: O Soldado Invernal - 2014",
                        "O Protetor - 2014", "Rambo: Programado para Matar - 1982",
                        "O Último Samurai - 2003", "300 - 2006", "Coração Valente - 1995",
                        "Homem de Ferro - 2008", "Thor: Ragnarok - 2017", "Capitão Marvel - 2019",
                        "Mulher-Maravilha - 2017", "Esquadrão Suicida - 2016", "Deadpool - 2016",
                        "O Justiceiro - 2004", "O Livro de Eli - 2010", "Tropa de Elite - 2007",
                        "Rei Arthur: A Lenda da Espada - 2017", "O Último Dragão - 1985"
                    ],
                    "Animação": [
                        "Toy Story - 1995", "O Rei Leão - 1994", "Procurando Nemo - 2003", 
                        "Shrek - 2001", "Frozen - 2013", "Zootopia - 2016",
                        "Up: Altas Aventuras - 2009", "Divertida Mente - 2015", "Moana - 2016",
                        "Os Incríveis - 2004", "Kung Fu Panda - 2008", 
                        "Ratatouille - 2007", "Carros - 2006", "WALL-E - 2008",
                        "A Era do Gelo - 2002", "Meu Malvado Favorito - 2010",
                        "A Bela e a Fera - 1991", "Aladdin - 1992", "Mulan - 1998",
                        "Enrolados - 2010", "Luca - 2021", "Soul - 2020",
                        "Viva: A Vida é uma Festa - 2017", "Big Hero 6 - 2014"
                    ],
                    "Ficção Científica": [
                        "Avatar - 2009", "Blade Runner - 1982", "Interestelar - 2014", 
                        "O Exterminador do Futuro - 1984", "Matrix Reloaded - 2003", "Duna - 2021",
                        "Gravidade - 2013", "Star Wars: Uma Nova Esperança - 1977", "Star Trek - 2009",
                        "E.T. - O Extraterrestre - 1982", "A Chegada - 2016",
                        "RoboCop - 1987", "O Quinto Elemento - 1997", "Minority Report - 2002",
                        "Planeta dos Macacos: A Origem - 2011", "Distrito 9 - 2009",
                        "Matrix Revolutions - 2003", "Alien - 1979", "Aliens: O Resgate - 1986",
                        "O Predador - 1987", "Guerra Mundial Z - 2013", "Eu, Robô - 2004",
                        "A Guerra dos Mundos - 2005", "Passageiros - 2016"
                    ],
                    "Aventura": [
                        "Maze Runner - 2014", "Harry Potter - 2001", "Os Goonies - 1985", 
                        "As Crônicas de Nárnia - 2005", "Indiana Jones - 1981", "Jurassic Park - 1993",
                        "Piratas do Caribe: A Maldição do Pérola Negra - 2003", "Jumanji - 1995",
                        "Rei Arthur: A Lenda da Espada - 2017", "A Viagem de Chihiro - 2001",
                        "O Hobbit - 2012", "O Senhor dos Anéis: A Sociedade do Anel - 2001",
                        "King Kong - 2005", "Tarzan - 1999", "A Múmia - 1999",
                        "Percy Jackson e o Ladrão de Raios - 2010",
                        "Jurassic World - 2015", "Tróia - 2004", "Robin Hood - 2010",
                        "Atlantis: O Reino Perdido - 2001", "Planeta do Tesouro - 2002",
                        "Procurando El Dorado - 2000", "Pocahontas - 1995"
                    ],
                    "Terror": [
                        "Telefone Preto - 2020", "A Entidade - 2012", "O Iluminado - 1980", 
                        "Invocação do Mal - 2013", "Hereditário - 2018", "Corra! - 2017",
                        "Halloween - 1978", "Pânico - 1996", "It: A Coisa - 2017",
                        "A Bruxa - 2015", "Atividade Paranormal - 2007",
                        "Annabelle - 2014", "O Chamado - 2002", "Poltergeist - 1982",
                        "Cemitério Maldito - 1989", "O Massacre da Serra Elétrica - 1974",
                        "A Freira - 2018", "Boneco do Mal - 2016", "O Babadook - 2014",
                        "O Orfanato - 2007", "Verónica - 2017", "A Chave Mestra - 2005",
                        "A Casa de Cera - 2005", "O Exorcista - 1973"
                    ],
                    "Drama": [
                        "À Procura da Felicidade - 2006", "Forrest Gump - 1994", "Clube da Luta - 1999",
                        "O Poderoso Chefão - 1972", "O Curioso Caso de Benjamin Button - 2008",
                        "Cidade de Deus - 2002", "12 Anos de Escravidão - 2013",
                        "Sociedade dos Poetas Mortos - 1989", "O Pianista - 2002",
                        "Beleza Americana - 1999", "A Lista de Schindler - 1993"
                    ],
                    "Comédia": [
                        "Se Beber, Não Case - 2009", "As Branquelas - 2004", "Debi & Lóide - 1994",
                        "Click - 2006", "O Mentiroso - 1997", "Norbit - 2007",
                        "Superbad - 2007", "Todo Mundo em Pânico - 2000", "Esposa de Mentirinha - 2011",
                        "O Máskara - 1994", "Entrando Numa Fria - 2000"
                    ],
                    "Romance": [
                        "Titanic - 1997", "Diário de uma Paixão - 2004", "Um Amor para Recordar - 2002",
                        "Simplesmente Acontece - 2014", "Como Eu Era Antes de Você - 2016",
                        "Amizade Colorida - 2011", "Amor e Outras Drogas - 2010",
                        "Querido John - 2010", "Cartas para Julieta - 2010", "P.S. Eu Te Amo - 2007"
                    ],
                    "Suspense": [
                        "Ilha do Medo - 2010", "Garota Exemplar - 2014", "Seven: Os Sete Crimes Capitais - 1995",
                        "O Silêncio dos Inocentes - 1991", "Fragmentado - 2016", "Corpo Fechado - 2000",
                        "Os Outros - 2001", "Prisioneiros - 2013", "Um Contratempo - 2016",
                        "Oldboy - 2003", "O Sexto Sentido - 1999"
                    ]
                }
        
class MovieApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(SuggestionScreen(name='suggestion'))
        return sm



if __name__ == '__main__':
    MovieApp().run()
