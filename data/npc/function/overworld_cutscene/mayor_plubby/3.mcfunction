#start facing at you
setblock 10385 55 -221 redstone_block

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> You again? Why am I not surprised.","color":"white"},{"text":" ⇒","color":"light_purple"}]


schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/4 5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
