# Une étape de biomes par tick (zone chargée : session ou fin de construction)
scoreboard players add $tvbs mg.st 1
execute if score $tvbs mg.st matches 1 in mg:terranova run function mg:terra/bio/s1
execute if score $tvbs mg.st matches 2 in mg:terranova run function mg:terra/bio/s2
execute if score $tvbs mg.st matches 3 in mg:terranova run function mg:terra/bio/s3
execute if score $tvbs mg.st matches 4 in mg:terranova run function mg:terra/bio/s4
execute if score $tvbs mg.st matches 5 in mg:terranova run function mg:terra/bio/s5
execute if score $tvbs mg.st matches ..4 run return run schedule function mg:terra/bio_step 1t
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -112 -112 111 111
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -96 -256 95 -97
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove 96 -96 255 95
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -256 -96 -97 95
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -96 96 95 255
