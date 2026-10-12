"""Gera artes originais pixeladas e GIFs ILUSTRATIVOS de movimento.

Opcional para quem quiser redesenhar os assets: pip install Pillow.
As animações são esquemáticas e NÃO substituem demonstrações reais.
"""
from pathlib import Path
from math import sin, pi
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent.parent / 'public' / 'assets'
IMAGES, GIFS = BASE / 'images', BASE / 'gifs'
IMAGES.mkdir(parents=True, exist_ok=True)
GIFS.mkdir(parents=True, exist_ok=True)
C = dict(bg='#10233e', grid='#1a3558', cyan='#60d1fb', blue='#367fbd', blue2='#25629b',
         lilac='#a2a5f6', skin='#f6ba8f', shade='#d28b70', hair='#17243e', white='#eaf6ff',
         pink='#f1a2c1', yellow='#ffdc8c', shoe='#e6f6ff', metal='#6d8cb4', grass='#5bd6bd')


def fnt(sz=11):
    for path in ['/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',
                 '/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf']:
        if Path(path).exists():
            return ImageFont.truetype(path, sz)
    return ImageFont.load_default()


def backdrop(w=240, h=154, mode=0):
    im = Image.new('RGB',(w,h),C['bg']); d=ImageDraw.Draw(im)
    for yy in range(0,h,16):
        for xx in range(0,w,16):
            d.rectangle((xx+1, yy+1, xx+1, yy+1), fill=C['grid'])
    d.rectangle((0,h-19,w,h),fill='#0c1930'); d.line((10,h-26,w-10,h-26),fill='#42709a',width=2)
    d.rectangle((7,8,11,12),fill=C['cyan']);d.rectangle((w-14,8,w-10,12),fill=C['cyan'])
    d.text((17,7),'BLUE REP // MOTION',font=fnt(9),fill=C['cyan'])
    d.text((w-60,h-15),'8-BIT GYM',font=fnt(8),fill='#6786ac')
    return im


def joint(d, a, b, color, width=7):
    d.line((int(a[0]),int(a[1]),int(b[0]),int(b[1])),fill='#0c1b31',width=width+3)
    d.line((int(a[0]),int(a[1]),int(b[0]),int(b[1])),fill=color,width=width)


def circle(d,x,y,r,color, outline='#122037'):
    d.ellipse((int(x-r),int(y-r),int(x+r),int(y+r)),fill=color,outline=outline,width=2)


def person_front(d, mode, t, x=126, y=49, scale=1):
    bob = sin(2*pi*t)
    # y: head center; hips head+65. Arms customized below.
    if mode in ('squat','sumo'):
        y += int((1-bob)*9)
    if mode == 'calf':
        y -= int((bob+1)*4)
    circle(d,x,y,10,C['skin'])
    d.pieslice((x-11,y-12,x+11,y+7),180,360,fill=C['hair'])
    d.rectangle((x-12,y-5,x-9,y+8),fill=C['hair'])
    d.rectangle((x-3,y+10,x+3,y+17),fill=C['shade'])
    shoulders=(x-17,y+22),(x+17,y+22)
    d.polygon([(x-17,y+20),(x+17,y+20),(x+13,y+62),(x-13,y+62)], fill=C['blue'],outline='#0b1c34',width=2)
    d.polygon([(x-13,y+61),(x+13,y+61),(x+16,y+72),(x-16,y+72)],fill=C['lilac'])
    hip=y+70
    if mode in ('squat','sumo'):
        open_=27 if mode=='sumo' else 18
        joint(d,(x-11,hip),(x-open_,hip+19),C['skin'],9)
        joint(d,(x+11,hip),(x+open_,hip+19),C['skin'],9)
        joint(d,(x-open_,hip+19),(x-open_-4,137),C['blue2'],8)
        joint(d,(x+open_,hip+19),(x+open_+4,137),C['blue2'],8)
        d.rectangle((x-open_-10,135,x-open_+2,141),fill=C['shoe'])
        d.rectangle((x+open_-1,135,x+open_+12,141),fill=C['shoe'])
    else:
        joint(d,(x-10,hip),(x-13,hip+27),C['skin'],9);joint(d,(x+10,hip),(x+13,hip+27),C['skin'],9)
        joint(d,(x-13,hip+27),(x-15,138),C['blue2'],8);joint(d,(x+13,hip+27),(x+15,138),C['blue2'],8)
        d.rectangle((x-20,136,x-9,142),fill=C['shoe']);d.rectangle((x+11,136,x+24,142),fill=C['shoe'])
    # Arms positioning by movement type.
    if mode in ('squat','sumo'):
        joint(d,shoulders[0],(x-21,y+43),C['skin']);joint(d,(x-21,y+43),(x-7,y+45),C['skin'])
        joint(d,shoulders[1],(x+21,y+43),C['skin']);joint(d,(x+21,y+43),(x+7,y+45),C['skin'])
        if mode=='squat': d.rectangle((x-8,y+40,x+8,y+51),fill=C['metal'],outline='#071b34',width=2)
        else: d.rectangle((x-6,y+51,x+6,y+68),fill=C['metal'],outline='#071b34',width=2)
    elif mode=='pull':
        high = int(8+26*(t+1)/2)
        d.line((x-49,20,x+49,20),fill=C['metal'],width=5)
        for sign in (-1,1):
            shoulder=(x+sign*17,y+22)
            elbow=(x+sign*35,y+5+high)
            hand=(x+sign*47,22+high)
            joint(d,shoulder,elbow,C['skin'],6);joint(d,elbow,hand,C['skin'],6)
        d.line((x-49,20+high,x+49,20+high),fill=C['cyan'],width=4)
    elif mode in ('triceps','pulldown'):
        for sign in (-1,1):
            elbow=(x+sign*22,y+41)
            hand=(x+sign*22,y+45+int(18*(1+t)/2))
            if mode=='pulldown': elbow=(x+sign*31,y+22);hand=(x+sign*34,y+36+int(30*(t+1)/2))
            joint(d,(x+sign*17,y+22),elbow,C['skin'],7);joint(d,elbow,hand,C['skin'],7)
        d.line((x-41,y+60+int(18*(1+t)/2),x+41,y+60+int(18*(1+t)/2)),fill=C['metal'],width=3)
    elif mode == 'overhead':
        hand_y=y-15+int(18*(1+t)/2)
        for sign in (-1,1):
            joint(d,(x+sign*17,y+22),(x+sign*13,y+1),C['skin'],6)
            joint(d,(x+sign*13,y+1),(x+sign*7,hand_y),C['skin'],6)
        d.rectangle((x-12,hand_y-6,x+12,hand_y),fill=C['metal'],outline='#112037',width=2)
    elif mode == 'biceps':
        for sign in (-1,1):
            elbow=(x+sign*19,y+49)
            hand=(x+sign*16,y+67-int(25*(t+1)/2))
            joint(d,(x+sign*17,y+22),elbow,C['skin'],6)
            joint(d,elbow,hand,C['skin'],6)
            d.rectangle((hand[0]-7,hand[1]-3,hand[0]+7,hand[1]+3),fill=C['metal'])
    elif mode == 'lateral':
        lift=(t+1)/2
        for sign in (-1,1):
            elbow=(x+sign*(21+18*lift),y+41-29*lift)
            hand=(x+sign*(29+34*lift),y+57-48*lift)
            joint(d,(x+sign*17,y+22),elbow,C['skin'],6);joint(d,elbow,hand,C['skin'],6)
            d.rectangle((hand[0]-6,hand[1]-4,hand[0]+6,hand[1]+4),fill=C['metal'])
    elif mode == 'fly':
        lift=(t+1)/2
        for sign in (-1,1):
            elbow=(x+sign*(32-9*lift),y+34+8*lift)
            hand=(x+sign*(58-43*lift),y+44+2*lift)
            joint(d,(x+sign*17,y+22),elbow,C['skin'],6);joint(d,elbow,hand,C['skin'],6)
        d.line((x-70,20,x-70,125),fill=C['metal'],width=4);d.line((x+70,20,x+70,125),fill=C['metal'],width=4)
    else:
        for sign in (-1,1):
            joint(d,(x+sign*17,y+22),(x+sign*24,y+55),C['skin'],7)


def side_pose(d, mode, t):
    move=(1+sin(t*2*pi))/2
    x=110;y=46
    if mode=='rdl':
        # Hip hinge: torso inclines without rounding the spine.
        hip=(111,101)
        head=(112+int(24*move),45+int(23*move))
        shoulder=(112+int(21*move),67+int(14*move))
        joint(d,hip,shoulder,C['blue'],21);circle(d,*head,10,C['skin']);d.rectangle((head[0]-10,head[1]-12,head[0]+9,head[1]-7),fill=C['hair'])
        joint(d,(109,105),(111,120),C['skin'],10);joint(d,(111,120),(116,139),C['blue2'],8)
        joint(d,(124,105),(124,121),C['skin'],10);joint(d,(124,121),(130,139),C['blue2'],8)
        joint(d,shoulder,(shoulder[0]+3,shoulder[1]+23),C['skin'],8)
        wrist=(shoulder[0]+3,shoulder[1]+39)
        joint(d,(shoulder[0]+3,shoulder[1]+23),wrist,C['skin'],7)
        d.rectangle((wrist[0]-13,wrist[1]-5,wrist[0]+13,wrist[1]+5),fill=C['metal'])
        d.rectangle((103,137,123,144),fill=C['shoe']);d.rectangle((121,137,140,144),fill=C['shoe'])
    elif mode in ('legpress','extensora','flexora','row'):
        d.rectangle((58,91,102,98),fill=C['metal']);d.rectangle((63,99,70,132),fill=C['metal'])
        circle(d,91,63,11,C['skin']);d.rectangle((82,50,99,55),fill=C['hair']);joint(d,(91,76),(91,94),C['blue'],17)
        if mode=='row':
            k=(97,108);ankle=(105,141)
            joint(d,(91,94),k,C['skin'],9);joint(d,k,ankle,C['blue2'],8)
            j=(110,88);hand=(123+int(28*move),89)
            joint(d,(94,82),j,C['skin'],7);joint(d,j,hand,C['skin'],7)
            d.line((180,25,180,132),fill=C['metal'],width=5);d.line((hand[0],hand[1],180,hand[1]),fill=C['cyan'],width=2)
        elif mode=='legpress':
            knee=(131-int(15*move),98+int(8*move));foot=(172-int(20*move),75+int(20*move))
            joint(d,(91,94),knee,C['skin'],10);joint(d,knee,foot,C['blue2'],9)
            d.line((foot[0]+9,foot[1]-22,foot[0]+9,foot[1]+32),fill=C['cyan'],width=8)
            d.line((135,137,204,34),fill=C['metal'],width=3)
        else:
            knee=(129,106);ankle=(132+int((25 if mode=='extensora' else -19)*move),132-int(21*move))
            joint(d,(91,94),knee,C['skin'],10);joint(d,knee,ankle,C['blue2'],8)
            circle(d,ankle[0]+5,ankle[1],7,C['metal'])
    elif mode in ('bench','hipthrust'):
        d.rectangle((44,97,168,105),fill=C['metal']);d.rectangle((54,105,61,132),fill=C['metal']);d.rectangle((152,105,159,132),fill=C['metal'])
        if mode=='bench':
            head=(70,78);circle(d,*head,10,C['skin']);d.rectangle((61,66,78,69),fill=C['hair'])
            joint(d,(80,82),(131,82),C['blue'],18)
            joint(d,(130,87),(148,108),C['skin'],8);joint(d,(148,108),(151,139),C['blue2'],7)
            h=68-int(23*move)
            joint(d,(98,79),(99,h),C['skin'],7);joint(d,(119,79),(120,h),C['skin'],7)
            d.rectangle((89,h-4,108,h+4),fill=C['metal']);d.rectangle((111,h-4,130,h+4),fill=C['metal'])
        else:
            height=int(20*move)
            circle(d,74,76-height//2,11,C['skin']);d.rectangle((64,64-height//2,82,67-height//2),fill=C['hair'])
            joint(d,(85,82-height//2),(128,95-height),C['blue'],19)
            joint(d,(128,95-height),(155,93),C['skin'],9);joint(d,(155,93),(164,139),C['blue2'],8)
            d.rectangle((119,85-height,138,94-height),fill=C['metal'])
    else: person_front(d,'squat',t)


def animation(name, mode):
    frames=[]
    for i in range(12):
        t=sin(2*pi*i/12)
        image=backdrop()
        d=ImageDraw.Draw(image)
        # Indoor apparatus and floor line for context.
        if mode in ('pull','pulldown','triceps'):
            d.line((48,27,48,124),fill='#507da4',width=4);d.rectangle((40,23,57,34),fill=C['metal'])
        if mode in ('squat','sumo','calf','pull','pulldown','triceps','overhead','biceps','lateral','fly'):
            person_front(d,mode,t)
        else:
            side_pose(d,mode,i/12)
        # Direction arrows show the action is animated rather than an exact technique video.
        d.text((10,128),'REPETICAO',font=fnt(8),fill='#82bfdf')
        d.rectangle((85,131,85+int(i/11*79),135),fill=C['cyan'])
        frames.append(image.resize((480,308),Image.Resampling.NEAREST).quantize(colors=40))
    frames[0].save(GIFS/f'{name}.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True,disposal=2)


def pixel_rect(d, x,y,w,h,fill):
    d.rectangle((x,y,x+w,y+h),fill=fill)


def avatar(d, ox=85, oy=23, scale=1, pose='A'):
    # Personagem desenhada em blocos; o formato é propositadamente pixelado.
    px=lambda x:ox+x*scale
    py=lambda y:oy+y*scale
    def block(x,y,w,h,clr):pixel_rect(d,px(x),py(y),w*scale,h*scale,clr)
    # Hair and head.
    block(27,1,27,6,C['hair']);block(21,7,39,9,C['hair']);block(19,16,45,18,C['hair'])
    block(24,15,31,27,C['skin']);block(27,37,26,7,C['shade']);block(34,23,4,3,C['hair']);block(48,23,4,3,C['hair']);block(37,32,11,2,C['shade'])
    block(19,26,8,35,C['hair']);block(57,26,8,40,C['hair']);block(34,44,13,8,C['skin'])
    # Top and shorts.
    block(15,49,55,43,C['cyan']);block(18,49,49,6,C['white']);block(25,85,36,19,C['lilac']);block(16,82,54,7,C['blue2'])
    # Arm, shoes, legs.
    if pose=='B':
        block(6,13,9,45,C['skin']);block(6,10,14,10,C['skin']);block(69,14,9,44,C['skin']);block(66,10,13,9,C['skin'])
        block(1,5,82,5,C['metal'])
    elif pose=='C':
        block(6,49,10,43,C['skin']);block(65,49,10,43,C['skin']);block(2,84,17,10,C['metal']);block(64,84,17,10,C['metal'])
    else:
        block(4,57,12,41,C['skin']);block(68,57,12,41,C['skin']);block(4,93,22,11,C['metal']);block(62,93,22,11,C['metal'])
    block(26,104,17,37,C['skin']);block(45,104,17,37,C['skin']);block(26,133,17,21,C['blue2']);block(45,133,17,21,C['blue2'])
    block(18,151,28,9,C['white']);block(44,151,28,9,C['white']);block(17,156,30,5,C['hair']);block(43,156,30,5,C['hair'])


def card(name,pose,main,accent):
    im=Image.new('RGB',(200,142),main);d=ImageDraw.Draw(im)
    for yy in range(0,142,11):
        for xx in range(0,200,11):
            d.point((xx,yy),fill=accent)
    d.ellipse((55,-27,196,115),outline=accent,width=5)
    d.rectangle((6,5,71,18),fill='#10243e');d.text((12,7),'PLAYER 01',fill=C['cyan'],font=fnt(9))
    d.rectangle((0,129,200,142),fill='#0b1d36')
    avatar(d,56,10,.72,pose)
    d.rectangle((9,115,53,120),fill=C['cyan']);d.rectangle((9,122,41,124),fill=C['white'])
    d.rectangle((157,27,189,32),fill=C['yellow']);d.rectangle((169,38,189,42),fill=C['yellow'])
    im.resize((800,568),Image.Resampling.NEAREST).save(IMAGES/f'treino-{name}.png',optimize=True)


def hero():
    im=Image.new('RGBA',(170,195),(0,0,0,0));d=ImageDraw.Draw(im)
    d.ellipse((17,10,165,158),fill='#143d64',outline='#286d9d',width=3)
    d.rectangle((18,168,153,174),fill='#1a5a7b');d.rectangle((24,174,146,178),fill='#0c3151')
    avatar(d,46,1,1.2,'A')
    d.rectangle((19,58,25,64),fill=C['yellow']);d.rectangle((13,64,19,70),fill=C['yellow'])
    d.rectangle((145,92,151,98),fill=C['cyan']);d.rectangle((151,98,157,104),fill=C['cyan'])
    im.resize((680,780),Image.Resampling.NEAREST).save(IMAGES/'hero-athlete.png',optimize=True)


if __name__=='__main__':
    hero()
    card('a','A','#1b4b72','#387ba1')
    card('b','B','#323967','#555b8c')
    card('c','C','#16526b','#317b86')
    modes={
        'goblet':'squat','leg-press':'legpress','hip-thrust':'hipthrust','extensora':'extensora','panturrilha':'calf',
        'puxada':'pull','remada':'row','pulldown':'pulldown','triceps-corda':'triceps','triceps-frances':'overhead','sumo':'sumo',
        'stiff':'rdl','flexora':'flexora','supino':'bench','crucifixo':'fly','rosca':'biceps','lateral':'lateral',
    }
    for name,mode in modes.items():
        animation(name,mode)
        print('GIF:',name)
