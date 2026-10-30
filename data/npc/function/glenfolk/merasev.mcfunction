execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Merasev","color":"aqua"},{"text":"> I hope the","color":"white"},{"text":" Sanctum of Petals","color":"light_purple"},{"text":" is safe to enter again soon, it used to be so beautiful. Especially the prized Monarch Rose, what a flower!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
