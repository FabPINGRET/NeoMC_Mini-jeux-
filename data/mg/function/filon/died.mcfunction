# @s est mort (inventaire gardé) : en PvP, la moitié de ce qu'il n'a pas vendu passe au tueur
scoreboard players reset @s mg.fnd
spawnpoint @s 8 100 45991
tag @s remove mg.fnin
execute unless score $fnpvp mg.st matches 1 run return 0
tag @a remove mg.fnkl
tag @a[tag=mg.fnw,scores={mg.fnk=1..},limit=1] add mg.fnkl
execute unless entity @a[tag=mg.fnkl] run return 0
execute store result score #n mg.st run clear @s minecraft:cobblestone 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:cobblestone"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:cobblestone'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:cobbled_deepslate 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:cobbled_deepslate"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:cobbled_deepslate'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:andesite 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:andesite"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:andesite'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:diorite 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:diorite"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:diorite'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:granite 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:granite"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:granite'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:tuff 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:tuff"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:tuff'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:gravel 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:gravel"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:gravel'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:flint 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:flint"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:flint'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:calcite 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:calcite"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:calcite'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:smooth_basalt 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:smooth_basalt"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:smooth_basalt'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:coal 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:coal"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:coal'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:raw_copper 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:raw_copper"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:raw_copper'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:raw_iron 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:raw_iron"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:raw_iron'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:raw_gold 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:raw_gold"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:raw_gold'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:redstone 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:redstone"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:redstone'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:lapis_lazuli 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:lapis_lazuli"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:lapis_lazuli'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:diamond 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:diamond"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:diamond'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:emerald 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:emerald"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:emerald'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:amethyst_shard 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:amethyst_shard"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:amethyst_shard'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:amethyst_block 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:amethyst_block"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:amethyst_block'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:raw_gold_block 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:raw_gold_block"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:raw_gold_block'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:raw_iron_block 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:raw_iron_block"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:raw_iron_block'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:ancient_debris 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:ancient_debris"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:ancient_debris'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
execute store result score #n mg.st run clear @s minecraft:gold_nugget[minecraft:custom_data~{fn_lucky:1b}] 0
scoreboard players operation #n mg.st /= #fn2 mg.st
execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "minecraft:gold_nugget[minecraft:custom_data~{fn_lucky:1b}]"
execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value 'minecraft:gold_nugget[custom_data={fn_lucky:1b},item_name={"text":"🍀 Pépite de chance","color":"gold"},enchantment_glint_override=true]'
execute if score #n mg.st matches 1.. run function mg:filon/xfer with storage mg:filon x
tellraw @a[tag=mg.fnw] [{"text":"⚔ ","color":"red"},{"selector":"@a[tag=mg.fnkl]","color":"yellow"},{"text":" a détroussé ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" (la moitié de son sac).","color":"gray"}]
tag @a remove mg.fnkl
