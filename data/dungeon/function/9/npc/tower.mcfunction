execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> Oho! I was worried that this would be the most dreadful memory of them all, but I'm pleased to see that's not the case. This is a knight costume my mother made me! I would spend afternoons in it, pretending I was a mighty hero. I dreamed of becoming one for real, though that dream faded with time.","color":"white"}]

scoreboard players set wm_memory4 bool 1
execute if score wm_memory1 bool matches 1 if score wm_memory2 bool matches 1 if score wm_memory3 bool matches 1 if score wm_memory4 bool matches 1 as @a[tag=mg.flw] at @s run tellraw @s [{"text":" And with that, my four lost memories have been regained. It's time to go for a swim, hero.","color":"white"}]
