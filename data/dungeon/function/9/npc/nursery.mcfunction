execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> I have not seen this in my mind's eye in many long years. It is the smiling face of my mother when she was young. This is one of the very first memories I ever formed, and how bittersweet it is to remember it now! She lived a beautiful, full life. A kinder Froggadew I have not met.","color":"white"}]

scoreboard players set wm_memory2 bool 1
execute if score wm_memory1 bool matches 1 if score wm_memory2 bool matches 1 if score wm_memory3 bool matches 1 if score wm_memory4 bool matches 1 as @a[tag=mg.flw] at @s run tellraw @s [{"text":" And with that, my four lost memories have been regained. It's time to go for a swim, hero.","color":"white"}]
