from pygame import mixer

class Music:
	def __init__ (self):
		self.good = False
		try:
			mixer.init ()
			mixer.music.load ("Assets/Music/Azureflux-Strike-Witches-Get-Bitches.mp3")
			mixer.music.set_volume (.04)
			self.good = True
		except:
			print ("Failed to load music!")

	def play (self):
		if self.good:
			mixer.music.play (-1)

	def stop (self):
		if self.good:
			mixer.music.stop ()
