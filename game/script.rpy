# Инициализация
init:

    # Локации и фоны
    image bg s01e01 = "bg01.png"

    # Персонажи
    image ca_default = "male01.png"
    image cb_default = "female01.png"

    transform centerZoomAndFade:
        parallel:
            zoom 1.0
            linear 8.0 zoom 1.4
        parallel:
            alpha 0.0 zoom 1.0
            linear 3.0 alpha 1.0
            pause 2.0
            linear 3.0 alpha 0.0

    transform easeFromRight:
        yalign 1.0
        parallel:
            xalign 1.1
            easein 1.0 xalign 1.0
        parallel:
            alpha 0.0
            easein 1.0 alpha 1.0

    transform easeFromLeft:
        yalign 1.0
        xzoom -1.0
        parallel:
            xalign -0.1
            easein 1.0 xalign 0
        parallel:
            alpha 0.0
            easein 1.0 alpha 1.0

# Определение ресурсов
define audio.amb01 = "music/ambience01.mp3"

# Определения
define fadeBetweenScenes = Fade(2.5, 0.0, 2.5)
define dissolveMedium = Dissolve(1.0)

# Определение персонажей игры.
define ca = Character('Ментор', color="#ffffff")
define cb = Character('Ангулла', color="#ffffff")

# Игра начинается здесь:
# Пролог
label start:

    play music ["<silence 2.0>", amb01] fadein 0.5 fadeout 1.0

    scene bg s01e01 with fadeBetweenScenes

    show text "На границе Предела" at centerZoomAndFade
    pause 8.0
    hide text
    show text "Они двигаются к завершению своей истории" at centerZoomAndFade
    pause 6.0

    jump s01e01_act01

# Акт 1
label s01e01_act01:

    scene bg s01e01 with fadeBetweenScenes

    show ca_default at easeFromRight

    ca "Вы создали новую игру NO"

    show cb_default at easeFromLeft

    cb "Здесь что-то можно добавить еще..."
    cb "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
