tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Mind Nexus","color":"dark_aqua"},{"text":"> Invader! I can smell your brain waves like a foul stench beneath your mask. Open yourself to my influence and I will scour you.","color":"white"},{"text":" ⇒","color":"light_purple"}]

setblock 10072 40 -105 minecraft:sea_lantern

execute positioned 10071 42 -104 run kill @n[tag=boss_marker,distance=..3]

function music:end
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/mind_contagion/1 9s
fill 10072 41 -105 10071 41 -105 air

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
