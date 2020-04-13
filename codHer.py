import pyglet
import math
# imports pyglets library
import random
from pyglet.window import Window, mouse, gl, key
#from pyglet.media import avbin
 
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
 
mygame = pyglet.window.Window(790, 700,                     # setting window
              resizable=False,  
              caption="CodHer",  
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False                                   # For flicker-free animation
              )                                             # Calling base class constructor
mygame.set_location(screen.width // 2 - 200,screen.height//2 - 350)
 
girlImage1 = pyglet.image.load_animation('media/sofi.gif')                 
girlImage2 = pyglet.image.load_animation('media/transparentF.gif')
girlImage3 = pyglet.image.load_animation('media/transparentN.gif')
girlImage4 = pyglet.image.load_animation('media/transparentW.gif')
girlSprite= pyglet.sprite.Sprite(girlImage1, 200, 0)
girlSprite.visible = False
girlSprite.scale =0.7

bgimage= pyglet.image.load('media/city.png')

obstacleimage1 = pyglet.image.load_animation('media/firewall.gif')
obstacleimage2 = pyglet.image.load_animation('media/bug.gif')
obstacleSprite = pyglet.sprite.Sprite(obstacleimage1, 800, 60)
obstacleSprite.scale = 2
obstacleSprite.visible =False


backSprite = pyglet.sprite.Sprite(bgimage, 0, 0)               
backSprite.visible = False

logoimage=pyglet.image.load('media/main2.PNG')
logosprite=pyglet.sprite.Sprite(logoimage, 0, 0)                 
logosprite.visible=True

inst=pyglet.image.load('media/help.png')
instsprite=pyglet.sprite.Sprite(inst, 0, 0)                 # sprite for help an instructions
instsprite.visible=False

menuimage = pyglet.image.load('media/menu.png')
menusprite = pyglet.sprite.Sprite(menuimage, 0, 0)          # sprite for menu
menusprite.visible= True

winimage = pyglet.image.load('media/win.png')
winsprite = pyglet.sprite.Sprite(winimage, 0, 0)          # sprite for winscreen
winsprite.visible= False

looseimage = pyglet.image.load('media/loose.png')
loosesprite = pyglet.sprite.Sprite(looseimage, 0, 0)          # sprite for loosescreen
loosesprite.visible= False

avatarimage = pyglet.image.load('media/avatars.PNG')
avatarsprite = pyglet.sprite.Sprite(avatarimage, 0, 0)          # sprite for avatars
avatarsprite.visible= False

levelimage = pyglet.image.load('media/levels.png')
levelsprite = pyglet.sprite.Sprite(levelimage, 0, 0)          # sprite for levels
levelsprite.visible= False

liveimage=pyglet.image.load('media/star.png')           #sprite for lives
live1= pyglet.sprite.Sprite(liveimage, 600, 600)
live1.scale = 0.1
live1.visible=False
live2= pyglet.sprite.Sprite(liveimage, 650, 600)
live2.scale = 0.1
live2.visible=False
live3= pyglet.sprite.Sprite(liveimage, 700, 600)
live3.scale = 0.1
live3.visible=False

player = pyglet.media.Player()
sound = pyglet.media.load('media/back.mp3') #sounds to play
player.queue(sound) 

# keep playing for as long as the app is running (or you tell it to stop):
player.eos_action = pyglet.media.SourceGroup.loop

player.play()
correctsound=pyglet.media.load('media/correctSOUND.wav', streaming = False)
wrongsound=pyglet.media.load('media/wrongSOUND.wav', streaming = False)



#variables
move=False
logo_on = 0
c=0
score = 0
lives =3
t =0
strike =0
q_num =0
level =1
frame =0
answer = ""
l =0
jump = 0
down = 0
obstacleSpeed = 2

#labels
scorelabel = pyglet.text.Label("",
                             font_name='Agency FB',
                             font_size=28,
                             x=20, y=650,
                             anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
levellabel = pyglet.text.Label("",
                             font_name='Agency FB',
                             font_size=48,
                             x=400, y=500,
                             anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
strikelabel = pyglet.text.Label("",
                             font_name='Agency FB',
                             font_size=48,
                             x=400, y=500,
                             anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
question = pyglet.text.Label("",
                             font_name='Agency FB',
                             font_size=18,
                             x=400, y=550, multiline = True, width = 500,
                             anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))


#questions
easy_questions = [" Which of the following will make the girl jump? \n A. If 3 < 2 then jump.\n B. If lion == tiger then jump.\n C. If a square has 4 sides then jump.\n D. If hair == hair then don't jump.\n",
                  "x = 1.0 \n What Data Type is x? \n A. Integer B. Double C. String S. Char ", " How many bits are in a byte? \n A. 4 B. 2. C. 8 D. 12 ", " How many bytes are in a megabyte? \n A. 1000000 B. 100000000 C. 100 D. 1000000000000", "Convert Binary to Decimal: What is 1010 in decimal? \n A. 9 B. 8 C. 10 D. 4", "Convert Binary to Decimal: What is 0001 in decimal? \n A. 0 B. 3 C. 4. D. 1 "   ]
easy_answers = ["c", "b", "c" , "a", "c", "d"]

medium_questions = ["x = 'Hello World'\n print(x) \n The code above would output?\n A. Hello World B. x C. x = 'Hello World' D. 'Hello World'", " x = 5\n if x == 5 \n { \n     print(x)\n }\n else\n{\n     print('x is not 5')\nThe code above would output?\nA. x is not 5 B. nothing C. 5 D. 6", "for(int i = 1; i <= 5; i++) \n{\n     print(i + " ")\n}\nThe code above would output?\nA. i i i i i B. 1 2 3 4 C. 1 2 3 4 5 D. 0 1 2 3 4", "int x = 1 \n while ( x < 6 )\n {\n     print(x + ' ')\n}\nThe code above would output?\nA. i i i i i B. 1 2 3 4 C. 1 2 3 4 5  D. 0 1 2 3 4", "How do you recognise a phishing scam?\n A. Email the sender back and ask if they meant to send the email B. Click on the links in the email and fill out the forms C. Forward the email to everyone D. Look at the sender's email, verify any logos and do not respond to anything within the email"]
medium_answers = ["a", "c", "c", "c", "d", "d"]

hard_questions = ["Which of the folowing is considered a definite indicator of an incident?\n A. Changes to system logs  B. Activities at unexpected times C. Presence of new accounts D. Presence of unfamiliar files", "Which data structure is indexable? \n A. Array B. Graph C. Linked List D. Tree", "What layer is the data link layer in the OSI model?\n A. First B. Second C. Third D. Fourth", "What is a Linked List?\nA. a data structure consisting of a collection of elements (values or variables), each identified by at least one index or key. B. a hierarchical tree structure, with a root value and subtrees of children with a parent node C. an ordered set of data elements, each containing a link to its successor D. a String", "What runtime is the fastest?\nA. O(nlogn) B. O(n) C. O(1) D. O(logn)"]
hard_answers = ["a", "a", "b" "c", "c" ]




        
@mygame.event

def on_draw():                                                                   # draws all the sprites
     
    mygame.clear()
    menusprite.draw()
    instsprite.draw()
    levelsprite.draw()
    avatarsprite.draw()
    backSprite.draw()
    girlSprite.draw()
    live1.draw()
    live2.draw()
    live3.draw()
    obstacleSprite.draw()
    strikelabel.draw()
    question.draw()
    logosprite.draw()
    scorelabel.draw()
    levellabel.draw()
    winsprite.draw()
    loosesprite.draw()

@mygame.event
def on_mouse_release(x, y, button, modifiers):                                    # takes users mouse input
    global frame, lis, lis2, c, b, s, t, angle, cond, b, t, m1, m2, lock, lock2, lock3, ballsprite, g1, g2
    
    
    if menusprite.visible== True :# menu selection
        girlSprite.visible = False
        if button==mouse.LEFT: 
            if (140 <= x <= 340) and (497 <= y <= 562):                         # if play selected
                menusprite.visible= False
                backSprite.visible=True
                girlSprite.visible = True
                live1.visible = True
                live2.visible = True
                live3.visible =True
                scorelabel.text = str(score)
                levellabel.text = "LEVEL" + str(level)
            elif (380 <= x <= 590) and (497 <= y <= 562):                       # if help selected
                instsprite.visible=True
                menusprite.visible= False
            elif (380 <= x <= 590) and (372 <= y <= 442):                       
                levelsprite.visible=True
                menusprite.visible= False
            elif (140 <= x <= 340) and (372 <= y <= 442):                      
                avatarsprite.visible=True
                menusprite.visible= False
            elif (250 <= x <= 465) and (250 <= y <= 320):                        # if quit selected
                mygame.close()
            
    elif menusprite.visible== False and instsprite.visible== True:              # help instructions
        if button==mouse.LEFT:
            if( 661 <= x <= 778) and ( 20 <= y <= 61):                          # if back is pressed
                instsprite.visible=False
                menusprite.visible=True
    elif menusprite.visible== False and levelsprite.visible== True:              # help instructions
        if button==mouse.LEFT:
            if( 661 <= x <= 778) and ( 20 <= y <= 61):                          # if back is pressed
                levelsprite.visible=False
                menusprite.visible=True
    elif menusprite.visible== False and avatarsprite.visible== True:              # help instructions
        if button==mouse.LEFT:
            if( 661 <= x <= 778) and ( 20 <= y <= 61):                          # if back is pressed
                avatarsprite.visible=False
                menusprite.visible=True
            elif( 195 <= x <= 288) and ( 451 <= y <= 585):
                girlSprite.image = girlImage1
            elif( 195 <= x <= 288) and ( 188 <= y <= 321):
                girlSprite.image = girlImage3
            elif( 478 <= x <= 578) and ( 188 <= y <= 321):
                girlSprite.image = girlImage2
            elif( 478 <= x <= 578) and ( 451 <= y <= 585):
                girlSprite.image = girlImage4
    elif menusprite.visible== False  and instsprite.visible==False:             # if back is pressed during game
        if button==mouse.LEFT:
            if frame< 21:
                menusprite.visible= True
    elif loosesprite.visible == True:
        if button==mouse.LEFT:
            if( 614 <= x <= 783) and ( 20 <= y <= 101):                          # if back is pressed
                loosesprite.visible=False
                backSprite.visible=False
                girlSprite.visible = False
                live1.visible = False
                live2.visible = False
                live3.visible =False
                scorelabel.text = ""
                levellabel.text = ""
                menusprite.visible= True
        
                                    
                            
    

@mygame.event

def on_key_release(symbol, modifiers):                                         #takes key input if gamescreen is on only
    
    global c, frame, lives, t, strike, q_num, level, logo_on, logosprite, score, answer, obstacleSprite, jump, obstacleSpeed
    
    if menusprite.visible== False  and instsprite.visible==False :
        if symbol == key.A:
            answer = "a"
        elif symbol == key.B:
            answer = "b"
        elif symbol == key.C:
            answer = "c"
        elif symbol == key.D:
            answer = "d"
        if level == 1:
            
            if answer == easy_answers[q_num]:
                obstacleSpeed = 7
                correctsound.play()
                score+=5
                scorelabel.text = str(score)
                jump =1
                #c=0
                question.text = ""
                q_num+=1                                                  #increment question
            else:
                wrongsound.play()
                
            
        elif level == 2:
            if answer == medium_questions[q_num]:
                obstacleSpeed = 7
                score+=5
                scorelabel.text = str(score)
                #c=0
                #obstacleSprite.x = 800
                question.text = ""
                q_num+=1                                                  #increment question
            else:
                wrongsound.play()
                
                
        elif level == 3:
            if answer == hard_questions[q_num]:
                obstacleSpeed = 7
                score+=5
                scorelabel.text = str[q_num]
                #c=0
                
                question.text = ""
                q_num+=1                                                    #increment question
            else:
                wrongsound.play()
                
                    
            
    
def update(dt):
    
    global c, frame, lives, t, strike, q_num, level, logo_on, logosprite, l, jump, down, move, obstacleSpeed
    
    l+=1
    if l > 20:
        levellabel.text =""
        l =0
    
    logo_on +=1
    if logo_on > 30:
        logosprite.visible= False
        
    backSprite.x -= 400 * dt
    if(backSprite.x <= -600):
        backSprite.x =0

    if jump ==1:
        girlSprite.y+=25
        girlSprite.x+=10
    if girlSprite.y >= 700:
        jump =0
        down =1
    if down == 1:
        girlSprite.y-=25
        girlSprite.x+=5
    if girlSprite.y <=20:
        girlSprite.y =20
        girlSprite.x -=5
        down =0
    if girlSprite.x <=200:
        girlSprite.x = 200
        
    if menusprite.visible== False and instsprite.visible==False and avatarsprite.visible == False:
        
        c+=0.5
        if q_num >= 5:
            q_num =0
            level+=1
            levellabel.text = "Level " + str(level) 
            if level >=4:
                winsprite.visible = True
                level =0
        if(c == 50):                                                     #after 50 frames, obstacle appears
            move = True
            rand = random.randint(0,2)
            if rand == 1:
                obstacleSprite.image = obstacleimage1
            else:
                obstacleSprite.image = obstacleimage2
            obstacleSprite.visible = True
            if level == 1:
                question.text = easy_questions[q_num]                            #question appears
            elif level == 2:
                question.text = medium_questions[q_num]
            elif level == 3:
                question.text = hard_questions[q_num]
            
        if move == True:                                                       # move obstacle
            obstacleSprite.x -= obstacleSpeed
            
                
        if( obstacleSprite.x <= 0):                                       #obstacle goes out of screen
            obstacleSprite.x = 800
            c=0
            obstacleSpeed = 2
            move = False
            
        #hit condition
        if( girlSprite.y+10 <= (obstacleSprite.y + obstacleSprite.height)) and ( obstacleSprite.x <= (girlSprite.x + girlSprite.width//2))and ( obstacleSprite.x >= (girlSprite.x)) :     #girl hit by obstacle
            wrongsound.play()
            obstacleSprite.x = 800
            c=0
            move = False
            q_num+=1
            question.text =""
            t+=1
            lives -=1
            if(lives == 2):
                live1.visible = False
            elif lives == 1:
                live2.visible = False
            
            strike =1
        
        if (lives == 0 and strike ==1):
            live3.visible = False
            loosesprite.visible = True
            lives = 3

        elif (lives > 0 and strike ==1):
            if t < 15:
                strikelabel.text = "STRIKE!"
                t+=1
            else:
                strikelabel.text = ""
                t=0
                strike =0
                
            

    
pyglet.clock.schedule_interval(update, 1/20.)
    
pyglet.app.run()
