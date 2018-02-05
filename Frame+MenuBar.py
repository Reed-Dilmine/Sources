#-------------------------------------------------------------------------------
# Name:        Frame + MenuBar
# Purpose:
#
# Author:      dlemen
#
# Created:     05/02/2018
# Copyright:   (c) dlemen 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

class MenuBar(Frame):
	"""Barre de menus déroulants"""
	def __init__(self, boss =None):
		Frame.__init__(self, borderwidth =2)

		##### Menu <Fichier> #####
		fileMenu = Menubutton(self, text ='Fichier')
		fileMenu.pack(side =LEFT)
		# Partie "déroulante" :
		me1 = Menu(fileMenu)
		me1.add_command(label ='Effacer', underline =0,
		command = boss.effacer)
		me1.add_command(label ='Terminer', underline =0,
		command = boss.master.destroy)
		# Intégration du menu :
		fileMenu.configure(menu = me1)

class Application(Frame):
	"""Application principale"""
	def __init__(self, boss =None):
		Frame.__init__(self)
		self.master.title('Fenêtre avec menus')
		mBar = MenuBar(self)
		mBar.pack()
		self.can = Canvas(self, bg='light grey', height=190,
		width=250, borderwidth =2)
		self.can.pack()
		self.pack()

	def effacer(self):
		self.can.delete(ALL)

if __name__ == '__main__':
	app = Application()
	app.mainloop()