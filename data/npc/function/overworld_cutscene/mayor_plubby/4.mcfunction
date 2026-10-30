execute positioned 10383 59 -222 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10383 59 -222 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Plubby","color":"light_purple"},{"text":"> Interesting, you two know each other already? I think this hero from the","color":"white"},{"text":" Floaty Isles","color":"gold"},{"text":" wanted to help us rescue the ","color":"white"},{"text":"Lord of Spores","color":"light_purple"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]


schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/5 8s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
