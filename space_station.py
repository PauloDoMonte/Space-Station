import pyxel
import os.path
import shelve

class status(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b

class Explorer(object):
	
	def __init__(self):
		pyxel.init(255,255, caption="Explorer I 0.0.1")
		self.status_window = status(0,"inicio")
		card = shelve.open('save_game')
		self.money = card['dinheiro']
		self.sci = card['ciencia']
		card.close()
		pyxel.mouse(True)
		pyxel.run(self.update, self.draw)
		
	def draw_money(self,x,y):
		self.x = x
		self.y = y
		money = "${:04}".format(self.money)
		pyxel.text(self.x,self.y,money, 11)
		
	def draw_sci(self,x,y):
		self.x = x
		self.y = y
		sci = "SCI: {:04}".format(self.sci)
		pyxel.text(self.x,self.y,sci,11)
		
	#	TERRA
	def draw_controle(self):
		pyxel.cls(0)
		self.draw_money(100,1)
		self.draw_sci(100,11)
		
		#	COMPUTADOR
		pyxel.rect(0,0,50,255,11)	# BARRA LATERAL
		pyxel.text(5,10,"CONTROLE", 7)
		pyxel.text(5,20, "PESQUISA", 1)
		pyxel.text(5,30, "ASTRONAUTAS", 1)
		pyxel.text(5,40, "CONSTRUCAO", 1)
		pyxel.text(5,50, "MONTAGEM", 1)
		pyxel.text(5,60, "LANCAMENTO", 1)
	
	def draw_pesquisa(self):
		pyxel.cls(0)
		
		#	COMPUTADOR
		pyxel.rect(0,0,50,255,11)	# BARRA LATERAL
		pyxel.text(5,10, "SPACECRAFT",7)
		pyxel.text(5,20, "SATELITE", 1)
		pyxel.text(5,30, "FOGUETE", 1)
		pyxel.text(5,40, "MOTORES", 1)
		pyxel.text(5,50, "PROPRELENTE",1)
		pyxel.text(5,60, "COMUNICACAO",1)
		pyxel.text(0,248, "<- VOLTAR", 1)
		
	def draw_astronautas(self):
		pyxel.cls(0)
		pyxel.rect(0,0,50,255,11)	# BARRA LATERAL		
		pyxel.text(5,10, "RECRUTAR",7)
		pyxel.text(5,20, "TREINAMENTO",1)
		pyxel.text(0,248, "<- VOLTAR", 1)

	def draw_construcao(self):
		pyxel.cls(0)
		pyxel.rect(0,0,50,255,11)	# BARRA LATERAL		
		pyxel.text(0,248, "<- VOLTAR", 1)
		
	def draw_montagem(self):	
		pyxel.cls(0)
		pyxel.rect(0,0,50,255,11)	# BARRA LATERAL		
		pyxel.text(5,10, "SPACECRAFT",7)
		pyxel.text(5,20, "SATELITE",1)
		pyxel.text(5,30, "FOGUETE",1)
		pyxel.text(0,248, "<- VOLTAR", 1)
		
	def draw_lancamento(self):
		pyxel.cls(0)
		pyxel.rect(0,0,50,255,11)	# BARRA LATERAL		
		pyxel.text(5,10, "NAVE",7)
		pyxel.text(5,20,"CARGA",1)
		pyxel.text(5,30, "TRIPULACAO",1)
		pyxel.text(5,40, "ASTRO",1)
		pyxel.text(5,50, "ORBITA",1)
		pyxel.text(0,248, "<- VOLTAR", 1)
		
	def window(self):
		if self.status_window.b == "inicio":
			pyxel.cls(0)
			pyxel.text(90, 55, "Explorer I 0.0.1", pyxel.frame_count % 16)
			pyxel.text(90, 65, "PRESS ENTER TO START", pyxel.frame_count % 16)
			pyxel.text(90, 75, "PRESS Q TO QUIT", pyxel.frame_count % 16)
		
		#	TERRA
		if self.status_window.a == 1:
			if self.status_window.b == "controle":
				self.draw_controle()

			if self.status_window.b == "pesquisa":
				self.draw_pesquisa()				
			
			if self.status_window.b == "astronautas":
				self.draw_astronautas()
			
			if self.status_window.b == "construcao":
				self.draw_construcao()
				
			if self.status_window.b == "montagem":
				self.draw_montagem()
			
			if self.status_window.b == "lancamento":
				self.draw_lancamento()
		
	def update(self):
		if pyxel.btn(pyxel.KEY_Q):
			pyxel.quit()
			
		if pyxel.btn(pyxel.KEY_ENTER):
			if self.status_window.b == "inicio":
				self.status_window.a = 1
				self.status_window.b = "controle"
				
		#	MENU DO CONTROLE
		if self.status_window.b == "controle":
			if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
				#	PESQUISA
				if(pyxel.mouse_x >= 5 and pyxel.mouse_x <= 35):
					if(pyxel.mouse_y >= 20 and pyxel.mouse_y <= 25):
						self.status_window.b = "pesquisa"
				
				#	ASTRONAUTA
				if(pyxel.mouse_x >= 5 and pyxel.mouse_x <= 47):
					if(pyxel.mouse_y >= 30 and pyxel.mouse_y <= 35):
						self.status_window.b = "astronautas"
						
				#	CONSTRUCAO
				if(pyxel.mouse_x >= 5 and pyxel.mouse_x <= 43):
					if(pyxel.mouse_y >= 40 and pyxel.mouse_y <= 45):
						self.status_window.b = "construcao"
				
				#	MONTAGEM
				if(pyxel.mouse_x >= 5 and pyxel.mouse_x <= 46):
					if(pyxel.mouse_y >= 50 and pyxel.mouse_y <= 55):
						self.status_window.b = "montagem"
				
				#	LANCAMENTO
				if(pyxel.mouse_x >= 5 and pyxel.mouse_x <= 46):
					if(pyxel.mouse_y >= 60 and pyxel.mouse_y <= 65):
						self.status_window.b = "lancamento"
				
						
		#	MENU DA PESQUISA
		if self.status_window.b == "pesquisa":
			if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
				#	VOLTAR
				if(pyxel.mouse_x >= 0 and pyxel.mouse_x <=40):
					if(pyxel.mouse_y >= 248 and pyxel.mouse_y <= 253):
						self.status_window.b = "controle"
		
		#	MENU DOS ASTRONAUTAS
		if self.status_window.b == "astronautas":
			if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
				#	VOLTAR
				if(pyxel.mouse_x >= 0 and pyxel.mouse_x <=40):
					if(pyxel.mouse_y >= 248 and pyxel.mouse_y <= 253):
						self.status_window.b = "controle"		
		
		#	MENU DA CONSTRUCAO
		if self.status_window.b == "construcao":
			if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
				#	VOLTAR
				if(pyxel.mouse_x >= 0 and pyxel.mouse_x <=40):
					if(pyxel.mouse_y >= 248 and pyxel.mouse_y <= 253):
						self.status_window.b = "controle"		
		
		#	MENU DA MONTAGEM
		if self.status_window.b == "montagem":
			if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
				#	VOLTAR
				if(pyxel.mouse_x >= 0 and pyxel.mouse_x <=40):
					if(pyxel.mouse_y >= 248 and pyxel.mouse_y <= 253):
						self.status_window.b = "controle"
		
		#	MENU DO LANCAMENTO
		if self.status_window.b == "lancamento":
			if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
				#	VOLTAR
				if(pyxel.mouse_x >= 0 and pyxel.mouse_x <=40):
					if(pyxel.mouse_y >= 248 and pyxel.mouse_y <= 253):
						self.status_window.b = "controle"		
	
	def draw(self):
		self.window()
		
if(os.path.exists("save") != True):
	card = shelve.open('save_game')
	card['dinheiro'] = 1000000.0
	card['ciencia'] = 10.0
	card.close()
Explorer()
