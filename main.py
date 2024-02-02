def start_game():
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

def end_game():
    pass

def on_received_string(receivedString):
    global linked, player_number, player_has_ball, is_game_running, ball_direction
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
        led.plot(4, 2)
        player_has_ball = 1
        is_game_running = True
    elif receivedString == "start_game":
        start_game()
        led.plot(0, 2)
        player_has_ball = 1
        ball_direction = [1, randint(0, 2)]
        is_game_running = True
radio.on_received_string(on_received_string)

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
ball_direction = [1, randint(0, 2)]
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
    if is_game_running:
        basic.pause(500)
        if player_has_ball == player_number:
            led.unplot(ball_x, ball_y)
        if player_has_ball == player_number:
            led.plot(ball_x, ball_y)
basic.forever(on_forever)

