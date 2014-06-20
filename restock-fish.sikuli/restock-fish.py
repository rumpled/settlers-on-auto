Settings.MoveMouseDelay = 0.1
#focus window
a = App.focus('/Applications/Google Chrome.app')
for i in range(0,80):
    click("1372840843780.png")
    wait("1372840865740.png") 
    click("1372840865740.png")
    click(Pattern("1372844008665.png").targetOffset(-13,22))
    click("1372840843780.png")
    wait("1372840865740.png")
    click("1372840865740.png")
    click(Pattern("1372844057982.png").targetOffset(15,18))
