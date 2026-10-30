execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I honestly tried really hard to find the lost Pygmy, I thought this was going to be my big heroic break! Not that I'm not already a real superhero or anything.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/8 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
