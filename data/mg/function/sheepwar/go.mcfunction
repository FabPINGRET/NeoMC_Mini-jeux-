# Sheep War — début : munitions adaptées au nombre de joueurs + joueurs moins fragiles aux explosions

scoreboard players reset @a mg.cd

# Taille de la plus grande équipe
execute store result score $nr mg.st if entity @a[team=mg_red,tag=mg.play]
execute store result score $nb mg.st if entity @a[team=mg_blue,tag=mg.play]
scoreboard players operation $tm mg.st = $nr mg.st
scoreboard players operation $tm mg.st > $nb mg.st

# Plus il y a de monde, moins il y a de moutons : (stock de départ, période de recharge, moutons par recharge)
scoreboard players set $sa mg.st 12
scoreboard players set $srp mg.st 70
scoreboard players set $srn mg.st 2
execute if score $tm mg.st matches 2 run scoreboard players set $sa mg.st 8
execute if score $tm mg.st matches 2 run scoreboard players set $srp mg.st 85
execute if score $tm mg.st matches 2 run scoreboard players set $srn mg.st 1
execute if score $tm mg.st matches 3..4 run scoreboard players set $sa mg.st 6
execute if score $tm mg.st matches 3..4 run scoreboard players set $srp mg.st 115
execute if score $tm mg.st matches 3..4 run scoreboard players set $srn mg.st 1
execute if score $tm mg.st matches 5.. run scoreboard players set $sa mg.st 4
execute if score $tm mg.st matches 5.. run scoreboard players set $srp mg.st 145
execute if score $tm mg.st matches 5.. run scoreboard players set $srn mg.st 1
scoreboard players operation $sr mg.st = $srp mg.st

execute store result storage mg:sw n int 1 run scoreboard players get $sa mg.st
execute as @a[tag=mg.play] run function mg:sheepwar/give_ammo with storage mg:sw
execute as @a[tag=mg.play] run function mg:sheepwar/give_special

# Moins de régénération / saturation : plus de saturation infinie, régénération naturelle coupée,
# remplacée par un petit soin (2 cœurs) toutes les 12 s
effect clear @a[tag=mg.play] minecraft:saturation
function mg:core/regen_off
scoreboard players set $sh mg.st 240

# Moins sensibles aux explosions : Résistance III + moins de recul (attribut isolé)
effect give @a[tag=mg.play] minecraft:resistance infinite 2 true
execute as @a[tag=mg.play] run function mg:sheepwar/attr_on

tellraw @a[tag=mg.play] [{"text":"☁ Clic droit sur un ","color":"white"},{"text":"Mouton-Fusée","color":"aqua"},{"text":" pour catapulter un MOUTON EXPLOSIF sur l'équipe adverse ! Le sol se détruit... ne tombe pas. Moutons limités : ","color":"white"},{"score":{"name":"$sa","objective":"mg.st"},"color":"gold"},{"text":" au départ, puis recharge lente.","color":"white"}]
tellraw @a[tag=mg.play] [{"text":"✦ Chaque mouton a son objet : ","color":"light_purple"},{"text":"Mouton-Fusée","color":"aqua"},{"text":" (normal), ","color":"gray"},{"text":"espace","color":"light_purple"},{"text":" (lévitation + explosion), ","color":"gray"},{"text":"nauséeux","color":"green"},{"text":", ","color":"gray"},{"text":"glacé","color":"aqua"},{"text":" (bloque sur place), ","color":"gray"},{"text":"ténèbres","color":"dark_gray"},{"text":" (cécité), ","color":"gray"},{"text":"feu","color":"gold"},{"text":" (flammes). Regarde ce que tu tiens en main !","color":"gray"}]
