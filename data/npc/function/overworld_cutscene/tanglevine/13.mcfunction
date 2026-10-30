execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Good luck in there! I'm afraid rescuing the ","color":"white"},{"text":"Lord of Forest ","color":"green"},{"text":"won't be as easy as it was to rescue me...","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true}]

execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

setblock 10467 57 121 minecraft:redstone_wire[east=side,north=none,power=0,south=none,west=up]

tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
