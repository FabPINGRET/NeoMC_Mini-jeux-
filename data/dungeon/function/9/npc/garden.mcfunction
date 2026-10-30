execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> Ah, I remember this flower from my youth. Over a season, I watched it grow, bloom, and finally die. That flower frightened me, so I locked its memory away. My time in bloom has long since passed, and I fear the wilt of death no more. I welcome the memory of that flower once again.","color":"white"}]

scoreboard players set wm_memory1 bool 1
execute if score wm_memory1 bool matches 1 if score wm_memory2 bool matches 1 if score wm_memory3 bool matches 1 if score wm_memory4 bool matches 1 as @a[tag=mg.flw] at @s run tellraw @s [{"text":" And with that, my four lost memories have been regained. Weird that you did this one fourth, but ok! It's time to go for a swim, hero.","color":"white"}]
