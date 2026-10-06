# Temple — vague 1
summon minecraft:drowned 11.5 64 9900.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned -11.5 64 9900.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 0.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
summon minecraft:drowned 8.5 64 9912.5 {Tags:["mg.mob","mg.dr"],PersistenceRequired:1b}
item replace entity @e[tag=mg.dr] weapon.mainhand with minecraft:trident[enchantments={impaling:3}]
tag @e[tag=mg.dr] remove mg.dr
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Noyé au trident (Impaling)","color":"yellow"},{"text":"  (4 monstres)","color":"dark_gray"}]
