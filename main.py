__author__ = 'Huis'


from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

import numpy as np
import random
import matplotlib.pyplot as plt
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm
import matplotlib
from xkcdify import XKCDify
from xkcdify import xkcd_line
import math
from matplotlib.patches import Ellipse
from matplotlib.patches import Arc

class Canvas(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Canvas, self).__init__(*args, **kwargs)
        self.createMenuBar()
        self.createToolsBar()
        self.createDrawArea()
        self.test()
        self.draw()


    def createMenuBar(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onQuit, fitem)


    def createToolsBar(self):
        toolbar = self.CreateToolBar(style=wx.TB_VERTICAL | wx.TB_RIGHT)
        squigle_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Squigle', wx.Bitmap('Squigle.png'))
        text_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Text', wx.Bitmap('Text.png'))
        red_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Red', wx.Bitmap('Red.png'))
        green_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Green', wx.Bitmap('Green.png'))
        blue_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Blue', wx.Bitmap('Blue.png'))
        black_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Black', wx.Bitmap('Black.png'))
        toolbar.Realize()
        # self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)


    def createDrawArea(self):
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()


    def test(self):
        # t = arange(0.0, 3.0, 0.01)
        # s = sin(2 * pi * t)
        # np.random.seed(0)
        #ax = pl.axes()
        self.axes.set_autoscale_on(False)
        self.axes.text(0.5, 0.8, 'Nanoteq',
             horizontalalignment='center', verticalalignment='center')
        # XKCDify(self.axes, xaxis_loc=-1, yaxis_loc=-1,
        #     xaxis_arrow='+', yaxis_arrow='+',
        #     expand_axes=True)
        # # pl.ylim([-0.2,1.2])
        # # pl.xlim([-0.2,1.2])
        # pl.show()
        #self.axes.plot(t, s)


    def draw(self):
        self.SetSize((1000, 700))
        self.SetTitle('DrawIt')
        self.ToggleWindowStyle(wx.STAY_ON_TOP & ~wx.RESIZE_BORDER) #TODO Disable Resize not working yet
        self.Centre()
        self.Show(True)

    def onQuit(self, e):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, title='DrawIt')
    panel = Canvas(frame)
    app.MainLoop()