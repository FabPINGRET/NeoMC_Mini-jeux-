execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"O - PEN - SE - SA - ME!","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

fill 10467 58 117 10469 60 117 air
playsound minecraft:zelda.secret master @a[tag=mg.flw] 10468 59 117 1 1 1

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/13 4s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
