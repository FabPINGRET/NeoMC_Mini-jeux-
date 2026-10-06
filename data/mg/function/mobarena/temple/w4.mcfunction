# Temple — vague 4
summon minecraft:drowned 11.5 64 9900.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -11.5 64 9900.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 0.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 8.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -8.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 12.5 64 9908.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:guardian -11.5 64 9909.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:guardian 10.5 64 9894.5 {Tags:["mg.mob"],PersistenceRequired:1b}
item replace entity @e[tag=mg.dr] weapon.mainhand with minecraft:trident[enchantments={impaling:3}]
tag @e[tag=mg.dr] remove mg.dr
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Noyé au trident (Impaling), 2× Gardien","color":"yellow"},{"text":"  (8 monstres)","color":"dark_gray"}]
