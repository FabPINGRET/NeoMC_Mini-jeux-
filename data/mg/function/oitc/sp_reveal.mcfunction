# Flèche révélatrice tirée (@s = la flèche) : tous les adversaires brillent 6 s
execute on origin run tag @s add mg.osh
effect give @a[tag=mg.play,tag=!mg.osh] minecraft:glowing 6 0 true
execute as @a[tag=mg.play] at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 1.8
tag @a remove mg.osh
