# Mob Arena — début : kit + nuit
execute as @a[tag=mg.play] run function mg:mobarena/kit

time set midnight

# Scoreboard latéral de la partie
scoreboard objectives setdisplay sidebar mg.mb
scoreboard objectives modify mg.mb displayname {"text":"☠ MOB ARENA ☠","color":"red","bold":true}
scoreboard players reset * mg.mb
scoreboard players set Monstres_restants mg.mb 0
scoreboard players set Joueurs_en_vie mg.mb 0
function mg:core/grief_off

# Plus de saturation gratuite : on mange grâce aux récompenses de vague
effect clear @a[tag=mg.play] minecraft:saturation
tellraw @a[tag=mg.play] [{"text":"☠ MOB ARENA : ","color":"dark_green","bold":true},{"text":"survivez ensemble aux vagues de monstres ! Soin entre les vagues, les joueurs tombés reviennent au début de la vague suivante. Boss final à la dernière vague.","color":"gray"}]
title @a[tag=mg.play] subtitle [{"text":"Vague 1 dans 5 secondes...","color":"yellow"}]
title @a[tag=mg.play] title [{"text":"☠","color":"dark_green"}]
execute if score $mt mg.st matches 8 run effect give @a[tag=mg.play] minecraft:water_breathing infinite 0 true
execute if score $mt mg.st matches 6..10 run tellraw @a[tag=mg.play] [{"text":"☠ ","color":"dark_red"},{"text":"20 vagues + un boss à deux phases. Les joueurs tombés reviennent à la vague suivante.","color":"gray"}]
