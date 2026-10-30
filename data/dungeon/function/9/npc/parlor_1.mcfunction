execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> This room, it's a reflection of the real parlor from my childhood home! This furniture layout reminds me there should be a ","color":"white"},{"text":"chest","color":"#44BBFF"},{"text":" here, like when I was a tadpole...","color":"white"}]

execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11109 69 -49 run function summon:intrusive_thought
execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11109 69 -49 run function summon:intrusive_thought

return 1
