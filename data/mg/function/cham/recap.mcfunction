# Récapitulatif de fin de manche (points de chacun, meilleur joueur)
tellraw @a[tag=mg.cmx] {"text":"━━━━━━━━ 🦎 MECCHA CHAMELEON ━━━━━━━━","color":"green","bold":true}
execute if entity @a[tag=mg.cmh,tag=!mg.cmout] run tellraw @a[tag=mg.cmx] [{"text":"🦎 Jamais trouvés : ","color":"green"},{"selector":"@a[tag=mg.cmh,tag=!mg.cmout]","color":"yellow"}]
execute as @a[tag=mg.cms] run tellraw @a[tag=mg.cmx] [{"text":"🔍 ","color":"red"},{"selector":"@s","color":"white"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmf"},"color":"yellow"},{"text":" trouvé(s), ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmpts"},"color":"gold"},{"text":" pts","color":"gray"}]
execute as @a[tag=mg.cmh] run tellraw @a[tag=mg.cmx] [{"text":"🦎 ","color":"green"},{"selector":"@s","color":"white"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmpts"},"color":"gold"},{"text":" pts","color":"gray"}]
scoreboard players set $cmbest mg.st -1
execute as @a[tag=mg.cmx] run scoreboard players operation $cmbest mg.st > @s mg.cmpts
execute as @a[tag=mg.cmx] if score @s mg.cmpts = $cmbest mg.st run tellraw @a[tag=mg.cmx] [{"text":"⭐ Meilleur joueur : ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"@s","objective":"mg.cmpts"},"color":"gold"},{"text":" pts)","color":"gray"}]
