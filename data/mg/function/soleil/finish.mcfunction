# @s franchit la ligne rouge
tag @s add mg.sqf
scoreboard players add $sqn mg.st 1
execute if score $sqn mg.st matches 1 run tag @s add mg.sq1
scoreboard players operation $s mg.st = $sqc mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $s mg.st /= #20 mg.st
tellraw @a[tag=!mg.surv] [{"text":"🏁 #","color":"green"},{"score":{"name":"$sqn","objective":"mg.st"},"color":"green","bold":true},{"text":" ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" franchit la ligne en ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]
effect give @s minecraft:resistance infinite 4 true
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.7 1.2
