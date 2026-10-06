# Suite du diagnostic (10 ticks plus tard)
execute if score $tc mg.st > $tc0 mg.st run tellraw @a[tag=mg.admin] {"text":"✔ Boucle tick active","color":"green"}
execute unless score $tc mg.st > $tc0 mg.st run tellraw @a[tag=mg.admin] {"text":"✖ Boucle tick inactive : #minecraft:tick non pris en compte → /reload","color":"red"}
