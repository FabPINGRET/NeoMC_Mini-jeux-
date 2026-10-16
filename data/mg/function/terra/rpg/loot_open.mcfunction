# Un butin d'élite : récompense tirée au sort selon la zone (×1 à ×3)
scoreboard players add @s mg.trel 1
execute store result score $r mg.st run random value 1..100
scoreboard players operation $c mg.st = @s mg.trrg
scoreboard players add $c mg.st 1
scoreboard players set #60 mg.st 60
scoreboard players operation $c mg.st *= #60 mg.st
scoreboard players operation @s mg.tvc += $c mg.st
tellraw @s [{"text":"📦 Butin d'élite : +","color":"gold"},{"score":{"name":"$c","objective":"mg.st"},"color":"yellow"},{"text":" ₵","color":"yellow"}]
execute if score $r mg.st matches 1..30 run scoreboard players add @s mg.trgr 3
execute if score $r mg.st matches 1..30 run tellraw @s {"text":"  +3 griffes","color":"gray"}
execute if score $r mg.st matches 31..50 run scoreboard players add @s mg.trvn 2
execute if score $r mg.st matches 31..50 run tellraw @s {"text":"  +2 glandes à venin","color":"gray"}
execute if score $r mg.st matches 51..65 run scoreboard players add @s mg.trai 2
execute if score $r mg.st matches 51..65 run tellraw @s {"text":"  +2 ailes","color":"gray"}
execute if score $r mg.st matches 66..75 run scoreboard players add @s mg.trdn 2
execute if score $r mg.st matches 66..75 run tellraw @s {"text":"  +2 dents","color":"gray"}
execute if score $r mg.st matches 76..80 run scoreboard players add @s mg.trec 1
execute if score $r mg.st matches 76..80 run tellraw @s {"text":"  +1 écaille de spinosaure (rare !)","color":"dark_aqua"}
function mg:terra/rpg/xp {n:80}
execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 0.7 1.2
scoreboard players remove $n mg.st 1
execute if score $n mg.st matches 1.. run function mg:terra/rpg/loot_open
