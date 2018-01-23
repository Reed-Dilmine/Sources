#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import wx

class LesMenus(wx.Frame):
    def __init__(self, titre):
        wx.Frame.__init__(self, None, 1, title = titre, size = (400, 200))

        menuFichier = wx.Menu(style = wx.MENU_TEAROFF)
        menuFichier.Append(wx.ID_OPEN, "&Ouvrir\tCTRL+o", "menu ouvrir")
        menuFichier.Append(wx.ID_CLOSE, "&Fermer\tCTRL+f", "menu fermer")
        menuFichier.AppendSeparator()
        menuFichier.Append(wx.ID_EXIT, "&Quitter\tCTRL+q", "menu quitter")

        menuBarre = wx.MenuBar()
        menuBarre.Append(menuFichier, "&Fichier")
        self.SetMenuBar(menuBarre)

        self.barre = wx.StatusBar(self, 1)
        self.barre.SetFieldsCount(2)
        self.barre.SetStatusWidths([1,1])
        self.SetStatusBar(self.barre)

        wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, wx.ID_OPEN, self.OnOpen)
        wx.EVT_MENU(self, wx.ID_CLOSE, self.OnClose)

    def OnOpen(self, evt):
        self.barre.SetStatusText("Choix = Ouvrir", 1)

    def OnClose(self, evt):
        self.barre.SetStatusText("Choix = Fermer", 1)

    def OnExit(self, evt):
        self.Destroy()

class MonApp(wx.App):
    def OnInit(self):
        fen = LesMenus("Exemple 9")
        fen.Show(True)
        self.SetTopWindow(fen)
        return True

app = MonApp()
app.MainLoop()
