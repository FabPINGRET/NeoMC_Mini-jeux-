execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> That’s embarrassing. I've been planning this righteous coup d'état for weeks!","color":"white"},{"text":" ⇒","color":"light_purple"}]

data modify entity @n[tag=slime_man_valor_tower_1,distance=0..] Pose set value {Head:[30f,0f,0f]}

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/11 7s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
