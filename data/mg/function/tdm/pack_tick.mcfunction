# Packs de soin (tdm/tick, état 2) : échéance du prochain pack, puis ramassage par un joueur à 1 PV
scoreboard players remove $tmhc mg.st 1
execute if score $tmhc mg.st matches ..0 run function mg:tdm/pack_try
execute as @e[type=minecraft:item_display,tag=mg.tmhk] at @s run function mg:tdm/pack_chk
