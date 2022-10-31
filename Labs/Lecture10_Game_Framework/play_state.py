from pico2d import *
import item_state
import logo_state
import game_framework
import title_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1 #오른쪽
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x  =0
            self.dir = 1


    def draw(self):
        if self.item == 'Ball':
            self.ball_image.draw(self.x+10, self.y+50)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x+10, self.y+50)
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
    delay(0.01)


boy = None #굳이 c로 따지면 NULL
grass = None
running = True

#초기화
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

# finalization code
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass