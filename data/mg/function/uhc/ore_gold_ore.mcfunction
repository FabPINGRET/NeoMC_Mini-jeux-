# @s a cassé gold_ore : un bloc de gold_block par minerai
data modify storage mg:uhc o.b set value "gold_block"
execute store result storage mg:uhc o.n int 1 run scoreboard players get @s mg.uog
function mg:uhc/give_n with storage mg:uhc o
scoreboard players reset @s mg.uog
execute at @s run kill @e[type=minecraft:item,distance=..8,nbt={PickupDelay:10s,Item:{id:"minecraft:raw_gold"}}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1.2
