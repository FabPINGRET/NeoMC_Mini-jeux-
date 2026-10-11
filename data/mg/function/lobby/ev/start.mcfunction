scoreboard players set $evn mg.st 1800
scoreboard players operation $evon mg.st = $evk mg.st
scoreboard players reset $evk mg.st
scoreboard players set $evt mg.st 180
bossbar set mg:ev max 180
bossbar set mg:ev style progress
bossbar set mg:ev players @a[tag=mg.evl]
scoreboard players reset * mg.evd
scoreboard players reset * mg.evc
execute as @a[tag=mg.evl] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1.2
execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_start
execute if score $evon mg.st matches 2 run function mg:lobby/ev/e2_start
execute if score $evon mg.st matches 3 run function mg:lobby/ev/e3_start
