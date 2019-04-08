def setup():
    krotkaKolorow= ((204,102,0),(255,204,0),(0,0,255))# po co całą krotka, skoro tylko raz korzystasz z jej jednego koloru? W zadaniu kolory miały się zieniać.
    size (400,400)
    global x
    global y
    x = 0
    y = 0
    stroke(*krotkaKolorow[1])
    strokeWeight(8)
    fill(255,0,0)
    pass
    
def draw():
    background(204,102,0)
    global x
    global y
    rect(x, y, 40, 40, 5) #po co mu przeźroczystość, jak co klatkę amalowujesz tło?
    x+=1
    y+=1
    pass
    #na koniec miał się zatrzymać/program zamknąć
    
