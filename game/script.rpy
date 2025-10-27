# Определение персонажей игры.
define e = Character('Незнакомка', color="#291246")



# Игра начинается здесь:
label start:

# Все функции которые будут использоваться в игре:

    python:
        def show_image(x):
            image_map = {
                0: "tabs0.png",
                1: "tabs1.png",
                2: "tabs2.png",
                3: "tabs3.png",
                4: "tabs4.png",
                5: "tabs5.png",
                6: "tabs6.png"
            }
            
            return image_map.get(x, None)




    jump act1
#Все локации которые будут использоваться в игре:

#Спальня с книпками

screen bedroom_map():
    imagemap:
        idle "bedroom"
        hover "bedroom2"

        hotspot (191, 191, 250, 400) action Jump("titles") alt "Swimming"
        hotspot (90, 620, 830, 320) action Notify("Я не устал.")
#        hotspot (191, 191, 250, 400) action Jump("titles") alt "Swimming"   
#        hotspot (191, 191, 250, 400) action Jump("titles") alt "Swimming"
#        hotspot (191, 191, 250, 400) action Jump("titles") alt "Swimming"
        hotspot (1390, 988, 530, 92) action Jump("kitchen") alt "Swimming"


screen kitchen_map():
    imagemap:
        idle "kitchen"
        hover "kitchen2"

        hotspot (1, 900, 400, 180) action Jump("bedroom") alt "Swimming"

#Интерактивные кнопки в спальне:

#Кровать
#    call screen bed_button

#label bed:
#    screen bed_button():
#        frame:
#            xpos 1 
#            ypos 600
#            button:
#                add "bed.png"
#                action Notify("Я не устал.")
#                hovered Notify("Кровать.")

#Окно
#    call screen window_in_bedroom_button

#label window_in_bedroom:
#    screen window_in_bedroom_button():
#        frame:
#            xpos 800 
#            ypos 200
#            button:
#                add "window_in_bed.png"
#                action Jump("window_in_bedroom_big")
#                hovered Notify("Окно.")

#Вернуться обратно в спальню
#    call screen windowsill_in_bedroom_button

#label windowsill_in_window:
#    screen windowsill_in_bedroom_button():
#        frame:
#            xpos 1 
#            ypos 900
#            button:
#                add "windowsill.png"
#                action Jump("bedroom")
#                hovered Notify("Спальня.")

#Bedroom — комната, где просыпается герой

label bedroom:

    call screen bedroom_map


#label window_in_bedroom_big:

#    scene window_bg

#    call screen windowsill_in_bedroom_button

#    pause (None)
    #девушка
    #таблетка
    #дверь


#Если у игрока есть какие-то данные он сможет подойти к девушке
#Откроется новый скрипт а так он может свободно
#Передвигаться по дому

#Basement — место со следами крови

label basement:



#Attic — возможное место хранения старых вещей

label attic:

#Study — место, где хранятся документы и дневник

label study:

#Kitchen — место, где герой может найти лекарства

label kitchen:

    call screen kitchen_map

label livingroom:



#Bathroom лекарства

label bathroom:

label kidsbedroom:



#Акт 1. Пробуждение

label act1:

    scene kill
#    play sound "scream.mp3"

    "НЕ НАДО! НЕЕТ!"

    scene black

    pause (2)

    scene home

    play sound "dark.mp3"

    
    #Сцена 1. Первое пробуждение
    #Заброшенный дом в деревне. Полумрак. Герой лежит на кровати, рядом разбросаны медицинские инструменты. В комнате пахнет лекарствами.

    #Герой (приоткрывает глаза, хватается за голову): 
    "Где я? Что со мной случилось? Почему я ничего не помню?"

    #Незнакомка (входит с чашкой, мягко): 
    show sorry:
        xalign 0.0
        yalign 1.0

    e "Тише, не торопитесь. Выпейте это, вам станет легче."
    
menu:

    "Хорошо.":
        jump choice1_yes

    "Нет.":
        jump choice_death

label choice1_yes:

    $ tabs = 6

    jump choice1_done

label choice1_done:

    # ... the game continues here.
 
    # добавление таблеток
    $ image_name = show_image(tabs)
    show image image_name:
        xalign 1.2
        yalign 1.15

    #Герой (недоверчиво): 

    "Кто вы такая? Где моя семья? Что с ними?"


#menu:
#
#    "Кто вы такая? Где моя семья? Что с ними?":
#        jump choice2_done
#
#    "Это ты убила их!!":
#        jump choice2_yes

#label choice2_yes:

#    $ tabs -= 1

#    jump choice2_done

#label choice2_done:

    #Незнакомка: 
#    $ image_name = show_image(tabs)
#    show image image_name:
#        xalign 1.2
#        yalign 1.15

    e "Ваша семья… Они в безопасности. А я — ваш врач, я помогаю вам восстановиться."

    #Герой: 
    "Восстановить что? Я не понимаю, что происходит!"

    #Незнакомка: 

    e "Память иногда играет с нами злые шутки. Но мы справимся с этим вместе."


    #Герой: 
    "Сколько я был без сознания?"

    #Незнакомка: 

    e "Недолго. Но вам нужно отдохнуть."



#    call screen example_screen

#label news:
#    screen example_screen():
    # Создаём imagebutton с изображением для состояния idle и hover
#        imagebutton:
#            idle "news.png"  # Изображение для состояния покоя
#            hover "newsb.png"  # Изображение для состояния наведения
#            action Jump("choice_death")  # Действие при нажатии
#            xpos 100  # Позиция по X
#            ypos 100  # Позиция по Y
 
            
    #Герой: 
    "Почему я не помню ничего? Где мы находимся?"

    #Незнакомка: 
    e "Мы в безопасном месте. Здесь вы сможете восстановить свои воспоминания."

    #Герой: 
    "А как я сюда попал?"

    #Незнакомка: 
    e "Вы были ранены. Я нашла вас в лесу и привела сюда."

    #Герой: 
    "Но почему я ничего не помню о том, как оказался в лесу?"

    #Незнакомка: 
    e "Иногда память блокирует травмирующие события. Это защитный механизм."

    #Сцена 2. Первые шаги
    #Герой пытается встать, но Незнакомка помогает ему.

    #Герой: 
    "Почему у меня такое чувство, что вы что-то скрываете?"

    #Незнакомка: 
    e "Просто ваше состояние нестабильно. Память возвращается постепенно."

    #Герой: 
    "А что за деревня? Почему она такая заброшенная?"

    #Незнакомка: 
    e "Это старая деревня. Многие уехали. Остались только те, кто не может или не хочет покидать родные места."

    #Герой: 
    "А вы? Вы местная?"

    #Незнакомка: 
    e "Можно и так сказать. Я здесь живу уже давно."

    #Герой: 
    "И что, здесь всегда так тихо?"

    #Незнакомка: 
    e "Да, здесь всегда спокойно. Это место помогает исцелиться."

    jump bedroom



#Здесь будут концовки:

#Смерть... Странный выбор...

label choice_death:

    scene doctors

    pause (2)

    "Что... происходит..."

    jump titles

#Конец игры!

label titles:

    scene black

    pause (5)

    return