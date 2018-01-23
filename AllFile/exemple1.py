#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import wx

class Bonjour(wx.Frame):
    def __init__(self, titre):
        wx.Frame.__init__(self, None, 1, title = titre, size = (200, 100))
        conteneur = wx.Panel(self, 1, size = self.GetClientSize())
        etiquette = wx.StaticText(conteneur, 1, "Bonjour tout le monde !",
                                   style = wx.ALIGN_CENTRE)
        etiquette.CentreOnParent()

class MonApp(wx.App):
    def OnInit(self):
        fen = Bonjour("Exemple 1")
        fen.Show(True)
        self.SetTopWindow(fen)
        return True

app = MonApp()
app.MainLoop()
