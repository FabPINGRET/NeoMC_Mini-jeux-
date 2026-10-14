# Vague sur l'outpost Bravo : 2 slashers + 1 par colon présent (5 au plus)
scoreboard players set $tvow2 mg.st 15
execute store result score $tvn mg.st if entity @a[tag=mg.tvw,x=-71.5,y=70,z=6.5,distance=..40]
scoreboard players add $tvn mg.st 2
execute if score $tvn mg.st matches 6.. run scoreboard players set $tvn mg.st 5
function mg:terra/d_wave_one_2
