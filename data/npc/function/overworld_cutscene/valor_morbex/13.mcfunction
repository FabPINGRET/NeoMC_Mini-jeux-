execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I'm just late because I was ","color":"white"},{"text":"unlocking the Ember Depot","color":"red"},{"text":" with a key that I found a monster holding. The ","color":"white"},{"text":"Lord of Flame ","color":"red"},{"text":"is imprisoned there, I think.","color":"white"},{"text":" ⇒","color":"light_purple"}]

data modify entity @n[tag=slime_man_valor_tower_1,distance=0..] Pose set value {}

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/14 11s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
