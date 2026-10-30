execute positioned 9953 39 -52 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 9953 39 -52 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Chantorios","color":"#D47453"},{"text":"> Go!","color":"white"}]

tag @e[tag=simpletoid,distance=0..] add running

#bool (mode)
execute as @e[tag=simpletoid,distance=0..] run scoreboard players set @s bool 1
#Value (speed)
execute as @e[tag=simpletoid,distance=0..] run scoreboard players set @s Value 3

setblock 9955 36 -52 minecraft:redstone_block
scoreboard players set simpletoid_respeed Value 30
