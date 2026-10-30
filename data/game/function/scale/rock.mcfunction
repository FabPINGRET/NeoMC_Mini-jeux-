give @s quartz[custom_model_data={strings:["6"]},custom_name={"bold":true,"color":"gray","italic":true,"text":"Rock Scales"},lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"gray","text":"Jagged"},{"color":"aqua","text":" energy..."}]]] 1
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
execute at @s run particle dust{color:[0.400,0.400,0.400],scale:1} ~ ~1 ~ 0.3 0.6 0.3 0 100 normal
tag @s add rock_scales
advancement grant @s only sidequest:scales_2

execute as @a[tag=mg.flw] run function game:100_check
