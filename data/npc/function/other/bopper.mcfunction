execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.fox.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute unless block -11546 205 -336 chest at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bopper","color":"red"},{"text":"> Ohhh my teddy... My teddy came alive and tried to kill me with magic! I left him in the","color":"white"},{"text":" hidden woods","color":"green"},{"text":", but I miss him so! If only teddy wasn't alive anymore...","color":"white"}]
execute if block -11546 205 -336 chest at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bopper","color":"red"},{"text":"> I'm so happy you aren't alive anymore, teddy. Please never do that again.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
