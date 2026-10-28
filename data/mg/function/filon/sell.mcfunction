# 💰 @s vend tout ce qui est vendable dans son inventaire, au cours du moment (Σ nombre × base en dixièmes × cours % ÷ 1000)
scoreboard players set #tot mg.st 0
execute store result score #n mg.st run clear @s minecraft:cobblestone
scoreboard players operation #n mg.st *= #fb0 mg.st
scoreboard players operation #n mg.st *= $fm0 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:cobbled_deepslate
scoreboard players operation #n mg.st *= #fb1 mg.st
scoreboard players operation #n mg.st *= $fm1 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:andesite
scoreboard players operation #n mg.st *= #fb2 mg.st
scoreboard players operation #n mg.st *= $fm2 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:diorite
scoreboard players operation #n mg.st *= #fb3 mg.st
scoreboard players operation #n mg.st *= $fm3 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:granite
scoreboard players operation #n mg.st *= #fb4 mg.st
scoreboard players operation #n mg.st *= $fm4 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:tuff
scoreboard players operation #n mg.st *= #fb5 mg.st
scoreboard players operation #n mg.st *= $fm5 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:gravel
scoreboard players operation #n mg.st *= #fb6 mg.st
scoreboard players operation #n mg.st *= $fm6 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:flint
scoreboard players operation #n mg.st *= #fb7 mg.st
scoreboard players operation #n mg.st *= $fm7 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:calcite
scoreboard players operation #n mg.st *= #fb8 mg.st
scoreboard players operation #n mg.st *= $fm8 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:smooth_basalt
scoreboard players operation #n mg.st *= #fb9 mg.st
scoreboard players operation #n mg.st *= $fm9 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:coal
scoreboard players operation #n mg.st *= #fb10 mg.st
scoreboard players operation #n mg.st *= $fm10 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:raw_copper
scoreboard players operation #n mg.st *= #fb11 mg.st
scoreboard players operation #n mg.st *= $fm11 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:raw_iron
scoreboard players operation #n mg.st *= #fb12 mg.st
scoreboard players operation #n mg.st *= $fm12 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:raw_gold
scoreboard players operation #n mg.st *= #fb13 mg.st
scoreboard players operation #n mg.st *= $fm13 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:redstone
scoreboard players operation #n mg.st *= #fb14 mg.st
scoreboard players operation #n mg.st *= $fm14 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:lapis_lazuli
scoreboard players operation #n mg.st *= #fb15 mg.st
scoreboard players operation #n mg.st *= $fm15 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:diamond
scoreboard players operation #n mg.st *= #fb16 mg.st
scoreboard players operation #n mg.st *= $fm16 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:emerald
scoreboard players operation #n mg.st *= #fb17 mg.st
scoreboard players operation #n mg.st *= $fm17 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:amethyst_shard
scoreboard players operation #n mg.st *= #fb18 mg.st
scoreboard players operation #n mg.st *= $fm18 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:amethyst_block
scoreboard players operation #n mg.st *= #fb19 mg.st
scoreboard players operation #n mg.st *= $fm19 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:raw_gold_block
scoreboard players operation #n mg.st *= #fb20 mg.st
scoreboard players operation #n mg.st *= $fm20 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:raw_iron_block
scoreboard players operation #n mg.st *= #fb21 mg.st
scoreboard players operation #n mg.st *= $fm21 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:ancient_debris
scoreboard players operation #n mg.st *= #fb22 mg.st
scoreboard players operation #n mg.st *= $fm22 mg.st
scoreboard players operation #tot mg.st += #n mg.st
execute store result score #n mg.st run clear @s minecraft:gold_nugget[minecraft:custom_data~{fn_lucky:1b}]
scoreboard players operation #n mg.st *= #fb23 mg.st
scoreboard players operation #n mg.st *= $fm23 mg.st
scoreboard players operation #tot mg.st += #n mg.st
scoreboard players operation #tot mg.st /= #fn1000 mg.st
execute if score #tot mg.st matches ..0 run return run tellraw @s {"text":"Rien à vendre : va miner ! ⛏","color":"gray"}
scoreboard players operation @s mg.fnp += #tot mg.st
scoreboard players operation @s mg.fns += #tot mg.st
tellraw @s [{"text":"💰 Vendu pour ","color":"gold"},{"score":{"name":"#tot","objective":"mg.st"},"color":"yellow","bold":true},{"text":" pts. Solde : ","color":"gold"},{"score":{"name":"@s","objective":"mg.fnp"},"color":"yellow"},{"text":" — saison : ","color":"gray"},{"score":{"name":"@s","objective":"mg.fns"},"color":"gray"}]
execute if score #tot mg.st matches 1000.. run tellraw @a[tag=mg.fnw] [{"text":"💎 ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" vient de vendre pour ","color":"gray"},{"score":{"name":"#tot","objective":"mg.st"},"color":"aqua","bold":true},{"text":" pts !","color":"gray"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1.1
execute at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.4
