# import colorgram
import turtle as t

t.colormode(255)
turtle = t.Turtle()


# def set_rgb_list():
#     colors = colorgram.extract("materials/spot-painting.jpg", 30)
#     rgb_list = []
#     for color in colors:
#         rgb = color.rgb
#         rgb_list.append((rgb.r, rgb.g, rgb.b))
#     return rgb_list


# print(set_rgb_list())

color_list = [
    (207, 160, 82),
    (54, 88, 130),
    (145, 91, 40),
    (140, 26, 49),
    (221, 207, 105),
    (132, 177, 203),
    (158, 46, 83),
    (45, 55, 104),
    (169, 160, 39),
    (129, 189, 143),
    (83, 20, 44),
    (37, 43, 67),
    (186, 94, 107),
    (187, 140, 170),
    (85, 120, 180),
    (59, 39, 31),
    (88, 157, 92),
    (78, 153, 165),
    (194, 79, 73),
    (45, 74, 78),
    (80, 74, 44),
    (161, 201, 218),
    (57, 125, 121),
    (219, 175, 187),
    (169, 206, 172),
    (219, 182, 169),
]

screen = t.Screen()
screen.exitonclick()
