# Temple — vague 20 : BOSS L'Émissaire du Kraken
summon minecraft:guardian 11.5 64 9900.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:guardian -11.5 64 9900.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:drowned 0.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 8.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -8.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 12.5 64 9908.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -11.5 64 9909.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 10.5 64 9894.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
item replace entity @e[tag=mg.dr] weapon.mainhand with minecraft:trident[enchantments={impaling:3}]
tag @e[tag=mg.dr] remove mg.dr
execute unless score $wdup mg.st matches 1 run summon minecraft:elder_guardian 0.5 62 9900.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"L'Émissaire du Kraken","color":"aqua","bold":true}],CustomNameVisible:1b}
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 3
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:800,name:"{\"text\":\"L\'Émissaire du Kraken\",\"color\":\"aqua\",\"bold\":true}"}
execute unless score $wdup mg.st matches 1 run function mg:mobarena/temple/boss_init
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"L'Émissaire du Kraken","color":"aqua"}]
execute unless score $wdup mg.st matches 1 run execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"2× Gardien, 6× Noyé au trident (Impaling)","color":"yellow"},{"text":"  (sbires + boss)","color":"dark_gray"}]
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"L'Émissaire du Kraken","color":"aqua","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
