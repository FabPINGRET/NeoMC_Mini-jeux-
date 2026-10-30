execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Ask the Mayor if you have any questions! I'm going to go work on my final preparations for storming ","color":"white"},{"text":"Sticky Hollow","color":"light_purple"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]


schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/13 8s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
