execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kovács János","color":"dark_purple"},{"text":"> I have been this realm's ","color":"white"},{"text":"Custodian of the Spheres","color":"light_purple"},{"text":" for ten-thousand years. I've done my duties with honor and I have earned my retirement.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute positioned 10319 35 -103 run kill @e[type=snowball,tag=boss_marker,distance=..3]

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
function music:end
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/custodian/1 10s

fill 10318 35 -104 10318 35 -103 air

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
