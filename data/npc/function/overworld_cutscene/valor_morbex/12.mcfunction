stopsound @a[tag=mg.flw] record
function music:slime_man_action

execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> It is I, ","color":"white"},{"text":"Slime Man","color":"green"},{"text":", a real-life superhero, defender of the","color":"white"},{"text":" Dark Isles","color":"dark_purple"},{"text":", in the flesh! Yep, I’m the real deal!","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/13 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
