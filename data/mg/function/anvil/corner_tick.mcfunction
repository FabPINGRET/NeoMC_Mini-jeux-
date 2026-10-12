# Anti-camping : rester 5 s dans un coin de l'arène → éliminé, sans avertissement
tag @a remove mg.acz
execute positioned -10 81 6690 run tag @a[tag=mg.play,distance=..3] add mg.acz
execute positioned 11 81 6690 run tag @a[tag=mg.play,distance=..3] add mg.acz
execute positioned -10 81 6711 run tag @a[tag=mg.play,distance=..3] add mg.acz
execute positioned 11 81 6711 run tag @a[tag=mg.play,distance=..3] add mg.acz
scoreboard players add @a[tag=mg.acz] mg.acn 1
scoreboard players set @a[tag=mg.play,tag=!mg.acz] mg.acn 0
execute as @a[tag=mg.acz,scores={mg.acn=100..}] run function mg:anvil/corner_kill
