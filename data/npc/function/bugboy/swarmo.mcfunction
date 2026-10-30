execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Swarmo","color":"green"},{"text":"> Welcome to our colony, Hero! With everything going on, we found it much safer to live underground. Plus, from here we can tend to the roots of our forest's giant trees! Maybe one day we can return them to their former glory.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
