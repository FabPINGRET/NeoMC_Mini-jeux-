execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> I am ","color":"white","bold":false},{"text":"Lord Morbex","color":"dark_aqua"},{"text":", emissary of the ","color":"white"},{"text":"World Virus","color":"dark_aqua","bold":true},{"text":". Our infection of the ","color":"white","bold":false},{"text":"Bell of Life","color":"gold"},{"text":" in the Floaty Isles has finally begun.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/2 11s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
