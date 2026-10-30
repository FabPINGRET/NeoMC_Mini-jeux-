scoreboard players add forge_level Value 1

execute if score forge_level Value matches 2 run tellraw @a[tag=mg.flw] [{"text":"You feel forges around the Isles sigh in relief as a measure of their power returns to them...","color":"gray","italic":true}]
execute if score forge_level Value matches 3 run tellraw @a[tag=mg.flw] [{"text":"You feel forges around the Isles laugh in exultation as their full power returns to them...","color":"gray","italic":true}]

execute if score forge_level Value matches 3 run advancement grant @a[tag=mg.flw] only sidequest_2:forgemuzzle
execute if score forge_level Value matches 3 run scoreboard players set $fla24 mg.fla 1
execute if score forge_level Value matches 3 run function game:100_check

# LAVA FLOWS
execute if score forge_level Value matches 2 run setblock -9765 240 422 minecraft:redstone_block
execute if score forge_level Value matches 2 run setblock -9765 240 424 minecraft:redstone_block
execute if score forge_level Value matches 2 run setblock -9765 240 426 minecraft:redstone_block

execute if score forge_level Value matches 3 run setblock -9765 240 428 minecraft:redstone_block
execute if score forge_level Value matches 3 run setblock -9765 240 430 minecraft:redstone_block
execute if score forge_level Value matches 3 run setblock -9769 240 416 minecraft:redstone_block
