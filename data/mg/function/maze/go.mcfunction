# Départ : le sas s'ouvre
execute unless score $jok mg.st matches 1 run function mg:maze/build
fill -51 65 41099 -51 67 41100 minecraft:air
effect give @a[tag=mg.play] minecraft:night_vision infinite 0 true
scoreboard players set $jtm mg.st 0
