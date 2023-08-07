print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.RGB import RGB
from midi import Midi


# KEYTBOARD SETUP
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules = [layers, encoders, tapdance]

# SWITCH MATRIX
keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS
encoders.pins = ((board.A2, board.A1, board.A0, False), (board.SCK, board.MISO, board.MOSI, False),)

# EXTENSIONS
rgb_ext = RGB(pixel_pin = board.D10, num_pixels=4, hue_default=100)
midi_ext = Midi()
keyboard.extensions.append(rgb_ext)
keyboard.extensions.append(midi_ext)
keyboard.debug_enabled = False

# MACROS ROW 1
# I left it that way as I didn't know exactly what to assign to the 12 keys. You can shortcut this part as you want.
# In the music function, enter your own youtube playlist link in the send string part
#

MUSIC = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string(''), KC.ENTER])
SPOTIFY = simple_key_sequence([KC.LCMD(KC.SPACE), send_string('spotify'), KC.ENTER ,KC.MACRO_SLEEP_MS(1000), KC.SPACE])
WHATSAPP = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('https://web.whatsapp.com'), KC.ENTER])
COPY = simple_key_sequence([KC.LCMD(KC.C)])
PASTE = simple_key_sequence([KC.LCMD(KC.V),KC.MACRO_SLEEP_MS(500)])
UNDO = simple_key_sequence([KC.LCMD(KC.Z),KC.MACRO_SLEEP_MS(1000)])
FORMAT_CODE = simple_key_sequence([KC.LCMD(KC.LSFT(KC.LALT(KC.F))),KC.MACRO_SLEEP_MS(1000)])
PRIVATE_BROWSING = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N)),KC.MACRO_SLEEP_MS(1000)])




#In this part, I wrote to check if there is an error in my resistor soldering.
#If you are going to use and do this, I recommend that you touch the two conductors to the part where the switches are at least once and check before soldering the switches. Thanks to this, I realized that there was a mistake in the 10th part, I took it out and soldered it again with another resistor.


BIR = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('1'), KC.ENTER])
IKI = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('2'), KC.ENTER])
UC = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('3'), KC.ENTER])
DORT = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('4'), KC.ENTER])
BES = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('5'), KC.ENTER])
ALTI = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('6'), KC.ENTER])
YEDI = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('7'), KC.ENTER])
SEKIZ = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('8'), KC.ENTER])
DOKUZ = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('9'), KC.ENTER])
ON = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), KC.MACRO_SLEEP_MS(1000), send_string('10'), KC.ENTER])
ONBIR = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('11'), KC.ENTER])
ONIKI = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('12'), KC.ENTER])






_______ = KC.TRNS
xxxxxxx = KC.NO

# LAYER SWITCHING TAP DANCE
# TD_LYRS = KC.TD(LOCK, KC.MO(1), xxxxxxx, KC.TO(2))
MIDI_OUT = KC.TD(KC.MIDI(70), xxxxxxx, xxxxxxx, KC.TO(0))

# array of default MIDI notes
# midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

# KEYMAPS

keyboard.keymap = [
    # MACROS
    [
        MUSIC ,       SPOTIFY,            WHATSAPP,             COPY,
        PASTE,        UNDO,           FORMAT_CODE,           PRIVATE_BROWSING,
         DOKUZ,    ON,       ONBIR,     ONIKI,
    ],
    # RGB CTL
    [
        xxxxxxx,    xxxxxxx,            xxxxxxx,                xxxxxxx,
        xxxxxxx,    KC.RGB_MODE_SWIRL,  KC.RGB_MODE_KNIGHT,     KC.RGB_MODE_BREATHE_RAINBOW,
        xxxxxxx,    KC.RGB_MODE_PLAIN,  KC.RGB_MODE_BREATHE,    KC.RGB_MODE_RAINBOW,
    ],
    # MIDI
    [
        KC.MIDI(30),    KC.MIDI(69),      KC.MIDI(70),       MIDI_OUT,
        KC.MIDI(67),    KC.MIDI(66),      KC.MIDI(65),       KC.MIDI(64),
        KC.MIDI(60),    KC.MIDI(61),      KC.MIDI(62),       KC.MIDI(63),  
    ]
]
#In this part, the right encoder does not work very well, instead of advancing the song, it directly passes the song, so you can code what you want in that part. I'll fix that part in my library in my spare time, but I don't know when I'll get it done and enter it as an update.

encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),         (KC.MRWD, KC.MFFD, KC.MUTE) ), #(KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MACROS
                    ((KC.RGB_AND, KC.RGB_ANI, xxxxxxx),  (KC.RGB_AND, KC.RGB_ANI, xxxxxxx)),   #(KC.RGB_HUD,    KC.RGB_HUI,     _______   )),   # RGB CTL
                    ((KC.VOLD, KC.VOLU, KC.MUTE),    (KC.MRWD, KC.MFFD, KC.MUTE))       #(KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MIDI
                ]


if __name__ == '__main__':
    keyboard.go()
    
