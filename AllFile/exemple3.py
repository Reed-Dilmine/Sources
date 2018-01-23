#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import wx

class Bonjour(wx.Frame):
    def __init__(self, titre):
        wx.Frame.__init__(self, parent = None, id = 1, title = titre, size = (250, 120))
        self.conteneur = wx.Panel(self, 1, size = self.GetClientSize())
        self.etiquette = wx.StaticText(self.conteneur, 1, "Bonjour tout le monde !",
                                          style = wx.ALIGN_CENTRE)
        self.etiquette.CentreOnParent()
        wx.EVT_SIZE(self, self.OnSize)

    def OnSize(self, evt):
        self.SetTitle("Exemple 3 %s" % evt.GetSize())
        self.conteneur.SetSize(self.GetClientSize())
        self.etiquette.CentreOnParent()

class MonApp(wx.App):
    def OnInit(self):
        fen = Bonjour("Exemple 3")
        fen.Show(True)
        self.SetTopWindow(fen)
        return True

app = MonApp()
app.MainLoop()
