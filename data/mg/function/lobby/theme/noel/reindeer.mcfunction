# 🎄 Noël : un animal du thème à cet endroit (appelé par lobby/theme/spot)
execute if score $rp mg.st matches 1 run summon minecraft:cow ~ ~ ~ {Tags:["mg.thm","mg.thmob","mg.th_reindeer"],PersistenceRequired:1b,Invulnerable:1b,DeathLootTable:"minecraft:empty",Silent:1b,variant:"mg:reindeer"}
execute unless score $rp mg.st matches 1 run summon minecraft:cow ~ ~ ~ {Tags:["mg.thm","mg.thmob","mg.th_reindeer"],PersistenceRequired:1b,Invulnerable:1b,DeathLootTable:"minecraft:empty",Silent:1b,variant:"minecraft:cold"}
