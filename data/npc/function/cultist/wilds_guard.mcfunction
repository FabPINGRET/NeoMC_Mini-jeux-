execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> On ","color":"white"},{"text":"Lord Morbex's","color":"dark_aqua"},{"text":" command, no one else is allowed to or from the ","color":"white"},{"text":"Dark Wilds","color":"dark_purple"},{"text":" except for Germ Eaters! The rabble here have stirred up enough trouble and we don't want them interfering with our grand plan there...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
