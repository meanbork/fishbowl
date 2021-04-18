from kivy.app import App
from kivymd.theming import ThemeManager
from plyer import battery, tts, vibrator
from kivymd.toast import toast


class MainApp(App):
	theme_cls = ThemeManager()
	
	def show_battery_info(self):
		print(battery.status)
		toast(str(battery.status))
	def vibrate(self):
		vibrator.pattern([0, 1, 0, 1])
	def speak(self, text_to_read):
		tts.speak(text_to_read)		
	
MainApp().run()

