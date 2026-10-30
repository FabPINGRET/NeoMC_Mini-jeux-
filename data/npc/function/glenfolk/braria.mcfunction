execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Braria","color":"aqua"},{"text":"> I used to be the librarian of the Great Library until it crumbled to smithereens. The Nightrobes rescued me and have been kind enough to let me tend their archives. My brain is filling up to the brim with forbidden knowledge!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value
