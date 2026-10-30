execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run advancement grant @a[distance=..10,tag=mg.flw] only sidequest:wizerm_start

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wizerm","color":"aqua"},{"text":"> How wonderful, a familiar face! A little while ago I accidentally exploded my tower to this dimension while experimenting with some mud. It is apparent you found your way here as well. My","color":"white"},{"text":" apprentice ","color":"green"},{"text":"is working on ","color":"white"},{"text":"interesting things in the basement","color":"aqua"},{"text":" if you want to go meet him. He's an eager lad!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

return 1
