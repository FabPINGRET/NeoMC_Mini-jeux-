execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Fumblefoot","color":"green"},{"text":"> Gruh bogogo bug gub. GUHHHHH GRUD ","color":"white"},{"text":"Slime Man","color":"green"},{"text":" buhhhhhh.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Fumblefoot","color":"green"},{"text":"> We Orcs hold the Glooblins of ","color":"white"},{"text":"Moldsap Woods","color":"light_purple"},{"text":" in high regard. They possess a commendable sense of community. The one known as","color":"white"},{"text":" Slime Man ","color":"green"},{"text":"is... intriguing.","color":"white"}]

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
