execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> It's Slime. Slime Man. Ugh, ok, this is embarassing. I'm going to go put this puppet back where I found it and find some other hero-ing to do.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/10 9s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
