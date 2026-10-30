execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mama Roach","color":"green"},{"text":"> Cut my life into pieces! Haha just kiddin.","color":"white"},{"text":" *cough*","color":"gray","italic":true},{"text":" Hope you're having a good adventure.","color":"white","italic":false}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
