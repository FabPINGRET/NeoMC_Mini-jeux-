execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Iaygrin-Vo","color":"light_purple"},{"text":"> Limbohold is safer than the true dimensions. It's a twisty place, but we're protected here. If the Floaty Isles don't make it through this, we'll bend our way into another dimension and find a new home.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
