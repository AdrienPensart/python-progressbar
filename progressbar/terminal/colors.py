# Based on: https://www.ditig.com/256-colors-cheat-sheet
import os

from progressbar.terminal.base import HLS, RGB, ColorGradient, Colors

black = Colors.register(RGB(0, 0, 0), HLS(0, 0, 0), 'Black', 0)
maroon = Colors.register(RGB(128, 0, 0), HLS(100, 0, 25), 'Maroon', 1)
green = Colors.register(RGB(0, 128, 0), HLS(100, 120, 25), 'Green', 2)
olive = Colors.register(RGB(128, 128, 0), HLS(100, 60, 25), 'Olive', 3)
navy = Colors.register(RGB(0, 0, 128), HLS(100, 240, 25), 'Navy', 4)
purple = Colors.register(RGB(128, 0, 128), HLS(100, 300, 25), 'Purple', 5)
teal = Colors.register(RGB(0, 128, 128), HLS(100, 180, 25), 'Teal', 6)
silver = Colors.register(RGB(192, 192, 192), HLS(0, 0, 75), 'Silver', 7)
grey = Colors.register(RGB(128, 128, 128), HLS(0, 0, 50), 'Grey', 8)
red = Colors.register(RGB(255, 0, 0), HLS(100, 0, 50), 'Red', 9)
lime = Colors.register(RGB(0, 255, 0), HLS(100, 120, 50), 'Lime', 10)
yellow = Colors.register(RGB(255, 255, 0), HLS(100, 60, 50), 'Yellow', 11)
blue = Colors.register(RGB(0, 0, 255), HLS(100, 240, 50), 'Blue', 12)
fuchsia = Colors.register(RGB(255, 0, 255), HLS(100, 300, 50), 'Fuchsia', 13)
aqua = Colors.register(RGB(0, 255, 255), HLS(100, 180, 50), 'Aqua', 14)
white = Colors.register(RGB(255, 255, 255), HLS(0, 0, 100), 'White', 15)
grey0 = Colors.register(RGB(0, 0, 0), HLS(0, 0, 0), 'Grey0', 16)
navy_blue = Colors.register(RGB(0, 0, 95), HLS(100, 240, 18), 'NavyBlue', 17)
dark_blue = Colors.register(RGB(0, 0, 135), HLS(100, 240, 26), 'DarkBlue', 18)
blue3 = Colors.register(RGB(0, 0, 175), HLS(100, 240, 34), 'Blue3', 19)
blue3 = Colors.register(RGB(0, 0, 215), HLS(100, 240, 42), 'Blue3', 20)
blue1 = Colors.register(RGB(0, 0, 255), HLS(100, 240, 50), 'Blue1', 21)
dark_green = Colors.register(RGB(0, 95, 0), HLS(100, 120, 18), 'DarkGreen', 22)
deep_sky_blue4 = Colors.register(
    RGB(0, 95, 95),
    HLS(100, 180, 18),
    'DeepSkyBlue4',
    23,
)
deep_sky_blue4 = Colors.register(
    RGB(0, 95, 135),
    HLS(100, 97, 26),
    'DeepSkyBlue4',
    24,
)
deep_sky_blue4 = Colors.register(
    RGB(0, 95, 175),
    HLS(100, 7, 34),
    'DeepSkyBlue4',
    25,
)
dodger_blue3 = Colors.register(
    RGB(0, 95, 215),
    HLS(100, 13, 42),
    'DodgerBlue3',
    26,
)
dodger_blue2 = Colors.register(
    RGB(0, 95, 255),
    HLS(100, 17, 50),
    'DodgerBlue2',
    27,
)
green4 = Colors.register(RGB(0, 135, 0), HLS(100, 120, 26), 'Green4', 28)
spring_green4 = Colors.register(
    RGB(0, 135, 95),
    HLS(100, 62, 26),
    'SpringGreen4',
    29,
)
turquoise4 = Colors.register(
    RGB(0, 135, 135),
    HLS(100, 180, 26),
    'Turquoise4',
    30,
)
deep_sky_blue3 = Colors.register(
    RGB(0, 135, 175),
    HLS(100, 93, 34),
    'DeepSkyBlue3',
    31,
)
deep_sky_blue3 = Colors.register(
    RGB(0, 135, 215),
    HLS(100, 2, 42),
    'DeepSkyBlue3',
    32,
)
dodger_blue1 = Colors.register(
    RGB(0, 135, 255),
    HLS(100, 8, 50),
    'DodgerBlue1',
    33,
)
green3 = Colors.register(RGB(0, 175, 0), HLS(100, 120, 34), 'Green3', 34)
spring_green3 = Colors.register(
    RGB(0, 175, 95),
    HLS(100, 52, 34),
    'SpringGreen3',
    35,
)
dark_cyan = Colors.register(RGB(0, 175, 135), HLS(100, 66, 34), 'DarkCyan', 36)
light_sea_green = Colors.register(
    RGB(0, 175, 175),
    HLS(100, 180, 34),
    'LightSeaGreen',
    37,
)
deep_sky_blue2 = Colors.register(
    RGB(0, 175, 215),
    HLS(100, 91, 42),
    'DeepSkyBlue2',
    38,
)
deep_sky_blue1 = Colors.register(
    RGB(0, 175, 255),
    HLS(100, 98, 50),
    'DeepSkyBlue1',
    39,
)
green3 = Colors.register(RGB(0, 215, 0), HLS(100, 120, 42), 'Green3', 40)
spring_green3 = Colors.register(
    RGB(0, 215, 95),
    HLS(100, 46, 42),
    'SpringGreen3',
    41,
)
spring_green2 = Colors.register(
    RGB(0, 215, 135),
    HLS(100, 57, 42),
    'SpringGreen2',
    42,
)
cyan3 = Colors.register(RGB(0, 215, 175), HLS(100, 68, 42), 'Cyan3', 43)
dark_turquoise = Colors.register(
    RGB(0, 215, 215),
    HLS(100, 180, 42),
    'DarkTurquoise',
    44,
)
turquoise2 = Colors.register(
    RGB(0, 215, 255),
    HLS(100, 89, 50),
    'Turquoise2',
    45,
)
green1 = Colors.register(RGB(0, 255, 0), HLS(100, 120, 50), 'Green1', 46)
spring_green2 = Colors.register(
    RGB(0, 255, 95),
    HLS(100, 42, 50),
    'SpringGreen2',
    47,
)
spring_green1 = Colors.register(
    RGB(0, 255, 135),
    HLS(100, 51, 50),
    'SpringGreen1',
    48,
)
medium_spring_green = Colors.register(
    RGB(0, 255, 175),
    HLS(100, 61, 50),
    'MediumSpringGreen',
    49,
)
cyan2 = Colors.register(RGB(0, 255, 215), HLS(100, 70, 50), 'Cyan2', 50)
cyan1 = Colors.register(RGB(0, 255, 255), HLS(100, 180, 50), 'Cyan1', 51)
dark_red = Colors.register(RGB(95, 0, 0), HLS(100, 0, 18), 'DarkRed', 52)
deep_pink4 = Colors.register(
    RGB(95, 0, 95), HLS(100, 300, 18), 'DeepPink4', 53
)
purple4 = Colors.register(RGB(95, 0, 135), HLS(100, 82, 26), 'Purple4', 54)
purple4 = Colors.register(RGB(95, 0, 175), HLS(100, 72, 34), 'Purple4', 55)
purple3 = Colors.register(RGB(95, 0, 215), HLS(100, 66, 42), 'Purple3', 56)
blue_violet = Colors.register(
    RGB(95, 0, 255),
    HLS(100, 62, 50),
    'BlueViolet',
    57,
)
orange4 = Colors.register(RGB(95, 95, 0), HLS(100, 60, 18), 'Orange4', 58)
grey37 = Colors.register(RGB(95, 95, 95), HLS(0, 0, 37), 'Grey37', 59)
medium_purple4 = Colors.register(
    RGB(95, 95, 135),
    HLS(17, 240, 45),
    'MediumPurple4',
    60,
)
slate_blue3 = Colors.register(
    RGB(95, 95, 175),
    HLS(33, 240, 52),
    'SlateBlue3',
    61,
)
slate_blue3 = Colors.register(
    RGB(95, 95, 215),
    HLS(60, 240, 60),
    'SlateBlue3',
    62,
)
royal_blue1 = Colors.register(
    RGB(95, 95, 255),
    HLS(100, 240, 68),
    'RoyalBlue1',
    63,
)
chartreuse4 = Colors.register(
    RGB(95, 135, 0),
    HLS(100, 7, 26),
    'Chartreuse4',
    64,
)
dark_sea_green4 = Colors.register(
    RGB(95, 135, 95),
    HLS(17, 120, 45),
    'DarkSeaGreen4',
    65,
)
pale_turquoise4 = Colors.register(
    RGB(95, 135, 135),
    HLS(17, 180, 45),
    'PaleTurquoise4',
    66,
)
steel_blue = Colors.register(
    RGB(95, 135, 175),
    HLS(33, 210, 52),
    'SteelBlue',
    67,
)
steel_blue3 = Colors.register(
    RGB(95, 135, 215),
    HLS(60, 220, 60),
    'SteelBlue3',
    68,
)
cornflower_blue = Colors.register(
    RGB(95, 135, 255),
    HLS(100, 225, 68),
    'CornflowerBlue',
    69,
)
chartreuse3 = Colors.register(
    RGB(95, 175, 0),
    HLS(100, 7, 34),
    'Chartreuse3',
    70,
)
dark_sea_green4 = Colors.register(
    RGB(95, 175, 95),
    HLS(33, 120, 52),
    'DarkSeaGreen4',
    71,
)
cadet_blue = Colors.register(
    RGB(95, 175, 135),
    HLS(33, 150, 52),
    'CadetBlue',
    72,
)
cadet_blue = Colors.register(
    RGB(95, 175, 175),
    HLS(33, 180, 52),
    'CadetBlue',
    73,
)
sky_blue3 = Colors.register(
    RGB(95, 175, 215), HLS(60, 200, 60), 'SkyBlue3', 74
)
steel_blue1 = Colors.register(
    RGB(95, 175, 255),
    HLS(100, 210, 68),
    'SteelBlue1',
    75,
)
chartreuse3 = Colors.register(
    RGB(95, 215, 0),
    HLS(100, 3, 42),
    'Chartreuse3',
    76,
)
pale_green3 = Colors.register(
    RGB(95, 215, 95),
    HLS(60, 120, 60),
    'PaleGreen3',
    77,
)
sea_green3 = Colors.register(
    RGB(95, 215, 135),
    HLS(60, 140, 60),
    'SeaGreen3',
    78,
)
aquamarine3 = Colors.register(
    RGB(95, 215, 175),
    HLS(60, 160, 60),
    'Aquamarine3',
    79,
)
medium_turquoise = Colors.register(
    RGB(95, 215, 215),
    HLS(60, 180, 60),
    'MediumTurquoise',
    80,
)
steel_blue1 = Colors.register(
    RGB(95, 215, 255),
    HLS(100, 195, 68),
    'SteelBlue1',
    81,
)
chartreuse2 = Colors.register(
    RGB(95, 255, 0),
    HLS(100, 7, 50),
    'Chartreuse2',
    82,
)
sea_green2 = Colors.register(
    RGB(95, 255, 95),
    HLS(100, 120, 68),
    'SeaGreen2',
    83,
)
sea_green1 = Colors.register(
    RGB(95, 255, 135),
    HLS(100, 135, 68),
    'SeaGreen1',
    84,
)
sea_green1 = Colors.register(
    RGB(95, 255, 175),
    HLS(100, 150, 68),
    'SeaGreen1',
    85,
)
aquamarine1 = Colors.register(
    RGB(95, 255, 215),
    HLS(100, 165, 68),
    'Aquamarine1',
    86,
)
dark_slate_gray2 = Colors.register(
    RGB(95, 255, 255),
    HLS(100, 180, 68),
    'DarkSlateGray2',
    87,
)
dark_red = Colors.register(RGB(135, 0, 0), HLS(100, 0, 26), 'DarkRed', 88)
deep_pink4 = Colors.register(
    RGB(135, 0, 95), HLS(100, 17, 26), 'DeepPink4', 89
)
dark_magenta = Colors.register(
    RGB(135, 0, 135),
    HLS(100, 300, 26),
    'DarkMagenta',
    90,
)
dark_magenta = Colors.register(
    RGB(135, 0, 175),
    HLS(100, 86, 34),
    'DarkMagenta',
    91,
)
dark_violet = Colors.register(
    RGB(135, 0, 215),
    HLS(100, 77, 42),
    'DarkViolet',
    92,
)
purple = Colors.register(RGB(135, 0, 255), HLS(100, 71, 50), 'Purple', 93)
orange4 = Colors.register(RGB(135, 95, 0), HLS(100, 2, 26), 'Orange4', 94)
light_pink4 = Colors.register(
    RGB(135, 95, 95),
    HLS(17, 0, 45),
    'LightPink4',
    95,
)
plum4 = Colors.register(RGB(135, 95, 135), HLS(17, 300, 45), 'Plum4', 96)
medium_purple3 = Colors.register(
    RGB(135, 95, 175),
    HLS(33, 270, 52),
    'MediumPurple3',
    97,
)
medium_purple3 = Colors.register(
    RGB(135, 95, 215),
    HLS(60, 260, 60),
    'MediumPurple3',
    98,
)
slate_blue1 = Colors.register(
    RGB(135, 95, 255),
    HLS(100, 255, 68),
    'SlateBlue1',
    99,
)
yellow4 = Colors.register(RGB(135, 135, 0), HLS(100, 60, 26), 'Yellow4', 100)
wheat4 = Colors.register(RGB(135, 135, 95), HLS(17, 60, 45), 'Wheat4', 101)
grey53 = Colors.register(RGB(135, 135, 135), HLS(0, 0, 52), 'Grey53', 102)
light_slate_grey = Colors.register(
    RGB(135, 135, 175),
    HLS(20, 240, 60),
    'LightSlateGrey',
    103,
)
medium_purple = Colors.register(
    RGB(135, 135, 215),
    HLS(50, 240, 68),
    'MediumPurple',
    104,
)
light_slate_blue = Colors.register(
    RGB(135, 135, 255),
    HLS(100, 240, 76),
    'LightSlateBlue',
    105,
)
yellow4 = Colors.register(RGB(135, 175, 0), HLS(100, 3, 34), 'Yellow4', 106)
dark_olive_green3 = Colors.register(
    RGB(135, 175, 95),
    HLS(33, 90, 52),
    'DarkOliveGreen3',
    107,
)
dark_sea_green = Colors.register(
    RGB(135, 175, 135),
    HLS(20, 120, 60),
    'DarkSeaGreen',
    108,
)
light_sky_blue3 = Colors.register(
    RGB(135, 175, 175),
    HLS(20, 180, 60),
    'LightSkyBlue3',
    109,
)
light_sky_blue3 = Colors.register(
    RGB(135, 175, 215),
    HLS(50, 210, 68),
    'LightSkyBlue3',
    110,
)
sky_blue2 = Colors.register(
    RGB(135, 175, 255),
    HLS(100, 220, 76),
    'SkyBlue2',
    111,
)
chartreuse2 = Colors.register(
    RGB(135, 215, 0),
    HLS(100, 2, 42),
    'Chartreuse2',
    112,
)
dark_olive_green3 = Colors.register(
    RGB(135, 215, 95),
    HLS(60, 100, 60),
    'DarkOliveGreen3',
    113,
)
pale_green3 = Colors.register(
    RGB(135, 215, 135),
    HLS(50, 120, 68),
    'PaleGreen3',
    114,
)
dark_sea_green3 = Colors.register(
    RGB(135, 215, 175),
    HLS(50, 150, 68),
    'DarkSeaGreen3',
    115,
)
dark_slate_gray3 = Colors.register(
    RGB(135, 215, 215),
    HLS(50, 180, 68),
    'DarkSlateGray3',
    116,
)
sky_blue1 = Colors.register(
    RGB(135, 215, 255),
    HLS(100, 200, 76),
    'SkyBlue1',
    117,
)
chartreuse1 = Colors.register(
    RGB(135, 255, 0),
    HLS(100, 8, 50),
    'Chartreuse1',
    118,
)
light_green = Colors.register(
    RGB(135, 255, 95),
    HLS(100, 105, 68),
    'LightGreen',
    119,
)
light_green = Colors.register(
    RGB(135, 255, 135),
    HLS(100, 120, 76),
    'LightGreen',
    120,
)
pale_green1 = Colors.register(
    RGB(135, 255, 175),
    HLS(100, 140, 76),
    'PaleGreen1',
    121,
)
aquamarine1 = Colors.register(
    RGB(135, 255, 215),
    HLS(100, 160, 76),
    'Aquamarine1',
    122,
)
dark_slate_gray1 = Colors.register(
    RGB(135, 255, 255),
    HLS(100, 180, 76),
    'DarkSlateGray1',
    123,
)
red3 = Colors.register(RGB(175, 0, 0), HLS(100, 0, 34), 'Red3', 124)
deep_pink4 = Colors.register(
    RGB(175, 0, 95),
    HLS(100, 27, 34),
    'DeepPink4',
    125,
)
medium_violet_red = Colors.register(
    RGB(175, 0, 135),
    HLS(100, 13, 34),
    'MediumVioletRed',
    126,
)
magenta3 = Colors.register(
    RGB(175, 0, 175),
    HLS(100, 300, 34),
    'Magenta3',
    127,
)
dark_violet = Colors.register(
    RGB(175, 0, 215),
    HLS(100, 88, 42),
    'DarkViolet',
    128,
)
purple = Colors.register(RGB(175, 0, 255), HLS(100, 81, 50), 'Purple', 129)
dark_orange3 = Colors.register(
    RGB(175, 95, 0),
    HLS(100, 2, 34),
    'DarkOrange3',
    130,
)
indian_red = Colors.register(
    RGB(175, 95, 95), HLS(33, 0, 52), 'IndianRed', 131
)
hot_pink3 = Colors.register(
    RGB(175, 95, 135),
    HLS(33, 330, 52),
    'HotPink3',
    132,
)
medium_orchid3 = Colors.register(
    RGB(175, 95, 175),
    HLS(33, 300, 52),
    'MediumOrchid3',
    133,
)
medium_orchid = Colors.register(
    RGB(175, 95, 215),
    HLS(60, 280, 60),
    'MediumOrchid',
    134,
)
medium_purple2 = Colors.register(
    RGB(175, 95, 255),
    HLS(100, 270, 68),
    'MediumPurple2',
    135,
)
dark_goldenrod = Colors.register(
    RGB(175, 135, 0),
    HLS(100, 6, 34),
    'DarkGoldenrod',
    136,
)
light_salmon3 = Colors.register(
    RGB(175, 135, 95),
    HLS(33, 30, 52),
    'LightSalmon3',
    137,
)
rosy_brown = Colors.register(
    RGB(175, 135, 135),
    HLS(20, 0, 60),
    'RosyBrown',
    138,
)
grey63 = Colors.register(RGB(175, 135, 175), HLS(20, 300, 60), 'Grey63', 139)
medium_purple2 = Colors.register(
    RGB(175, 135, 215),
    HLS(50, 270, 68),
    'MediumPurple2',
    140,
)
medium_purple1 = Colors.register(
    RGB(175, 135, 255),
    HLS(100, 260, 76),
    'MediumPurple1',
    141,
)
gold3 = Colors.register(RGB(175, 175, 0), HLS(100, 60, 34), 'Gold3', 142)
dark_khaki = Colors.register(
    RGB(175, 175, 95),
    HLS(33, 60, 52),
    'DarkKhaki',
    143,
)
navajo_white3 = Colors.register(
    RGB(175, 175, 135),
    HLS(20, 60, 60),
    'NavajoWhite3',
    144,
)
grey69 = Colors.register(RGB(175, 175, 175), HLS(0, 0, 68), 'Grey69', 145)
light_steel_blue3 = Colors.register(
    RGB(175, 175, 215),
    HLS(33, 240, 76),
    'LightSteelBlue3',
    146,
)
light_steel_blue = Colors.register(
    RGB(175, 175, 255),
    HLS(100, 240, 84),
    'LightSteelBlue',
    147,
)
yellow3 = Colors.register(RGB(175, 215, 0), HLS(100, 1, 42), 'Yellow3', 148)
dark_olive_green3 = Colors.register(
    RGB(175, 215, 95),
    HLS(60, 80, 60),
    'DarkOliveGreen3',
    149,
)
dark_sea_green3 = Colors.register(
    RGB(175, 215, 135),
    HLS(50, 90, 68),
    'DarkSeaGreen3',
    150,
)
dark_sea_green2 = Colors.register(
    RGB(175, 215, 175),
    HLS(33, 120, 76),
    'DarkSeaGreen2',
    151,
)
light_cyan3 = Colors.register(
    RGB(175, 215, 215),
    HLS(33, 180, 76),
    'LightCyan3',
    152,
)
light_sky_blue1 = Colors.register(
    RGB(175, 215, 255),
    HLS(100, 210, 84),
    'LightSkyBlue1',
    153,
)
green_yellow = Colors.register(
    RGB(175, 255, 0),
    HLS(100, 8, 50),
    'GreenYellow',
    154,
)
dark_olive_green2 = Colors.register(
    RGB(175, 255, 95),
    HLS(100, 90, 68),
    'DarkOliveGreen2',
    155,
)
pale_green1 = Colors.register(
    RGB(175, 255, 135),
    HLS(100, 100, 76),
    'PaleGreen1',
    156,
)
dark_sea_green2 = Colors.register(
    RGB(175, 255, 175),
    HLS(100, 120, 84),
    'DarkSeaGreen2',
    157,
)
dark_sea_green1 = Colors.register(
    RGB(175, 255, 215),
    HLS(100, 150, 84),
    'DarkSeaGreen1',
    158,
)
pale_turquoise1 = Colors.register(
    RGB(175, 255, 255),
    HLS(100, 180, 84),
    'PaleTurquoise1',
    159,
)
red3 = Colors.register(RGB(215, 0, 0), HLS(100, 0, 42), 'Red3', 160)
deep_pink3 = Colors.register(
    RGB(215, 0, 95),
    HLS(100, 33, 42),
    'DeepPink3',
    161,
)
deep_pink3 = Colors.register(
    RGB(215, 0, 135),
    HLS(100, 22, 42),
    'DeepPink3',
    162,
)
magenta3 = Colors.register(RGB(215, 0, 175), HLS(100, 11, 42), 'Magenta3', 163)
magenta3 = Colors.register(
    RGB(215, 0, 215),
    HLS(100, 300, 42),
    'Magenta3',
    164,
)
magenta2 = Colors.register(RGB(215, 0, 255), HLS(100, 90, 50), 'Magenta2', 165)
dark_orange3 = Colors.register(
    RGB(215, 95, 0),
    HLS(100, 6, 42),
    'DarkOrange3',
    166,
)
indian_red = Colors.register(
    RGB(215, 95, 95), HLS(60, 0, 60), 'IndianRed', 167
)
hot_pink3 = Colors.register(
    RGB(215, 95, 135),
    HLS(60, 340, 60),
    'HotPink3',
    168,
)
hot_pink2 = Colors.register(
    RGB(215, 95, 175),
    HLS(60, 320, 60),
    'HotPink2',
    169,
)
orchid = Colors.register(RGB(215, 95, 215), HLS(60, 300, 60), 'Orchid', 170)
medium_orchid1 = Colors.register(
    RGB(215, 95, 255),
    HLS(100, 285, 68),
    'MediumOrchid1',
    171,
)
orange3 = Colors.register(RGB(215, 135, 0), HLS(100, 7, 42), 'Orange3', 172)
light_salmon3 = Colors.register(
    RGB(215, 135, 95),
    HLS(60, 20, 60),
    'LightSalmon3',
    173,
)
light_pink3 = Colors.register(
    RGB(215, 135, 135),
    HLS(50, 0, 68),
    'LightPink3',
    174,
)
pink3 = Colors.register(RGB(215, 135, 175), HLS(50, 330, 68), 'Pink3', 175)
plum3 = Colors.register(RGB(215, 135, 215), HLS(50, 300, 68), 'Plum3', 176)
violet = Colors.register(RGB(215, 135, 255), HLS(100, 280, 76), 'Violet', 177)
gold3 = Colors.register(RGB(215, 175, 0), HLS(100, 8, 42), 'Gold3', 178)
light_goldenrod3 = Colors.register(
    RGB(215, 175, 95),
    HLS(60, 40, 60),
    'LightGoldenrod3',
    179,
)
tan = Colors.register(RGB(215, 175, 135), HLS(50, 30, 68), 'Tan', 180)
misty_rose3 = Colors.register(
    RGB(215, 175, 175),
    HLS(33, 0, 76),
    'MistyRose3',
    181,
)
thistle3 = Colors.register(
    RGB(215, 175, 215),
    HLS(33, 300, 76),
    'Thistle3',
    182,
)
plum2 = Colors.register(RGB(215, 175, 255), HLS(100, 270, 84), 'Plum2', 183)
yellow3 = Colors.register(RGB(215, 215, 0), HLS(100, 60, 42), 'Yellow3', 184)
khaki3 = Colors.register(RGB(215, 215, 95), HLS(60, 60, 60), 'Khaki3', 185)
light_goldenrod2 = Colors.register(
    RGB(215, 215, 135),
    HLS(50, 60, 68),
    'LightGoldenrod2',
    186,
)
light_yellow3 = Colors.register(
    RGB(215, 215, 175),
    HLS(33, 60, 76),
    'LightYellow3',
    187,
)
grey84 = Colors.register(RGB(215, 215, 215), HLS(0, 0, 84), 'Grey84', 188)
light_steel_blue1 = Colors.register(
    RGB(215, 215, 255),
    HLS(100, 240, 92),
    'LightSteelBlue1',
    189,
)
yellow2 = Colors.register(RGB(215, 255, 0), HLS(100, 9, 50), 'Yellow2', 190)
dark_olive_green1 = Colors.register(
    RGB(215, 255, 95),
    HLS(100, 75, 68),
    'DarkOliveGreen1',
    191,
)
dark_olive_green1 = Colors.register(
    RGB(215, 255, 135),
    HLS(100, 80, 76),
    'DarkOliveGreen1',
    192,
)
dark_sea_green1 = Colors.register(
    RGB(215, 255, 175),
    HLS(100, 90, 84),
    'DarkSeaGreen1',
    193,
)
honeydew2 = Colors.register(
    RGB(215, 255, 215),
    HLS(100, 120, 92),
    'Honeydew2',
    194,
)
light_cyan1 = Colors.register(
    RGB(215, 255, 255),
    HLS(100, 180, 92),
    'LightCyan1',
    195,
)
red1 = Colors.register(RGB(255, 0, 0), HLS(100, 0, 50), 'Red1', 196)
deep_pink2 = Colors.register(
    RGB(255, 0, 95),
    HLS(100, 37, 50),
    'DeepPink2',
    197,
)
deep_pink1 = Colors.register(
    RGB(255, 0, 135),
    HLS(100, 28, 50),
    'DeepPink1',
    198,
)
deep_pink1 = Colors.register(
    RGB(255, 0, 175),
    HLS(100, 18, 50),
    'DeepPink1',
    199,
)
magenta2 = Colors.register(RGB(255, 0, 215), HLS(100, 9, 50), 'Magenta2', 200)
magenta1 = Colors.register(
    RGB(255, 0, 255),
    HLS(100, 300, 50),
    'Magenta1',
    201,
)
orange_red1 = Colors.register(
    RGB(255, 95, 0),
    HLS(100, 2, 50),
    'OrangeRed1',
    202,
)
indian_red1 = Colors.register(
    RGB(255, 95, 95),
    HLS(100, 0, 68),
    'IndianRed1',
    203,
)
indian_red1 = Colors.register(
    RGB(255, 95, 135),
    HLS(100, 345, 68),
    'IndianRed1',
    204,
)
hot_pink = Colors.register(
    RGB(255, 95, 175), HLS(100, 330, 68), 'HotPink', 205
)
hot_pink = Colors.register(
    RGB(255, 95, 215), HLS(100, 315, 68), 'HotPink', 206
)
medium_orchid1 = Colors.register(
    RGB(255, 95, 255),
    HLS(100, 300, 68),
    'MediumOrchid1',
    207,
)
dark_orange = Colors.register(
    RGB(255, 135, 0),
    HLS(100, 1, 50),
    'DarkOrange',
    208,
)
salmon1 = Colors.register(RGB(255, 135, 95), HLS(100, 15, 68), 'Salmon1', 209)
light_coral = Colors.register(
    RGB(255, 135, 135),
    HLS(100, 0, 76),
    'LightCoral',
    210,
)
pale_violet_red1 = Colors.register(
    RGB(255, 135, 175),
    HLS(100, 340, 76),
    'PaleVioletRed1',
    211,
)
orchid2 = Colors.register(
    RGB(255, 135, 215),
    HLS(100, 320, 76),
    'Orchid2',
    212,
)
orchid1 = Colors.register(
    RGB(255, 135, 255),
    HLS(100, 300, 76),
    'Orchid1',
    213,
)
orange1 = Colors.register(RGB(255, 175, 0), HLS(100, 1, 50), 'Orange1', 214)
sandy_brown = Colors.register(
    RGB(255, 175, 95),
    HLS(100, 30, 68),
    'SandyBrown',
    215,
)
light_salmon1 = Colors.register(
    RGB(255, 175, 135),
    HLS(100, 20, 76),
    'LightSalmon1',
    216,
)
light_pink1 = Colors.register(
    RGB(255, 175, 175),
    HLS(100, 0, 84),
    'LightPink1',
    217,
)
pink1 = Colors.register(RGB(255, 175, 215), HLS(100, 330, 84), 'Pink1', 218)
plum1 = Colors.register(RGB(255, 175, 255), HLS(100, 300, 84), 'Plum1', 219)
gold1 = Colors.register(RGB(255, 215, 0), HLS(100, 0, 50), 'Gold1', 220)
light_goldenrod2 = Colors.register(
    RGB(255, 215, 95),
    HLS(100, 45, 68),
    'LightGoldenrod2',
    221,
)
light_goldenrod2 = Colors.register(
    RGB(255, 215, 135),
    HLS(100, 40, 76),
    'LightGoldenrod2',
    222,
)
navajo_white1 = Colors.register(
    RGB(255, 215, 175),
    HLS(100, 30, 84),
    'NavajoWhite1',
    223,
)
misty_rose1 = Colors.register(
    RGB(255, 215, 215),
    HLS(100, 0, 92),
    'MistyRose1',
    224,
)
thistle1 = Colors.register(
    RGB(255, 215, 255),
    HLS(100, 300, 92),
    'Thistle1',
    225,
)
yellow1 = Colors.register(RGB(255, 255, 0), HLS(100, 60, 50), 'Yellow1', 226)
light_goldenrod1 = Colors.register(
    RGB(255, 255, 95),
    HLS(100, 60, 68),
    'LightGoldenrod1',
    227,
)
khaki1 = Colors.register(RGB(255, 255, 135), HLS(100, 60, 76), 'Khaki1', 228)
wheat1 = Colors.register(RGB(255, 255, 175), HLS(100, 60, 84), 'Wheat1', 229)
cornsilk1 = Colors.register(
    RGB(255, 255, 215),
    HLS(100, 60, 92),
    'Cornsilk1',
    230,
)
grey100 = Colors.register(RGB(255, 255, 255), HLS(0, 0, 100), 'Grey100', 231)
grey3 = Colors.register(RGB(8, 8, 8), HLS(0, 0, 3), 'Grey3', 232)
grey7 = Colors.register(RGB(18, 18, 18), HLS(0, 0, 7), 'Grey7', 233)
grey11 = Colors.register(RGB(28, 28, 28), HLS(0, 0, 10), 'Grey11', 234)
grey15 = Colors.register(RGB(38, 38, 38), HLS(0, 0, 14), 'Grey15', 235)
grey19 = Colors.register(RGB(48, 48, 48), HLS(0, 0, 18), 'Grey19', 236)
grey23 = Colors.register(RGB(58, 58, 58), HLS(0, 0, 22), 'Grey23', 237)
grey27 = Colors.register(RGB(68, 68, 68), HLS(0, 0, 26), 'Grey27', 238)
grey30 = Colors.register(RGB(78, 78, 78), HLS(0, 0, 30), 'Grey30', 239)
grey35 = Colors.register(RGB(88, 88, 88), HLS(0, 0, 34), 'Grey35', 240)
grey39 = Colors.register(RGB(98, 98, 98), HLS(0, 0, 37), 'Grey39', 241)
grey42 = Colors.register(RGB(108, 108, 108), HLS(0, 0, 40), 'Grey42', 242)
grey46 = Colors.register(RGB(118, 118, 118), HLS(0, 0, 46), 'Grey46', 243)
grey50 = Colors.register(RGB(128, 128, 128), HLS(0, 0, 50), 'Grey50', 244)
grey54 = Colors.register(RGB(138, 138, 138), HLS(0, 0, 54), 'Grey54', 245)
grey58 = Colors.register(RGB(148, 148, 148), HLS(0, 0, 58), 'Grey58', 246)
grey62 = Colors.register(RGB(158, 158, 158), HLS(0, 0, 61), 'Grey62', 247)
grey66 = Colors.register(RGB(168, 168, 168), HLS(0, 0, 65), 'Grey66', 248)
grey70 = Colors.register(RGB(178, 178, 178), HLS(0, 0, 69), 'Grey70', 249)
grey74 = Colors.register(RGB(188, 188, 188), HLS(0, 0, 73), 'Grey74', 250)
grey78 = Colors.register(RGB(198, 198, 198), HLS(0, 0, 77), 'Grey78', 251)
grey82 = Colors.register(RGB(208, 208, 208), HLS(0, 0, 81), 'Grey82', 252)
grey85 = Colors.register(RGB(218, 218, 218), HLS(0, 0, 85), 'Grey85', 253)
grey89 = Colors.register(RGB(228, 228, 228), HLS(0, 0, 89), 'Grey89', 254)
grey93 = Colors.register(RGB(238, 238, 238), HLS(0, 0, 93), 'Grey93', 255)

dark_gradient = ColorGradient(
    red1,
    orange_red1,
    dark_orange,
    orange1,
    yellow1,
    yellow2,
    green_yellow,
    green1,
)
light_gradient = ColorGradient(
    red1,
    orange_red1,
    dark_orange,
    orange1,
    gold3,
    dark_olive_green3,
    yellow4,
    green3,
)
bg_gradient = ColorGradient(black)

# Check if the background is light or dark. This is by no means a foolproof
# method, but there is no reliable way to detect this.
if os.environ.get('COLORFGBG', '15;0').split(';')[-1] == str(white.xterm):
    # Light background
    gradient = light_gradient
    primary = black
else:
    # Default, expect a dark background
    gradient = dark_gradient
    primary = white
