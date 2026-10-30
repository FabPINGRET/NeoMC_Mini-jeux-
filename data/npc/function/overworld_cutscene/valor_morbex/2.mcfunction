execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> I had expected more from the","color":"white","bold":false},{"text":" Bell","color":"gold"},{"text":" than merely sending a mortal to defend it... but here we are.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/3 8s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
