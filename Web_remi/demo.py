from remi import start, App, gui
class MyApp(App):
    def init(self, args): 
        super(MyApp, self).init(args)
    def main(self):
        container = gui.VBox(width=300, height=200, style={'margin':'5px auto'})
        self.lbl = gui.Label('你好，我是一个WebApp！')
        self.bt = gui.Button('请点击这里')
        self.bt.onclick.do(self.on_button_pressed)
        container.append(self.lbl)
        container.append(self.bt)
        return container
    def on_button_pressed(self, widget):
        self.lbl.set_text('你点击了按钮!')

start(MyApp)