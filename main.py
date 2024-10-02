from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.clock import Clock

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        with self.canvas:
            # Fondo azul (#5EA5FB)
            Color(0.368, 0.647, 0.984, 1)  # Convertido de #5EA5FB
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

            # Cuadro blanco detrás del logo con esquinas redondeadas
            Color(1, 1, 1, 1)  # Blanco
            self.white_box = RoundedRectangle(pos=(Window.width / 2 - 105, Window.height / 2 - 80), size=(210, 160), radius=[20])

        # Imagen del logo centrada
        self.logo = Image(source='logo.png', size_hint=(None, None), size=(200, 150))
        self.logo.pos = (Window.width / 2 - self.logo.width / 2, Window.height / 2 - self.logo.height / 2)
        self.add_widget(self.logo)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        with self.canvas.before:  # Dibujamos el fondo antes de los botones
            # Fondo azul claro
            Color(0.368, 0.647, 0.984, 1)  # Color #5EA5FB
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

            # Cuadro blanco con esquinas redondeadas
            Color(1, 1, 1, 1)  # Blanco
            padding = 20  # Espacio alrededor del cuadro
            self.white_box = RoundedRectangle(
                pos=(padding, padding), 
                size=(Window.width - 2 * padding, Window.height - 2 * padding), 
                radius=[25]  # Redondeado
            )
        
        # Ahora los botones se dibujan encima del cuadro blanco
        # Botón "ABC" (Letras)
        self.letras_button = Button(
            size_hint=(None, None),  
            size=(300, 200),  
            pos_hint={'center_x': 0.5, 'center_y': 0.75},  # Alineado al centro
            background_normal='letras.png',  
            background_down='letras.png',
            border=(0, 0, 0, 0)  
        )
        self.add_widget(self.letras_button)

        # Botón "Colores"
        self.colores_button = Button(
            size_hint=(None, None),  
            size=(300, 200),  
            pos_hint={'center_x': 0.5, 'center_y': 0.5},  # Alineado al centro
            background_normal='Sin título-4.png',  
            background_down='Sin título-4.png',  
            border=(0, 0, 0, 0)  
        )
        self.add_widget(self.colores_button)

        # Botón "Figuras"
        self.figuras_button = Button(
            size_hint=(None, None),  
            size=(300, 200),  
            pos_hint={'center_x': 0.49, 'center_y': 0.25},  # Alineado al centro
            background_normal='Sin título-2.png',  
            background_down='Sin título-2.png',  
            border=(0, 0, 0, 0)  
        )
        self.add_widget(self.figuras_button)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.white_box.pos = (20, 20)  # Mantén el cuadro blanco con espacio en los bordes
        self.white_box.size = (Window.width - 40, Window.height - 40)  # Actualiza el tamaño si la ventana cambia

class KidsityApp(App):
    def build(self):
        sm = ScreenManager()
        self.loading_screen = LoadingScreen(name='loading')
        self.main_screen = MainScreen(name='main')
        sm.add_widget(self.loading_screen)
        sm.add_widget(self.main_screen)

        # Cambiar a la pantalla principal después de 4 segundos
        Clock.schedule_once(self.switch_to_main, 4)
        return sm

    def switch_to_main(self, dt):
        self.root.current = 'main'

if __name__ == '__main__':
    KidsityApp().run()