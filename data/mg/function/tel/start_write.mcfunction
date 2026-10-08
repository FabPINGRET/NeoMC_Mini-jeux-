# @s : écrire un mot
function mg:tel/chain_of
gamemode adventure @s
tp @s 0.5 64 19420.5
give @s minecraft:writable_book[custom_name=[{"text":"📞 Écris ici (1re page)","color":"gold","italic":false}]]
title @s title {"text":"📞 Écris un mot","color":"gold","bold":true}
title @s subtitle {"text":"Livre : 1re page, « Terminé », puis Valider","color":"gray"}
tellraw @s [{"text":"\n📞 Écris un mot ou une petite expression ","color":"gold","bold":true},{"text":"(sur la 1re page du livre, puis « Terminé ») : un autre joueur devra le construire. 60 s.","color":"gray"}]
tellraw @s ["",{"text":" [✔ Valider]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/trigger mg.tel set 1"},"hover_event":{"action":"show_text","value":"Écris sur la 1re page du livre, clique « Terminé », puis valide"}}]
