# Инициализация
init:

    # Локации и фоны
    image bg s01e01 = "bg01.png"

    # Персонажи
    image ca_default = "male01.png"
    image cb_default = "female01.png"
    image cc_default = "male02.png"
    image cd_default = "male03.png"

    transform centerZoomAndFade:
        parallel:
            zoom 0.8
            linear 8.0 zoom 1.0
        parallel:
            alpha 0.0 zoom 1.0
            linear 3.0 alpha 1.0
            pause 2.0
            linear 3.0 alpha 0.0

    transform easeFromRight:
        yalign 1.0
        zoom 1.0
        parallel:
            xalign 1.1
            easein 1.0 xalign 1.0
        parallel:
            alpha 0.0
            easein 1.0 alpha 1.0

    transform easeFromLeft:
        yalign 1.0
        xzoom -1.0 yzoom 1.0
        parallel:
            xalign -0.1
            easein 1.0 xalign 0
        parallel:
            alpha 0.0
            easein 1.0 alpha 1.0

    transform easeFromLeftBack00:
        yalign 1.0 xalign 0
        yzoom 0.75 xzoom -0.75
        parallel:
            alpha 0.0
            easein 0.5 alpha 1.0

    transform easeFromLeftBack01:
        yalign 1.0 xalign 0.15
        yzoom 0.75 xzoom -0.75
        parallel:
            alpha 0.0
            easein 0.5 alpha 1.0

    transform easeFromLeftBack02:
        yalign 1.0 xalign 0.3
        yzoom 0.75 xzoom -0.75
        parallel:
            alpha 0.0
            easein 0.5 alpha 1.0

# Определение ресурсов
define audio.amb01 = "music/ambience01.mp3"

# Определения
define fadeBetweenScenes = Fade(2.5, 0.0, 2.5)
define dissolveMedium = Dissolve(1.0)

# Определение персонажей игры.
define ca = Character('Ментор', color="#ffffff")
define cb = Character('CB', color="#ffffff")
define cc = Character('CC', color="#ffffff")
define cd = Character('CD', color="#ffffff")

# Игра начинается здесь:
# Пролог
label start:

    # play music ["<silence 2.0>", amb01] fadein 0.5 fadeout 1.0

    scene bg s01e01 with fadeBetweenScenes

    show text "Группа странников пересекает границу Предела" at centerZoomAndFade
    pause 6.0

    jump s01e01_act01

# Акт 1
label s01e01_act01:

    scene bg s01e01 with fadeBetweenScenes

    show ca_default at easeFromRight
    pause 0.25
    show cb_default at easeFromLeftBack00
    pause 0.1
    show cc_default at easeFromLeftBack01
    pause 0.1
    show cd_default at easeFromLeftBack02
    pause 0.1

    ca "Вы создали новую игру NO"

    show cb_default at easeFromLeft
    pause 0.25

    cb "Здесь что-то можно добавить еще..."
    cb "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    show cb_default at easeFromLeftBack00
    pause 0.1

    ca "Хорошо..."

    return
