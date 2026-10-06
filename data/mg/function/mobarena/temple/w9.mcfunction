# Temple — vague 9
summon minecraft:drowned 11.5 64 9900.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -11.5 64 9900.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 0.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 8.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -8.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 12.5 64 9908.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -11.5 64 9909.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 10.5 64 9894.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -9.5 64 9894.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 0.5 64 9892.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 6.5 64 9918.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -5.5 64 9918.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:guardian 18.5 64 9906.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:guardian -17.5 64 9906.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:guardian 18.5 64 9894.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:guardian -17.5 64 9894.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:guardian 12.5 64 9920.5 {Tags:["mg.mob"],PersistenceRequired:1b}
item replace entity @e[tag=mg.dr] weapon.mainhand with minecraft:trident[enchantments={impaling:3}]
tag @e[tag=mg.dr] remove mg.dr
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"12× Noyé au trident (Impaling), 5× Gardien","color":"yellow"},{"text":"  (17 monstres)","color":"dark_gray"}]
