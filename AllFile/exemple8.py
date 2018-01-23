#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import wx

class LesMenus(wx.Frame):
    def __init__(self, titre):
       wx.Frame.__init__(self, None, 1, title = titre, size = (400, 200))
       menuFichier = wx.Menu()
       menuFichier.Append(wx.ID_OPEN, "&Ouvrir\tCTRL+o")
       menuFichier.Append(wx.ID_CLOSE, "&Fermer\tCTRL+f")
       menuFichier.AppendSeparator()
       menuFichier.Append(wx.ID_EXIT, "&Quitter\tCTRL+q")
       menuBarre = wx.MenuBar()
       menuBarre.Append(menuFichier, "&Fichier")
       self.SetMenuBar(menuBarre)

class MonApp(wx.App):
    def OnInit(self):
        fen = LesMenus("Exemple 8")
        fen.Show(True)
        self.SetTopWindow(fen)
        return True

app = MonApp()
app.MainLoop()
