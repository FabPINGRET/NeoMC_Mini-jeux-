# 🟩 Slime Jump — tick
scoreboard players add $sjt mg.st 1
execute store result bossbar mg:slimejump value run scoreboard players get $sjt mg.st
execute as @a[tag=mg.play] at @s if block ~ ~-0.5 ~ minecraft:emerald_block run function mg:slimejump/cp
execute as @a[tag=mg.play] at @s if entity @s[y=-64,dy=138] run function mg:slimejump/fall
execute if score $state mg.st matches 2 as @a[tag=mg.play] at @s if block ~ ~-0.5 ~ minecraft:diamond_block run return run function mg:slimejump/finish
execute if score $state mg.st matches 2 as @a[tag=mg.play] at @s if block ~ ~-0.5 ~ minecraft:gold_block if entity @s[x=-5,y=84,z=37940,dx=6,dy=3,dz=6] run return run function mg:slimejump/finish
execute if score $state mg.st matches 2 if score $sjt mg.st matches 4800.. run function mg:slimejump/timeout
