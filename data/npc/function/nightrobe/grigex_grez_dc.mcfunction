execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if block -281 50 -175 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grigex-Grez","color":"light_purple"},{"text":"> That structure there! The creases in space are focused around it. We can't take any risks hero, space is about to rip open and when it does,","color":"white"},{"text":" kill whatever comes through","color":"light_purple"},{"text":". The ","color":"white"},{"text":"World Virus","color":"dark_aqua"},{"text":"'s attack is about to begin.","color":"white"}]

execute unless block -281 50 -175 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grigex-Grez","color":"light_purple"},{"text":"> The","color":"white"},{"text":" World Virus ","color":"dark_aqua"},{"text":"must be fought from the other side. That's the only way to thwart his attack on the Isles and the ","color":"white"},{"text":"Bell of Life","color":"gold"},{"text":".","color":"white"}]

setblock -281 50 -173 minecraft:redstone_block
execute positioned -278 58 -154 run kill @e[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
