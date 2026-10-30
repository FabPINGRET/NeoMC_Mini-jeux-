setblock 10017 91 -105 air
tp @n[tag=morbex_valor_tower,distance=0..] 10022 90 -98 0 0

function music:end
tag @a[tag=mg.flw] remove cutscene

function music:miniboss

spawnpoint @a[tag=mg.flw] 10022 94 -87 180 0
scoreboard players set $flsp mg.st 37
bossbar set boss:morbex color pink
bossbar set boss:morbex players @a[tag=mg.flw]
bossbar set boss:morbex value 100
execute positioned 10022 94 -98 run function summon:lord_morbex_1
particle minecraft:trial_spawner_detection_ominous 10022 95 -98 0.3 0.5 0.3 0 100
playsound minecraft:entity.glow_squid.squirt master @a[tag=mg.flw] 10022 93 -98 1 2
scoreboard players set morbex_health Value 100

#Start bossbar tracking and miniboss things
setblock 10014 91 -103 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
