# Départ du parkour (@s = joueur sur le plot de départ)
execute if entity @s[tag=mg.pkr] if score @s mg.ppt matches -1 run return 0
tag @s add mg.pkr
scoreboard players set @s mg.ppc 0
scoreboard players set @s mg.ppt -1
scoreboard players set @s mg.ppf 0
function mg:core/heal
tellraw @s [{"text":"✦ PARKOUR : ","color":"green","bold":true},{"text":"saute jusqu'au bloc diamant ! Le chrono démarre quand tu quittes le plot. 3 checkpoints (blocs de lapis) ; si tu tombes, tu reviens au dernier. Retour au lobby : ","color":"gray"},{"text":"[quitter]","color":"red","click_event":{"action":"run_command","command":"trigger mg.opt set 11"},"hover_event":{"action":"show_text","value":"Abandonner le parkour"}}]
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5
