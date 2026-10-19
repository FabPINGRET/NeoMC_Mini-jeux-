# @s rend son contrat : récompense selon la région de l'espèce
scoreboard players set $g mg.st 0
execute if score @s mg.olct matches 1 run scoreboard players set $g mg.st 1
execute if score @s mg.olct matches 2 run scoreboard players set $g mg.st 1
execute if score @s mg.olct matches 3 run scoreboard players set $g mg.st 1
execute if score @s mg.olct matches 4 run scoreboard players set $g mg.st 1
execute if score @s mg.olct matches 5 run scoreboard players set $g mg.st 1
execute if score @s mg.olct matches 6 run scoreboard players set $g mg.st 2
execute if score @s mg.olct matches 7 run scoreboard players set $g mg.st 2
execute if score @s mg.olct matches 8 run scoreboard players set $g mg.st 2
execute if score @s mg.olct matches 9 run scoreboard players set $g mg.st 2
execute if score @s mg.olct matches 10 run scoreboard players set $g mg.st 2
execute if score @s mg.olct matches 11 run scoreboard players set $g mg.st 3
execute if score @s mg.olct matches 12 run scoreboard players set $g mg.st 3
execute if score @s mg.olct matches 13 run scoreboard players set $g mg.st 3
execute if score @s mg.olct matches 14 run scoreboard players set $g mg.st 3
execute if score @s mg.olct matches 15 run scoreboard players set $g mg.st 4
execute if score @s mg.olct matches 16 run scoreboard players set $g mg.st 4
execute if score @s mg.olct matches 17 run scoreboard players set $g mg.st 4
execute if score @s mg.olct matches 18 run scoreboard players set $g mg.st 4
execute if score @s mg.olct matches 19 run scoreboard players set $g mg.st 4
execute if score @s mg.olct matches 20 run scoreboard players set $g mg.st 5
execute if score @s mg.olct matches 21 run scoreboard players set $g mg.st 5
execute if score @s mg.olct matches 22 run scoreboard players set $g mg.st 5
execute if score @s mg.olct matches 23 run scoreboard players set $g mg.st 5
execute if score @s mg.olct matches 24 run scoreboard players set $g mg.st 5
execute if score @s mg.olct matches 25 run scoreboard players set $g mg.st 6
execute if score @s mg.olct matches 26 run scoreboard players set $g mg.st 6
execute if score @s mg.olct matches 27 run scoreboard players set $g mg.st 6
execute if score @s mg.olct matches 28 run scoreboard players set $g mg.st 6
execute if score @s mg.olct matches 29 run scoreboard players set $g mg.st 6
execute if score @s mg.olct matches 30 run scoreboard players set $g mg.st 7
execute if score @s mg.olct matches 31 run scoreboard players set $g mg.st 7
execute if score @s mg.olct matches 32 run scoreboard players set $g mg.st 7
execute if score @s mg.olct matches 33 run scoreboard players set $g mg.st 7
execute if score @s mg.olct matches 34 run scoreboard players set $g mg.st 7
execute if score @s mg.olct matches 35 run scoreboard players set $g mg.st 8
execute if score @s mg.olct matches 36 run scoreboard players set $g mg.st 8
execute if score @s mg.olct matches 37 run scoreboard players set $g mg.st 8
execute if score @s mg.olct matches 38 run scoreboard players set $g mg.st 8
execute if score @s mg.olct matches 39 run scoreboard players set $g mg.st 8
scoreboard players operation $c mg.st = $g mg.st
scoreboard players operation $c mg.st *= #100 mg.st
scoreboard players add $c mg.st 60
scoreboard players operation @s mg.olg += $c mg.st
scoreboard players operation $x mg.st = $c mg.st
scoreboard players operation $x mg.st *= #2 mg.st
execute store result storage mg:ombre s.n int 1 run scoreboard players get $x mg.st
function mg:ombre/xpm with storage mg:ombre s
tellraw @s [{"text":"📋 Contrat rempli : +","color":"green"},{"score":{"name":"$c","objective":"mg.st"},"color":"gold","bold":true},{"text":" 💰","color":"gold"}]
scoreboard players set @s mg.olct 0
scoreboard players add @s mg.olcd 1
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.2
