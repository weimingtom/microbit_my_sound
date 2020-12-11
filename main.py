def on_sound_loud():
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(100)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_forever():
    if input.button_is_pressed(Button.A):
        music.start_melody(music.built_in_melody(Melodies.BIRTHDAY), MelodyOptions.ONCE)
basic.forever(on_forever)
