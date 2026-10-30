#execute positioned -9864 109 553 at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a ~ ~ ~ 1 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Wahrog the Prophet","color":"#44BBFF"},{"text":"> My mind, it is host to","color":"white"},{"text":" crackling parasites","color":"#44BBFF"},{"text":", sucking me down into my own cortices forever! I will never escape the walls of my own skull. The crackling stuffs me inside myself like a rabbit in a bag.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute positioned -9864 109 553 run kill @e[type=snowball,tag=boss_marker,distance=..3]

fill -9863 109 553 -9863 110 553 air

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
function music:end
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/wahrog/1 12s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
