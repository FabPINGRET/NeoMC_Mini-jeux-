#execute positioned 285 82 1453 at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run playsound minecraft:entity.vex.death neutral @a ~ ~ ~ 1 0.1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Folded Threnodist","color":"dark_purple"},{"text":"> ...","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute positioned 285 82 1453 run kill @e[type=snowball,tag=boss_marker,distance=..3]

fill 284 80 1453 284 80 1452 air

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
function music:end
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/threnodist/1 6s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
