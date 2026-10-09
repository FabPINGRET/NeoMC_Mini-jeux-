# @s : on attend que les quilles s'immobilisent (1,25 s mini, 6 s maxi) puis on compte
scoreboard players operation #ln mg.st = @s mg.bln
scoreboard players set #n mg.st 0
execute as @e[type=minecraft:block_display,tag=mg.bpmv] if score @s mg.bln = #ln mg.st run scoreboard players add #n mg.st 1
execute if score @s mg.btm matches 25.. if score #n mg.st matches 0 run return run function mg:bowl/count
execute if score @s mg.btm matches 120.. run function mg:bowl/count
