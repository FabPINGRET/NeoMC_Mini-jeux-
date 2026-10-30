execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I always loved the sickly-sweet air down here, but now... it just feels yucky. Anyway, here's the plan: I'm gonna go look for the","color":"white"},{"text":" magic spell","color":"light_purple"},{"text":" rumored to be hidden deep in the hollow, and you can work on replacing","color":"white"},{"text":" four missing track switches ","color":"gold"},{"text":"for the minecart rails in the next room. I'm counting on you, sidekick!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
