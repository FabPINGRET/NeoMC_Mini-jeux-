# Vague sur l'outpost Charlie : 2 slashers + 1 par colon présent (5 au plus)
scoreboard players set $tvow3 mg.st 15
execute store result score $tvn mg.st if entity @a[tag=mg.tvw,x=30.5,y=66,z=72.5,distance=..40]
scoreboard players add $tvn mg.st 2
execute if score $tvn mg.st matches 6.. run scoreboard players set $tvn mg.st 5
function mg:terra/d_wave_one_3
