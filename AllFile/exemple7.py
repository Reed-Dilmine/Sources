#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import wx

class Bonjour(wx.Frame):
    def __init__(self, titre):
        wx.Frame.__init__(self, None, 1, title = titre)
        frameSizer = wx.BoxSizer(wx.VERTICAL)
        panelSizer = wx.GridSizer(2, 2, 0, 0)
        conteneur = wx.Panel(self, 1)
        for x in range(4):
            y = x + 1
            etiquette = wx.StaticText(conteneur, 1, "Bonjour le monde ! (%s)" % y ,
                                      style = wx.ALIGN_CENTRE)
            panelSizer.Add(etiquette, 0, wx.ALIGN_CENTRE)
        conteneur.SetSizer(panelSizer)
        frameSizer.Add(conteneur, 1, wx.EXPAND)
        self.SetSizer(frameSizer)
        frameSizer.SetSizeHints(self)
        self.SetSize((400, 150))
        wx.EVT_SIZE(self, self.OnSize)
        
    def OnSize(self, evt):
        self.SetTitle("Exemple 7 %s" % evt.GetSize())
        evt.Skip()
        
class MonApp(wx.App):
    def OnInit(self):
        fen = Bonjour("Exemple 7")
        fen.Show(True)
        self.SetTopWindow(fen)
        return True
        
app = MonApp()
app.MainLoop()
