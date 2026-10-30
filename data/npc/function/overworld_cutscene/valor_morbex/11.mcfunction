setblock 10018 91 -105 minecraft:redstone_block

data modify entity @n[tag=slime_man_valor_tower_1,distance=0..] Pose set value {}

execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> Ah, I can see by the lack of a twinkle in your eye that you’re not amazed by me yet.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/12 9s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
