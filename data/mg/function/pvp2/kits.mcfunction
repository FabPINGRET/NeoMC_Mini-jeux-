# Distribution des kits de classe au GO (état 2) — chaque kit est isolé dans sa propre fonction
execute as @a[tag=mg.play,scores={mg.cl=2}] run function mg:pvp2/kit_archer
execute as @a[tag=mg.play,scores={mg.cl=3}] run function mg:pvp2/kit_tank
execute as @a[tag=mg.play,scores={mg.cl=4}] run function mg:pvp2/kit_assassin
execute as @a[tag=mg.play,scores={mg.cl=5}] run function mg:pvp2/kit_mage
execute as @a[tag=mg.play,scores={mg.cl=6}] run function mg:pvp2/kit_pyro
# Guerrier = classe par défaut (1, ou valeur absente/invalide)
execute as @a[tag=mg.play,scores={mg.cl=11}] run function mg:pvp2/kit_lancer
execute as @a[tag=mg.play,scores={mg.cl=12}] run function mg:pvp2/kit_ninja
execute as @a[tag=mg.play,scores={mg.cl=13}] run function mg:pvp2/kit_medic
execute as @a[tag=mg.play,scores={mg.cl=14}] run function mg:pvp2/kit_engineer
execute as @a[tag=mg.play] unless score @s mg.cl matches 2..6 unless score @s mg.cl matches 11..14 run function mg:pvp2/kit_warrior

tellraw @a[tag=mg.play] [{"text":"⚔ Chacun pour soi, chacun sa classe : dernier survivant = gagnant !","color":"yellow"}]
execute as @a[tag=mg.play,scores={mg.cl=2}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Archer","color":"green"}]
execute as @a[tag=mg.play,scores={mg.cl=3}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Tank","color":"aqua"}]
execute as @a[tag=mg.play,scores={mg.cl=4}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Assassin","color":"dark_gray"}]
execute as @a[tag=mg.play,scores={mg.cl=5}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Mage","color":"light_purple"}]
execute as @a[tag=mg.play,scores={mg.cl=6}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Pyromane","color":"gold"}]
execute as @a[tag=mg.play] unless score @s mg.cl matches 2..6 unless score @s mg.cl matches 11..14 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Guerrier","color":"white"}]
execute as @a[tag=mg.play,scores={mg.cl=11}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Lancier","color":"dark_aqua"}]
execute as @a[tag=mg.play,scores={mg.cl=12}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Ninja","color":"blue"}]
execute as @a[tag=mg.play,scores={mg.cl=13}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Médecin","color":"red"}]
execute as @a[tag=mg.play,scores={mg.cl=14}] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" joue ","color":"gray"},{"text":"Ingénieur","color":"gray"}]
