#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import wx

class Bonjour(wx.Frame):
    def __init__(self, titre):
        wx.Frame.__init__(self, None, 1, title = titre)
        frameSizer = wx.BoxSizer(wx.VERTICAL)
        panelSizer = wx.BoxSizer(wx.HORIZONTAL)
        conteneur = wx.Panel(self, 1)
        etiquette = wx.StaticText(conteneur, 1, "Bonjour tout le monde !", style = wx.ALIGN_CENTRE)
        panelSizer.Add(etiquette, 1, wx.ALIGN_CENTRE)
        conteneur.SetSizer(panelSizer)
        frameSizer.Add(conteneur, 1, wx.EXPAND)
        self.SetSizer(frameSizer)
        frameSizer.SetSizeHints(self)
        self.SetSize((200, 100))

class MonApp(wx.App):
    def OnInit(self):
        fen = Bonjour("Exemple 4")
        fen.Show(True)
        self.SetTopWindow(fen)
        return True

app = MonApp(redirect = False)
app.MainLoop()
