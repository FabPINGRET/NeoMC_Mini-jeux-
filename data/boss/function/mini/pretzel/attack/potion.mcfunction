spreadplayers -10340 446 3 12 false @e[tag=pretzel_rand,distance=0..]
execute as @e[tag=pretzel_rand,sort=random,limit=3,distance=0..] at @s unless block ~ 87 ~ air run tag @s add pretzel_potioning
execute as @e[tag=pretzel_potioning,distance=0..] at @s positioned ~ 108 ~ run summon lingering_potion ~ ~ ~ {Tags:["pretzel_potion"],Item:{id:"minecraft:lingering_potion",count:1,components:{"minecraft:potion_contents":{potion:"minecraft:harming"}}}}

execute as @e[tag=pretzel_potioning,distance=0..] at @s run playsound minecraft:entity.experience_orb.pickup hostile @a[tag=mg.flw] ~ 88 ~ 1 0.8

execute as @e[tag=pretzel_potioning,distance=0..] at @s run particle minecraft:dust_pillar{block_state:"pink_terracotta"} ~ 88 ~ 0.3 0 0.3 0.1 30
tag @e[tag=pretzel_rand,distance=0..] remove pretzel_potioning

schedule function floaty:sched/boss/mini/pretzel/schedule_attack 3s
