execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.mainhand minecraft:crossbow[!minecraft:custom_data={ice_cannon:1b}] run tag @s add crossbow_upgrade

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!crossbow_upgrade,tag=mg.flw] [{"text":"<"},{"text":"Dastardly Willy","color":"aqua"},{"text":"> I've been charged with developing cannons to protect the Abscondence. As a part of my research, I created a powerful ","color":"white"},{"text":"crossbow variant","color":"aqua"},{"text":" I'd be happy to share with you. If you bring me a ","color":"white"},{"text":"crossbow","color":"aqua"},{"text":", I can upgrade it, no problem.","color":"white"}]

advancement grant @a[tag=crossbow_upgrade,tag=mg.flw] only sidequest_2:npc_willy
tag @a[tag=crossbow_upgrade,tag=mg.flw] add upgrade_willy

execute as @a[tag=mg.flw] run function game:100_check

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=crossbow_upgrade,tag=mg.flw] [{"text":"<"},{"text":"Dastardly Willy","color":"aqua"},{"text":"> Let me take a crack at that crossbow for ya. And... all set! Your crossbow is now an ","color":"white"},{"text":"Ice Cannon","color":"aqua"},{"text":"! Load it with normal arrows and the Cannon will make them ","color":"white"},{"text":"explosive","color":"aqua"},{"text":". Monsters will still take damage if you hit the ground or a wall near them.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:zelda.itemget master @a[tag=crossbow_upgrade,tag=mg.flw] ~ ~ ~ 1 1

item replace entity @a[tag=crossbow_upgrade,tag=mg.flw] weapon.mainhand from block -62 93 -287 container.0
execute as @a[tag=crossbow_upgrade,tag=mg.flw] at @s run particle dust_pillar{block_state:"minecraft:packed_ice"} ~ ~ ~ 0.3 0 0.3 0 50 normal

tag @a[tag=mg.flw] remove crossbow_upgrade

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
