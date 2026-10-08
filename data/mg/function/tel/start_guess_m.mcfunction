$tp @s $(x).5 65 $(vz).5 0 20
gamemode adventure @s
give @s minecraft:writable_book[custom_name=[{"text":"📞 Écris ici (1re page)","color":"gold","italic":false}]]
title @s title {"text":"🔍 Qu'est-ce que c'est ?","color":"aqua","bold":true}
title @s subtitle {"text":"Fais le tour, écris ta réponse dans le livre, puis Valider","color":"gray"}
tellraw @s [{"text":"\n🔍 Devine ce que représente cette construction ","color":"aqua","bold":true},{"text":"(1re page du livre, puis « Terminé »). 60 s.","color":"gray"}]
tellraw @s ["",{"text":" [✔ Valider]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger mg.tel set 1"},"hover_event":{"action":"show_text","value":"Écris sur la 1re page du livre, clique « Terminé », puis valide"}}]
