execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> Oh... I loathe this memory. It is the skull of an Orc child I found beside the road many years ago. He had fallen and died alone before anyone could find him. This image haunted me until I buried it deep within the cellars of my mind, but I accept that the time has come for me to confront it.","color":"white"}]

scoreboard players set wm_memory3 bool 1
execute if score wm_memory1 bool matches 1 if score wm_memory2 bool matches 1 if score wm_memory3 bool matches 1 if score wm_memory4 bool matches 1 as @a[tag=mg.flw] at @s run tellraw @s [{"text":" And with that, my four lost memories have been regained. It's time to go for a swim, hero.","color":"white"}]
