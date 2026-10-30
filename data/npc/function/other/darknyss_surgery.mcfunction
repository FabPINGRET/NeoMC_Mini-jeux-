execute positioned -409 42 132 if entity @p[gamemode=!spectator,tag=darknyss,tag=mg.flw] run tag @p[gamemode=!spectator,tag=mg.flw] add undoing_darknyss_surgery
execute positioned -409 42 132 if entity @p[gamemode=!spectator,tag=!darknyss,tag=mg.flw] run tag @p[gamemode=!spectator,tag=mg.flw] add darknyss_surgery

advancement grant @p[tag=darknyss_surgery,tag=!darknyss,tag=mg.flw] only sidequest_2:npc_darknyss
tag @p[tag=darknyss_surgery,tag=!darknyss,tag=mg.flw] add upgrade_darknyss
execute as @a[tag=mg.flw] run function game:100_check

playsound minecraft:item.shears.snip master @p[tag=darknyss_surgery,tag=!darknyss,tag=mg.flw] ~ ~ ~ 1 1 1
playsound minecraft:item.shears.snip master @p[tag=darknyss_surgery,tag=!darknyss,tag=mg.flw] ~ ~ ~ 1 0.5 1
playsound minecraft:item.shears.snip master @p[tag=darknyss_surgery,tag=!darknyss,tag=mg.flw] ~ ~ ~ 1 2 1

playsound minecraft:item.shears.snip master @p[tag=undoing_darknyss_surgery,tag=darknyss,tag=mg.flw] ~ ~ ~ 1 1 1
playsound minecraft:item.shears.snip master @p[tag=undoing_darknyss_surgery,tag=darknyss,tag=mg.flw] ~ ~ ~ 1 0.5 1
playsound minecraft:item.shears.snip master @p[tag=undoing_darknyss_surgery,tag=darknyss,tag=mg.flw] ~ ~ ~ 1 2 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @p[tag=darknyss_surgery,tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @p[tag=undoing_darknyss_surgery,tag=mg.flw] ~ ~ ~ 1 0.8

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @p[tag=darknyss_surgery,tag=!darknyss,tag=mg.flw] [{"text":"<"},{"text":"Darknyss Pierre","color":"aqua"},{"text":"> Those tendons have GOT to go. These connect-y bits? I'll just unconnect them. A little snip here, a little snip there, and done! Your legs just got wayyy better. You should now be able to ","color":"white"},{"text":"walk up blocks as if they were stairs","color":"light_purple"},{"text":". It just helps to get around without having to jump so much.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @p[tag=undoing_darknyss_surgery,tag=darknyss,tag=mg.flw] [{"text":"<"},{"text":"Darknyss Pierre","color":"aqua"},{"text":"> Ah, you want your connect-y bits reconnected? Nothing a staple gun can't fix! Aaaaand done, your legs should be ","color":"white"},{"text":"back to normal","color":"light_purple"},{"text":" now. I hope my practice on farm animals paid off!","color":"white"}]

attribute @p[tag=darknyss_surgery,tag=!darknyss,tag=mg.flw] minecraft:step_height base set 1
attribute @p[tag=undoing_darknyss_surgery,tag=darknyss,tag=mg.flw] minecraft:step_height base reset

tag @a[tag=darknyss_surgery,tag=mg.flw] add darknyss
tag @a[tag=undoing_darknyss_surgery,tag=mg.flw] remove darknyss

tag @a[tag=mg.flw] remove undoing_darknyss_surgery
tag @a[tag=mg.flw] remove darknyss_surgery

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
