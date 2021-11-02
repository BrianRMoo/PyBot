import wolframalpha
import wikipedia
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Personal Python Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        
        self.Show()

    def OnEnter(self, event):
        queryInput = self.txt.GetValue()
        queryInput = queryInput.lower()
        try:
            app_id ="" #API KEY HERE
            client = wolframalpha.Client(app_id)
            
            res=client.query(queryInput)
            answer = next(res.results).text
            print("WolframpAlpha: " + answer + '\n')
           
        except StopIteration:
            print("WolframAlpha: Too broad, try narrowing your search terms or check your spelling.")
            try:            
            #Client creation wikipedia
            #wikipedia.summary(query, sentencesToDisplay)
                
                print("Wikipedia: " + wikipedia.summary(queryInput, sentences=4, chars= 0, auto_suggest = False))
                
            except wikipedia.PageError():
                print("Wikipedia results in error")
            #pass
        
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()




