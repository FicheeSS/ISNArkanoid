WCASE = 15
HCASE = 10
GCASE = 2
NBRICKSX = 19
NBRICKSY = 14

SCREENSIZE = (int((NBRICKSX*WCASE)+((NBRICKSX+1)*GCASE)),int(((NBRICKSY*HCASE)+((NBRICKSY+1)*GCASE))*3))
effectiveSize = (SCREENSIZE[0],SCREENSIZE[1]+20)
BALLSIZE = 15

NOWALL = 0
TOPWALL = 1
BOTTOMWALL = 2
LEFTWALL = 3
RIGHTWALL = 4

RADIUS = 7
BALLPLACE =SCREENSIZE[0] -(NBRICKSX*(WCASE+GCASE)) 
STDEXEC = 1000
PALETTEHEIGHT = 10 
PALETTEWIDTH = 55

BRICKSIZE = (WCASE,HCASE)

VICTORY = 1
DEFEAT = 2
INLEVEL = 3
l_KEY = 1
r_KEY = 2

BACKGROUNDMUSICLOC = "./music/main.ogg"
BOUNCESOUNDLOC = "./music/bounce.ogg"
