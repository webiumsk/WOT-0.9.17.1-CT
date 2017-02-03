# 2017.02.03 21:46:35 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/Keys.py
"""
This module contains definitions of all keycodes known to the client.
They are set to the values as in the C++ files.
"""
MODIFIER_SHIFT = 1
MODIFIER_CTRL = 2
MODIFIER_ALT = 4
KEY_NOT_FOUND = 0
KEY_NONE = 0
KEY_NULL = 0
KEY_ESCAPE = 1
KEY_1 = 2
KEY_2 = 3
KEY_3 = 4
KEY_4 = 5
KEY_5 = 6
KEY_6 = 7
KEY_7 = 8
KEY_8 = 9
KEY_9 = 10
KEY_0 = 11
KEY_MINUS = 12
KEY_EQUALS = 13
KEY_BACKSPACE = 14
KEY_TAB = 15
KEY_Q = 16
KEY_W = 17
KEY_E = 18
KEY_R = 19
KEY_T = 20
KEY_Y = 21
KEY_U = 22
KEY_I = 23
KEY_O = 24
KEY_P = 25
KEY_LBRACKET = 26
KEY_RBRACKET = 27
KEY_RETURN = 28
KEY_LCONTROL = 29
KEY_A = 30
KEY_S = 31
KEY_D = 32
KEY_F = 33
KEY_G = 34
KEY_H = 35
KEY_J = 36
KEY_K = 37
KEY_L = 38
KEY_SEMICOLON = 39
KEY_APOSTROPHE = 40
KEY_GRAVE = 41
KEY_LSHIFT = 42
KEY_BACKSLASH = 43
KEY_Z = 44
KEY_X = 45
KEY_C = 46
KEY_V = 47
KEY_B = 48
KEY_N = 49
KEY_M = 50
KEY_COMMA = 51
KEY_PERIOD = 52
KEY_SLASH = 53
KEY_RSHIFT = 54
KEY_NUMPADSTAR = 55
KEY_LALT = 56
KEY_SPACE = 57
KEY_CAPSLOCK = 58
KEY_F1 = 59
KEY_F2 = 60
KEY_F3 = 61
KEY_F4 = 62
KEY_F5 = 63
KEY_F6 = 64
KEY_F7 = 65
KEY_F8 = 66
KEY_F9 = 67
KEY_F10 = 68
KEY_NUMLOCK = 69
KEY_SCROLL = 70
KEY_NUMPAD7 = 71
KEY_NUMPAD8 = 72
KEY_NUMPAD9 = 73
KEY_NUMPADMINUS = 74
KEY_NUMPAD4 = 75
KEY_NUMPAD5 = 76
KEY_NUMPAD6 = 77
KEY_ADD = 78
KEY_NUMPAD1 = 79
KEY_NUMPAD2 = 80
KEY_NUMPAD3 = 81
KEY_NUMPAD0 = 82
KEY_NUMPADPERIOD = 83
KEY_OEM_102 = 86
KEY_F11 = 87
KEY_F12 = 88
KEY_F13 = 100
KEY_F14 = 101
KEY_F15 = 102
KEY_KANA = 112
KEY_ABNT_C1 = 115
KEY_CONVERT = 121
KEY_NOCONVERT = 123
KEY_YEN = 125
KEY_ABNT_C2 = 126
KEY_NUMPADEQUALS = 141
KEY_PREVTRACK = 144
KEY_AT = 145
KEY_COLON = 146
KEY_UNDERLINE = 147
KEY_KANJI = 148
KEY_STOP = 149
KEY_AX = 150
KEY_UNLABELED = 151
KEY_NEXTTRACK = 153
KEY_NUMPADENTER = 156
KEY_RCONTROL = 157
KEY_MUTE = 160
KEY_CALCULATOR = 161
KEY_PLAYPAUSE = 162
KEY_MEDIASTOP = 164
KEY_VOLUMEDOWN = 174
KEY_VOLUMEUP = 176
KEY_WEBHOME = 178
KEY_NUMPADCOMMA = 179
KEY_NUMPADSLASH = 181
KEY_SYSRQ = 183
KEY_RALT = 184
KEY_PAUSE = 197
KEY_HOME = 199
KEY_UPARROW = 200
KEY_PGUP = 201
KEY_LEFTARROW = 203
KEY_RIGHTARROW = 205
KEY_END = 207
KEY_DOWNARROW = 208
KEY_PGDN = 209
KEY_INSERT = 210
KEY_DELETE = 211
KEY_LWIN = 219
KEY_RWIN = 220
KEY_APPS = 221
KEY_POWER = 222
KEY_SLEEP = 223
KEY_WAKE = 227
KEY_WEBSEARCH = 229
KEY_WEBFAVORITES = 230
KEY_WEBREFRESH = 231
KEY_WEBSTOP = 232
KEY_WEBFORWARD = 233
KEY_WEBBACK = 234
KEY_MYCOMPUTER = 235
KEY_MAIL = 236
KEY_MEDIASELECT = 237
KEY_IME_CHAR = 255
KEY_MOUSE0 = 256
KEY_LEFTMOUSE = 256
KEY_MOUSE1 = 257
KEY_RIGHTMOUSE = 257
KEY_MOUSE2 = 258
KEY_MIDDLEMOUSE = 258
KEY_MOUSE3 = 259
KEY_MOUSE4 = 260
KEY_MOUSE5 = 261
KEY_MOUSE6 = 262
KEY_MOUSE7 = 263
KEY_JOY0 = 272
KEY_JOY1 = 273
KEY_JOY2 = 274
KEY_JOY3 = 275
KEY_JOY4 = 276
KEY_JOY5 = 277
KEY_JOY6 = 278
KEY_JOY7 = 279
KEY_JOY8 = 280
KEY_JOY9 = 281
KEY_JOY10 = 282
KEY_JOY11 = 283
KEY_JOY12 = 284
KEY_JOY13 = 285
KEY_JOY14 = 286
KEY_JOY15 = 287
KEY_JOY16 = 288
KEY_JOY17 = 289
KEY_JOY18 = 290
KEY_JOY19 = 291
KEY_JOY20 = 292
KEY_JOY21 = 293
KEY_JOY22 = 294
KEY_JOY23 = 295
KEY_JOY24 = 296
KEY_JOY25 = 297
KEY_JOY26 = 298
KEY_JOY27 = 299
KEY_JOY28 = 300
KEY_JOY29 = 301
KEY_JOY30 = 302
KEY_JOY31 = 303
KEY_JOYDUP = 272
KEY_JOYDDOWN = 273
KEY_JOYDLEFT = 274
KEY_JOYDRIGHT = 275
KEY_JOYSTART = 276
KEY_JOYSELECT = 277
KEY_JOYBACK = 277
KEY_JOYALPUSH = 278
KEY_JOYARPUSH = 279
KEY_JOYCROSS = 280
KEY_JOYA = 280
KEY_JOYCIRCLE = 281
KEY_JOYB = 281
KEY_JOYSQUARE = 282
KEY_JOYX = 282
KEY_JOYTRIANGLE = 283
KEY_JOYY = 283
KEY_JOYL1 = 284
KEY_JOYBLACK = 284
KEY_JOYR1 = 285
KEY_JOYWHITE = 285
KEY_JOYL2 = 286
KEY_JOYLTRIGGER = 286
KEY_JOYR2 = 287
KEY_JOYRTRIGGER = 287
KEY_JOYAHARD = 288
KEY_JOYBHARD = 289
KEY_JOYXHARD = 290
KEY_JOYYHARD = 291
KEY_JOYBLACKHARD = 292
KEY_JOYWHITEHARD = 293
KEY_JOYLTRIGGERHARD = 294
KEY_JOYRTRIGGERHARD = 295
KEY_JOYALUP = 304
KEY_JOYALDOWN = 305
KEY_JOYALLEFT = 306
KEY_JOYALRIGHT = 307
KEY_JOYARUP = 308
KEY_JOYARDOWN = 309
KEY_JOYARLEFT = 310
KEY_JOYARRIGHT = 311
KEY_DEBUG = 312
KEY_LCDKB_LEFT = 320
KEY_LCDKB_RIGHT = 321
KEY_LCDKB_OK = 322
KEY_LCDKB_CANCEL = 323
KEY_LCDKB_UP = 324
KEY_LCDKB_DOWN = 325
KEY_LCDKB_MENU = 326
AXIS_LX = 0
AXIS_LY = 1
AXIS_RX = 2
AXIS_RY = 3
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\Keys.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:46:35 St�edn� Evropa (b�n� �as)