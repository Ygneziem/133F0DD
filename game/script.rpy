# Инициализация
init:

    image bg s01e01 = "bg01.png"
    image ca_default = "male01.png"

    transform fromDownToCenter:
        xalign 0.5 yalign 0.6
        #easein 1.0 yalign 0.6
        #linear 2.0 yalign 0.4
        #easeout 1.0 yalign 0.3
        linear 6.0 yalign 0.4

    transform easeFromRight:
        xalign 1.1 yalign 1.0
        easein 0.5 xalign 1.0

# Определения
define fadeBetweenScenes = Fade(2.0, 0.0, 2.0)
define dissolveMedium = Dissolve(1.0)

# Определение персонажей игры.
define ca = Character('Ментор', color="#ffffff")

# Игра начинается здесь:
# Пролог
label start:

    scene bg s01e01 with fadeBetweenScenes

    show text "На границе Предела" at fromDownToCenter with dissolveMedium
    pause 4
    hide text with dissolveMedium

    jump s01e01_act01

# Акт 1
label s01e01_act01:

    scene bg s01e01 with fadeBetweenScenes

    # Команда пересекает границу Предела
    show ca_default at easeFromRight with dissolveMedium

    ca "Вы создали новую игру NO"
    ca "Здесь что-то можно добавить еще..."
    ca "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
