# @s a vaincu une élite : butin (or, matériaux de la région, gemme, poussière de lune)
advancement revoke @s only mg:ombre/k/elite
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olel 1
scoreboard players operation $c mg.st = @s mg.olrg
scoreboard players add $c mg.st 1
scoreboard players operation $c mg.st *= #40 mg.st
scoreboard players operation @s mg.olg += $c mg.st
tellraw @s [{"text":"📦 Butin d'élite : +","color":"gold"},{"score":{"name":"$c","objective":"mg.st"},"color":"yellow"},{"text":" 💰","color":"yellow"}]
function mg:ombre/mat_region {n:3}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..25 run scoreboard players add @s mg.olsp 1
execute if score $r mg.st matches ..25 run tellraw @s {"text":"  💎 Gemme de lune : +1 point de caractéristique !","color":"light_purple"}
execute if score $r mg.st matches 90.. run scoreboard players add @s mg.olm9 1
execute if score $r mg.st matches 90.. run tellraw @s {"text":"  ✦ +1 poussière de lune (rare)","color":"light_purple"}
function mg:ombre/xp {n:60}
execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 0.7 1.2
