execute positioned 10670 77 -84 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> Can you believe these weaklings serve a god of Forgetting? Hah! It will be easy to convince them to worship me instead.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute positioned 10670 79 -84 run kill @e[type=snowball,tag=boss_marker,distance=..3]

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
function music:end
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/memory_contagion/1 10s

fill 10671 78 -84 10671 78 -83 air

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
