execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Corr","color":"aqua"},{"text":"> These swords the","color":"white"},{"text":" Bugboys","color":"green"},{"text":" make are expertly crafted. Apparently, they grow them from the roots of a tree. The \"Blade Willow\" they call it. Worth a visit if you're looking for a weapon, we're fresh out.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
