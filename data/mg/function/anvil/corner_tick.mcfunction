# Anti-camping : rester dans un coin de l'arène → avertissement à 2 s, éliminé à 5 s
tag @a remove mg.acz
execute positioned -10 81 6690 run tag @a[tag=mg.play,distance=..3] add mg.acz
execute positioned 11 81 6690 run tag @a[tag=mg.play,distance=..3] add mg.acz
execute positioned -10 81 6711 run tag @a[tag=mg.play,distance=..3] add mg.acz
execute positioned 11 81 6711 run tag @a[tag=mg.play,distance=..3] add mg.acz
scoreboard players add @a[tag=mg.acz] mg.acn 1
scoreboard players set @a[tag=mg.play,tag=!mg.acz] mg.acn 0
title @a[tag=mg.acz,scores={mg.acn=40..}] actionbar {"text":"⚠ Ne reste pas dans le coin, l'enclume arrive !","color":"red","bold":true}
execute as @a[tag=mg.acz,scores={mg.acn=40}] at @s run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.5
execute as @a[tag=mg.acz,scores={mg.acn=100..}] run function mg:anvil/corner_kill
