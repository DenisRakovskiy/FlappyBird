x1=500
x=255
txt=0
y1=-770
state = 0
f1=0
true = 0
false = 0

def rectsCollide(x,y,w,h, x1,y1,w1,h1):
    def check_collide(x,y,w,h, x1,y1):
        return x1>=x and x1 <= x+w and y1 >= y and y1 <= y+h
    return check_collide(x,y, w, h , x1, y1) or \
           check_collide(x,y, w, h , x1, y1+h1) or \
           check_collide(x,y, w, h , x1+w1, y1) or \
           check_collide(x,y, w, h , x1+w1, y1+h1)

def setup() :
    global chicken,truba1,truba2,state,start,phone
    chicken = loadImage(u'KURICA.png')
    truba1  = loadImage(u'TRUBA.png')
    truba2 = loadImage(u'TRUBA2.png')
    start = loadImage(u'start.png')
    phone = loadImage (u'ANIME.jpg')
    size (500,500)     
    textSize(15)
    fill(0)
    noStroke()
def draw():
    global x,t,x1,txt,y1,state,record,f1,true,false
    if state == 0:
        background(255)
        image(phone,250,200,255,255)
        image(start,255,255,90,70)
        textSize(60)
        
        if mousePressed:
            if mouseX > 255 and mouseY > 255 and mouseX < 255+60 and mouseY < 255+60:
                state = 1
    elif state == 1:
        x+=2
        x1-=2
        background('#03FFFD')

        fill(255,255,0)
        if (rectsCollide(x1,y1, 50, 1000 , 255 , x , 25,25) or rectsCollide(x1,y1+1080, 50, 1000 , 255 , x , 25,25)):
                background(255)
                textSize(50)
                text("GameOver",140,250)
                x=1000

        image(chicken , 255,x , 25,25)
    
    
        fill(0,255,0)
        image(truba1,x1,y1, 50, 1000)
        image(truba2,x1,y1 + 1080, 50, 1000)
        textSize(20)
        fill("#8531B9")
        text( 'x:'+str(mouseX),0,30)
        text('y:'+str(mouseY),0,60)
        textSize(30)
        text("score:",0,90)
        text(txt,0,120)
        text(record,0,240)
        fill('#3D40BC')
        if keyPressed:
            if key == "0":
                x-=5
        if x<0:
            background(255)
            textSize(50)
            text("GameOver",140,250)
            x-=10
        if x>485:
            background(255)
            textSize(50)
            text("GameOver",140,250)
            x+=10
        if x1<-50:
            y1= random(-1000,-450)
            x1=500
        if x1==160:
            txt+=1

    

    
    
        
