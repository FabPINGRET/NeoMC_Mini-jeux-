#execute positioned 10520 43 -168 run playsound minecraft:entity.villager.ambient neutral @a ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> How's it goin, buh'? Hey, are your pockets bulging with... Items???","color":"white"},{"text":" ⇒","color":"light_purple"}]


execute positioned 10520 43 -168 run kill @e[type=snowball,tag=boss_marker,distance=..3]

setblock 10521 42 -168 air
setblock 10520 42 -169 air

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
function music:end
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

schedule function floaty:sched/npc/overworld_cutscene/pretzel/1 8s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
