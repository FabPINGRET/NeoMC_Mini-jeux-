# 🙈 Labyrinthe aveugle — tick
scoreboard players add $lbt mg.st 1
execute store result bossbar mg:lab value run scoreboard players get $lbt mg.st
execute if score $state mg.st matches 2 as @a[tag=mg.lbw,tag=mg.play] at @s if block ~ ~-0.5 ~ minecraft:gold_block run return run function mg:lab/win
execute if score $state mg.st matches 2 if score $lbt mg.st matches 4800.. run function mg:lab/timeout
