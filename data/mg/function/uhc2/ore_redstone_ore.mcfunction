# @s a cassé redstone_ore : un bloc de redstone_block par minerai
data modify storage mg:uhc o.b set value "redstone_block"
execute store result storage mg:uhc o.n int 1 run scoreboard players get @s mg.uor
function mg:uhc2/give_n with storage mg:uhc o
scoreboard players reset @s mg.uor
execute at @s run kill @e[type=minecraft:item,distance=..8,nbt={PickupDelay:10s,Item:{id:"minecraft:redstone"}}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1.2
