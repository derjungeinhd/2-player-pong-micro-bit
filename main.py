def start_game():
    global player_number, player_1_pos, player_2_pos, player_has_ball, is_game_running, ball_direction
    music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_number(3)
    basic.pause(400)
    music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_number(2)
    basic.pause(400)
    music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_number(1)
    basic.pause(400)
    music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_number(0)
    basic.pause(100)
    basic.clear_screen()
    player_has_ball = 1
    if player_number == 1:
        player_1_pos = 2
        led.plot(0, 2)
        ball_direction = [1, randint(0, 2)]
    elif player_number == 2:
        player_2_pos = 2
        led.plot(4, 2)
    is_game_running = True


def end_game():
    pass

def on_received_string(receivedString):
    global linked, player_number, player_has_ball, is_game_running, ball_direction, ball_pos
    if receivedString == "initialise":
        linked = True
        radio.send_string("ini_finished")
        player_number = 1
        basic.pause(500)
        for index in range(3):
            basic.clear_screen()
            basic.pause(200)
            basic.show_number(1)
            basic.pause(200)
    elif receivedString == "ini_finished":
        linked = True
        player_number = 2
        basic.pause(500)
        for index2 in range(3):
            basic.clear_screen()
            basic.pause(200)
            basic.show_number(2)
            basic.pause(200)
        basic.pause(2000)
        radio.send_string("start_game")
        start_game()
    elif receivedString == "start_game":
        start_game()
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    if name == "switch2P1":

    elif name == "switch2P2":

radio.on_received_value(on_received_value)

def on_button_pressed_a():
    global player_1_pos, player_2_pos
    if is_game_running:
        if player_number == 1:
            led.unplot(0, player_1_pos)
            if player_1_pos > 0:
                player_1_pos += -1
            led.plot(0, player_1_pos)
        elif player_number == 2:
            led.unplot(4, player_2_pos)
            if player_2_pos > 0:
                player_2_pos += -1
            led.plot(4, player_2_pos)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global player_1_pos, player_2_pos
    if is_game_running:
        if player_number == 1:
            led.unplot(0, player_1_pos)
            if player_1_pos < 4:
                player_1_pos += 1
            led.plot(0, player_1_pos)
        elif player_number == 2:
            led.unplot(4, player_2_pos)
            if player_2_pos < 4:
                player_2_pos += 1
            led.plot(4, player_2_pos)
input.on_button_pressed(Button.B, on_button_pressed_b)

player_number = 0
player_has_ball = 1
player_2_pos = 2
player_1_pos = 2
ball_pos = [2, 2]
ball_direction = [1, randint(0, 1)]
is_game_running = False
linked = False

music.set_built_in_speaker_enabled(True)
basic.show_icon(IconNames.HEART)
music.play(music.string_playable("A G A F - - - - ", 120),
    music.PlaybackMode.UNTIL_DONE)
basic.clear_screen()
basic.show_string("Pong")
radio.set_group(64)

while not (linked):
    radio.send_string("initialise")
    for index3 in range(5):
        if not (linked):
            basic.show_leds("""
                # . # # .
                . # . # #
                . . # # .
                . # . # #
                # . # # .
                """)
            basic.pause(500)
            basic.clear_screen()
            basic.pause(500)

def on_forever():
    global ball_pos, ball_direction, player_has_ball, player_number, is_game_running, player_1_pos, player_2_pos
    if is_game_running:
        basic.pause(500)
        if player_has_ball == player_number:
            led.unplot(ball_pos[0], ball_pos[1])
        
        if ball_direction[1] == 0:
            if ball_pos[1] == 0:
                ball_pos[1] += 1
                ball_direction[1] = 1
            else:
                ball_pos[1] -= 1
        elif ball_direction[1] == 1:
            if ball_pos[1] == 4:
                ball_pos[1] -= 1
                ball_direction[1] = 0
            else:
                ball_pos[1] += 1
        
        if ball_direction[0] == 0:
            if ball_pos[0] == 0:
                if player_number == 1:
                    if ball_pos[1] == player_1_pos:
                        ball_pos[0] += 1
                        ball_direction[0] = 1
                    else:
                        is_game_running
                        end_game()

                elif player_number == 2:
                    radio.send_value("switch2P1", ball_pos[1])
                    player_has_ball == 1
        elif ball_direction[0] == 1:
        
        if player_has_ball == player_number:
            led.plot(ball_pos[0], ball_pos[1])
basic.forever(on_forever)