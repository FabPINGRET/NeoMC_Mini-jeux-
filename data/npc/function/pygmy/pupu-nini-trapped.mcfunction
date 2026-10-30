execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Please, help me! Get ","color":"white"},{"text":"everyone over here first","color":"green"},{"text":"...","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Please, help me! I sneaked through the ","color":"white"},{"text":"Worldgate","color":"yellow"},{"text":" when you opened it, and a horrible man who smelled like pumpkins kidnapped me! You have to get me out of here!","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] run tag @a[tag=mg.flw] add no_warp
execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] run scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] run stopsound @a[tag=mg.flw] record
#lock door
execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] run setblock 214 40 122 minecraft:redstone_block
#remove button
execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] run fill 214 43 112 214 43 113 air
execute positioned 214 43 112 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] run schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/0 7s

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
