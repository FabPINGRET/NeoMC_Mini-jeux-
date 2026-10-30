#execute positioned -8 53 1601 run playsound minecraft:entity.creaking.attack neutral @a ~ ~ ~ 1 0.1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Knotfire","color":"green"},{"text":"> You have come to pay me tribute, good. Your body might be a grand gift, or it might be a poor one.","color":"white"},{"text":" ⇒","color":"light_purple"}]


execute positioned -8 55 1601 run kill @e[type=snowball,tag=boss_marker,distance=..3]

fill -8 53 1602 -9 53 1602 air

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
function music:end
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/knotfire/1 9s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
