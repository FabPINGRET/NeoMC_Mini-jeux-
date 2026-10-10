# @s a cassé lapis_ore : un bloc de lapis_block par minerai
data modify storage mg:uhc o.b set value "lapis_block"
execute store result storage mg:uhc o.n int 1 run scoreboard players get @s mg.uol
function mg:uhc2/give_n with storage mg:uhc o
scoreboard players reset @s mg.uol
execute at @s run kill @e[type=minecraft:item,distance=..8,nbt={PickupDelay:10s,Item:{id:"minecraft:lapis_lazuli"}}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1.2
