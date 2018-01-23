# -*- coding:Utf-8 -*-
from tkinter import *
from math import floor
from time import sleep


class Cell:
    """Cellule"""

    def __init__(self, gb, pos, state=0, next_state=0):
        self.gb = gb
        self.pos = pos
        self.state = state
        self.next_state = next_state
        self.oval = self.gb.create_oval(
            self.pos[0]*gb.t+2, \
            self.pos[1]*gb.t+2, \
            self.pos[0]*gb.t+gb.t-2, \
            self.pos[1]*gb.t+gb.t-2, \
            fill='#FFF', width='0', tags=gb.tagCell, activefill='#433DCE')

    def get_oval(self):
        return self.oval

    def get_pos(self):
        return self.pos

    def get_state(self):
        return self.state

    def set_state(self, state):
        if self.state != state :
            if state == 1 :
                self.gb.itemconfigure(self.oval, fill='#000')
            if state == 0 :
                self.gb.itemconfigure(self.oval, fill='#FFF')
            self.state = self.next_state = state
            return 1
        return 0

    def get_next_state(self):
        return self.next_state

    def set_next_state(self, next_state):
        self.next_state = next_state

    def toggle_state(self):
        """ Toggle the state's cell """
        if self.state == 0 :
            self.state = self.next_state = 1
            self.gb.itemconfigure(self.oval, fill='#000', activefill='red')
        else:
            self.state = self.next_state = 0
            self.gb.itemconfigure(self.oval, fill='#FFF', activefill='#433DCE')

    def in_play(self):
        self.gb.itemconfigure(self.oval, activefill=self.gb.itemcget(self.oval, 'fill'))


class Gameboard(Canvas):
    """Grille contenant les cellules"""

    def __init__(self, boss=None, w=600, h=600, t=15, tagCell='cell'):
        self.boss, self.w, self.h, self.t, self.tagCell = boss, w, h, t, tagCell
        self.anim = 0
        self.create_grid()
        self.create_cells()

    def create_grid(self):
        """ Création du quadrillage """
        Canvas.__init__(self, self.boss, width=self.w+1, height=self.h+1, bg="#FFF")
        for x in range(1, self.w+2, self.t):
            self.create_line(x, 0, x, self.h+2, fill='#AAA')
        for y in range(1, self.h+2, self.t):
            self.create_line(0, y, self.w+2, y, fill='#AAA')

    def create_cells(self):
        """ Création des cellules """
        self.cells = {}
        for x in range(0, self.w//self.t):
            for y in range(0, self.h//self.t):
                cell = Cell(self, (x, y))
                self.cells[(x, y)] = cell
        self.tag_bind(self.tagCell, '<Button-1>', self.toggle_cell_state)

    def toggle_cell_state(self, event):
        """ Find the cell and toggle its state via appropriate class """
        self.cells[floor(event.x//self.t), floor(event.y//self.t)].toggle_state()

    def start(self):
        """ Lancement du jeu """
        # on contrôle que le jeu n'est pas déjà lancé
        if self.anim == 1 :
            return
        self.anim = 1
        # Désactivation de la fonctionnalité de changement d'état d'une cellule
        self.tag_unbind(self.tagCell, '<Button-1>')
        # Désactivation du hover sur les cellules
        for i, c in self.cells.items() :
            c.in_play()
        # Lancement de l'animation
        self.animer()

    def animer(self):
        for i, c in self.cells.items() :
            nb = self.get_nb_near(c)
            if c.get_state() == 0 and nb == 3 :
                c.set_next_state(1)
            elif c.get_state() == 1 and nb != 2 and nb != 3 :
                c.set_next_state(0)
        fin = 1
        for i, c in self.cells.items() :
            if c.set_state(c.get_next_state()) == 1 :
                fin = 0
        if fin == 1 :
            self.reset()
        if self.anim == 1 :
            self.after(300, self.animer)

    def get_nb_near(self, cell):
        (x, y) = cell.get_pos()
        near_pos = ((x-1,y-1),(x-1,y),(x,y-1),(x-1,y+1),(x+1,y-1),(x+1,y),(x,y+1),(x+1,y+1))
        cpt = 0
        for c in near_pos :
            if self.cells.get(c, None) != None :
                cpt += self.cells[c].get_state()
        return cpt

    def reset(self):
        """ Stoppe l'animation et recrée les cellules """
        self.anim = 0
        self.delete(self.tagCell)
        self.create_cells()


class Application(Frame):
    """Application principale du jeu de la vie"""

    def __init__(self, boss =None):
        """ Initialisation et positionnement des widgets """

        Frame.__init__(self, parent=boss, bg='#EEE')
        self.master.title('Jeu de la vie')

        self.gameboard = Gameboard(self)
        self.gameboard.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        self.btn_start = Button(self, text ="Start", command=self.gameboard.start, \
        bg='#04AB0A', fg='#FFF', activebackground='#1FD826', activeforeground='#FFF', \
        cursor='hand1', relief='flat', overrelief='flat')
        self.btn_start.grid(row=2, column=1, sticky=E, pady=10)

        self.btn_reset= Button(self, text ="Stop", command=self.gameboard.reset, \
        bg='#3D6790', fg='#FFF', activebackground='#5E8BB6', activeforeground='#FFF', \
        cursor='hand1', relief='flat', overrelief='flat')
        self.btn_reset.grid(row=2, column=2, pady=10)

        self.btn_quit= Button(self, text ="Quit", command =quit, \
        bg='#D10518', fg='#FFF', activebackground='#EA3243', activeforeground='#FFF', \
        cursor='hand1', relief='flat', overrelief='flat')
        self.btn_quit.grid(row=2, column=3, sticky=W, pady=10)

        self.grid()


if __name__ == '__main__':
    Application().mainloop()
