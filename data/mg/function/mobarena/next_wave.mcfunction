# Mob Arena — lance la vague suivante
scoreboard players add $wv mg.st 1
scoreboard players set $wt mg.st 0
scoreboard players set $gl mg.st 0

# Les joueurs tombés reviennent à chaque nouvelle vague
execute as @a[tag=mg.out,tag=!mg.spectate] run function mg:mobarena/revive

# Titre du scoreboard : vague actuelle / total
execute store result storage mg:mw w int 1 run scoreboard players get $wv mg.st
execute store result storage mg:mw m int 1 run scoreboard players get $wmax mg.st
function mg:mobarena/sb_title with storage mg:mw

title @a[tag=!mg.surv] title [{"text":"Vague ","color":"red","bold":true},{"score":{"name":"$wv","objective":"mg.st"},"color":"red","bold":true}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.4 1.4

tellraw @a [{"text":"\n[Mob Arena] ","color":"dark_green","bold":true},{"text":"⚔ VAGUE ","color":"red","bold":true},{"score":{"name":"$wv","objective":"mg.st"},"color":"red","bold":true},{"text":" / ","color":"red"},{"score":{"name":"$wmax","objective":"mg.st"},"color":"red"}]
scoreboard players set $ml mg.st 99
execute store result storage mg:mw w int 1 run scoreboard players get $wv mg.st
function mg:mobarena/wave with storage mg:mw
function mg:mobarena/scale

# ULTRA HARD : tous les monstres de la vague sont plus rapides, plus forts et plus résistants
execute if score $mt mg.st matches 3 run effect give @e[tag=mg.mob] minecraft:speed infinite 1 true
execute if score $mt mg.st matches 3 run effect give @e[tag=mg.mob] minecraft:strength infinite 1 true
execute if score $mt mg.st matches 3 run effect give @e[tag=mg.mob] minecraft:resistance infinite 1 true
