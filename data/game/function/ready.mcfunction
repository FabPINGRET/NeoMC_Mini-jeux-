execute if score mainstory Story matches -1 positioned 1274 209 212 run tag @p[tag=mg.flw] add ready
execute if score mainstory Story matches -1 if entity @a[tag=!ready,tag=mg.flw] positioned 1274 209 212 run tellraw @a[tag=mg.flw] [{"selector":"@p[tag=mg.flw]","color":"aqua"},{"text":" is ready!","color":"white"}]
execute if score mainstory Story matches -1 unless entity @a[tag=!ready,tag=mg.flw] run setblock 1278 197 218 minecraft:redstone_block

execute unless score mainstory Story matches -1 positioned 1274 209 212 as @p[tag=mg.flw] run function game:join
