# @s (slasher) bondit sur le colon le plus proche
scoreboard players set @s mg.tvat 8
execute facing entity @p[tag=mg.tvw,gamemode=adventure] feet rotated ~ -16 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.0}
function mg:terra/push
playsound minecraft:entity.fox.screech hostile @a ~ ~ ~ 1 1.3
