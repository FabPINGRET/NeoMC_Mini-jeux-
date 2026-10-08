# 🏹 Mini Hunger Games — tick
scoreboard players add $hgt mg.st 1
execute if score $hgt mg.st matches ..199 as @a[tag=mg.play] at @s run tp @s ~ ~ ~
execute if score $hgt mg.st matches ..199 run effect give @a[tag=mg.play] minecraft:slowness 1 9 true
execute if score $hgt mg.st matches 1..199 run function mg:hg/countdown
execute if score $hgt mg.st matches 200 run title @a[tag=mg.play] title {"text":"GO !","color":"green","bold":true}
execute if score $hgt mg.st matches 200 as @a[tag=mg.play] at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 1 1
execute if score $hgt mg.st matches 200 run effect clear @a[tag=mg.play] minecraft:slowness
execute if score $hgt mg.st matches 600 run function mg:hg/pvp
execute if score $hgt mg.st matches 3000 run function mg:hg/chests
execute if score $hgt mg.st matches 3000 run tellraw @a[tag=mg.play] {"text":"🏹 Les coffres ont été remplis !","color":"gold"}
execute if score $hgt mg.st matches 3000 as @a[tag=mg.play] at @s run playsound minecraft:block.chest.open master @s ~ ~ ~ 1 0.8
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..60}] run function mg:core/eliminate
scoreboard players operation $hgq mg.st = $hgt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $hgq mg.st %= #20 mg.st
execute if score $hgq mg.st matches 0 run function mg:hg/second
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run return run function mg:core/win_player
execute if score $state mg.st matches 2 if score $n0 mg.st matches ..1 if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] if score $hgt mg.st matches 6000.. run return run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
