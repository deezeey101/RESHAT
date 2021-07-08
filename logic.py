def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    def solver(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("Error")

    # Change from positive/negative
    def plus_minus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            self.outputLabel.setText(f'-{screen}')
    
    # decimal
    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(screen + ".")         

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
