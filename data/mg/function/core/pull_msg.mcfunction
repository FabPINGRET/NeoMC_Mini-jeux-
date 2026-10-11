# @s : participant d'une partie lancée par un admin, peut refuser pendant le compte à rebours
tellraw @s [{"text":"🎮 Un admin lance une partie, tu es dedans ! ","color":"gold"},{"text":"[✖ Ne pas rejoindre]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.opt set 60"},"hover_event":{"action":"show_text","value":"Rester où tu étais (survie, Neo GTA, lobby)"}}]
