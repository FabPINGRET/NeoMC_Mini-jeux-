execute if score @s mg.olfur matches 1.. run return run tellraw @s {"text":"Tu as déjà une cape de fourrure.","color":"yellow"}
execute unless score @s mg.olm1 matches 5.. run return run tellraw @s {"text":"Il faut 5 peaux de bête.","color":"red"}
scoreboard players remove @s mg.olm1 5
scoreboard players set @s mg.olfur 1
tellraw @s {"text":"🧥 Cape de fourrure : tu ne crains plus le froid de Givrecroc.","color":"aqua"}
