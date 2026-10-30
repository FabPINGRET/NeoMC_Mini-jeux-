clone -9864 114 553 -9864 114 553 -9864 109 553
particle instant_effect{color:[0.000,1.000,1.000]} -9864 109.5 553 0.3 0.3 0.3 1 200 normal
playsound minecraft:entity.lightning_bolt.thunder master @a[tag=mg.flw] -9864 109 553 2 1

spawnpoint @a[tag=mg.flw] -9864 109 557 0 0
scoreboard players set $flsp mg.st 39

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
