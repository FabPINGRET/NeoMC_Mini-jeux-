execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Eye in the Grove","color":"gold"},{"text":"> Why","color":"white","italic":false},{"text":"yyyy","color":"gray","italic":true},{"text":" do you assume cr","color":"white","italic":false},{"text":"eeee","color":"gray","italic":true},{"text":"py things that watch you in the dark want to hu","color":"white","italic":false},{"text":"rrrrrr","color":"gray","italic":true},{"text":"t you? We just want bo","color":"white","italic":false},{"text":"tttthhhhh","color":"gray","italic":true},{"text":" your e","color":"white","italic":false},{"text":"yyyyy","color":"gray","italic":true},{"text":"es...","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute positioned -32 57 -189 run kill @e[type=snowball,tag=boss_marker,distance=..3]

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
function music:end
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/eye_in_the_grove/1 8s

fill -31 57 -189 -32 57 -190 air

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
