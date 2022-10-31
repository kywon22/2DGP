import pico2d
import play_state
import logo_state

pico2d.open_canvas()

states = [logo_state, play_state]#모듈을 변수로 저장
for state in states:
    state.enter() #초기화
#게임루프
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        state.delay(0.05)
    state.exit() #종료

pico2d.close_canvas()