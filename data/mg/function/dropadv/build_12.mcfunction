function mg:dropadv/fl_remove
data modify storage mg:dropadv v2 set value 1b
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"The Dropper : Aventure construit (10 niveaux).","color":"green"}]
