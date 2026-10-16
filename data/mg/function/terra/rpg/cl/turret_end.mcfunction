scoreboard players operation $own mg.st = @s mg.tvo
execute as @e[tag=mg.trtur] if score @s mg.tvo = $own mg.st run kill @s
particle minecraft:smoke ~ ~0.8 ~ 0.2 0.3 0.2 0.02 15
playsound minecraft:block.chain.break player @a ~ ~ ~ 0.6 1
