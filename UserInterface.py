import wx
import recipe

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        self.text_ctrl2 = wx.TextCtrl(panel)
        self.text_ctrl3 = wx.TextCtrl(panel)
        self.text_ctrl4 = wx.TextCtrl(panel)
        my_sizer.AddMany([
            (self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5),
            (self.text_ctrl2, 0, wx.ALL | wx.EXPAND, 5),
            (self.text_ctrl3, 0, wx.ALL | wx.EXPAND, 5),
            (self.text_ctrl4, 0, wx.ALL | wx.EXPAND, 5)])        
        my_btn = wx.Button(panel, label='submit')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)        
        self.Show()


    def on_press(self, event):
        id = self.text_ctrl.GetValue()
        name = self.text_ctrl2.GetValue()
        ingredients = self.text_ctrl3.GetValue()
        method = self.text_ctrl4.GetValue()

        if not id or not name:
            # no val
            print("Required")
        else:
            recipe.new_Recipe(id, name, ingredients, method, link="google.com")



def run():
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()