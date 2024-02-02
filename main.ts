function start_game() {
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
    basic.showNumber(3)
    basic.pause(400)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
    basic.showNumber(2)
    basic.pause(400)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
    basic.showNumber(1)
    basic.pause(400)
    music.play(music.tonePlayable(523, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    basic.showNumber(0)
    basic.pause(100)
    basic.clearScreen()
    let player_has_ball = 1
}

function end_game() {
    
}

radio.onReceivedString(function on_received_string(receivedString: string) {
    
    if (receivedString == "initialise") {
        linked = true
        radio.sendString("ini_finished")
        player_number = 1
        basic.pause(500)
        for (let index = 0; index < 3; index++) {
            basic.clearScreen()
            basic.pause(200)
            basic.showNumber(1)
            basic.pause(200)
        }
    } else if (receivedString == "ini_finished") {
        linked = true
        player_number = 2
        basic.pause(500)
        for (let index2 = 0; index2 < 3; index2++) {
            basic.clearScreen()
            basic.pause(200)
            basic.showNumber(2)
            basic.pause(200)
        }
        basic.pause(2000)
        radio.sendString("start_game")
        start_game()
        led.plot(4, 2)
        player_has_ball = 1
        is_game_running = true
    } else if (receivedString == "start_game") {
        start_game()
        led.plot(0, 2)
        ball_direction = [1, randint(0, 2)]
        is_game_running = true
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (is_game_running) {
        if (player_number == 1) {
            led.unplot(0, player_1_pos)
            if (player_1_pos > 0) {
                player_1_pos += -1
            }
            
            led.plot(0, player_1_pos)
        } else if (player_number == 2) {
            led.unplot(4, player_2_pos)
            if (player_2_pos > 0) {
                player_2_pos += -1
            }
            
            led.plot(4, player_2_pos)
        }
        
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (is_game_running) {
        if (player_number == 1) {
            led.unplot(0, player_1_pos)
            if (player_1_pos < 4) {
                player_1_pos += 1
            }
            
            led.plot(0, player_1_pos)
        } else if (player_number == 2) {
            led.unplot(4, player_2_pos)
            if (player_2_pos < 4) {
                player_2_pos += 1
            }
            
            led.plot(4, player_2_pos)
        }
        
    }
    
})
let player_number = 0
let player_has_ball = 1
let player_2_pos = 2
let player_1_pos = 2
let ball_pos = [2, 2]
let ball_direction = [1, randint(0, 1)]
let is_game_running = false
let linked = false
music.setBuiltInSpeakerEnabled(true)
basic.showIcon(IconNames.Heart)
music.play(music.stringPlayable("A G A F - - - - ", 120), music.PlaybackMode.UntilDone)
basic.clearScreen()
basic.showString("Pong")
radio.setGroup(64)
while (!linked) {
    radio.sendString("initialise")
    for (let index3 = 0; index3 < 5; index3++) {
        if (!linked) {
            basic.showLeds(`
                # . # # .
                . # . # #
                . . # # .
                . # . # #
                # . # # .
                `)
            basic.pause(500)
            basic.clearScreen()
            basic.pause(500)
        }
        
    }
}
basic.forever(function on_forever() {
    
    if (is_game_running) {
        basic.pause(500)
        if (player_has_ball == player_number) {
            led.unplot(ball_pos[0], ball_pos[1])
        }
        
        if (ball_direction[1] == 0) {
            if (ball_pos[1] == 0) {
                ball_pos[1] += 1
                ball_direction[1] = 1
            } else {
                ball_pos[1] -= 1
            }
            
        } else if (ball_direction[1] == 1) {
            if (ball_pos[1] == 4) {
                ball_pos[1] -= 1
                ball_direction[1] = 0
            } else {
                ball_pos[1] += 1
            }
            
        }
        
        if (player_has_ball == player_number) {
            led.plot(ball_pos[0], ball_pos[1])
        }
        
    }
    
})
