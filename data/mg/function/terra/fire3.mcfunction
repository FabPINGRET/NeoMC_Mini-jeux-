# @s tire (fusil Mk2) : +90 de chaleur, surchauffe à 1000
execute if entity @s[tag=mg.tvoh] run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.6
execute if score @s mg.tvcd matches 1.. run return 0
scoreboard players set @s mg.tvcd 3
scoreboard players add @s mg.tvh 90
execute if score @s mg.trcl matches 1 run scoreboard players remove @s mg.tvh 27
execute if score @s mg.tvh matches 1000.. run function mg:terra/overheat
playsound minecraft:entity.breeze.shoot player @a ~ ~ ~ 0.7 1.6
scoreboard players set $tvr mg.st 0
tag @s add mg.tvsh
execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/ray3
tag @s remove mg.tvsh
tag @e[tag=mg.tvhitn] remove mg.tvhitn
