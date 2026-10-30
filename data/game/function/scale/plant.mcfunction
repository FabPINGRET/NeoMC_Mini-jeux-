give @s quartz[custom_model_data={strings:["7"]},custom_name={"bold":true,"color":"green","text":"Plant Scales"},enchantment_glint_override=true,lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"green","italic":true,"text":"Sprouting "},{"color":"aqua","text":"energy..."}]]] 1
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
execute at @s run particle dust{color:[0.400,1.000,0.400],scale:1} ~ ~1 ~ 0.3 0.6 0.3 0 100 normal
tag @s add plant_scales
advancement grant @s only sidequest:scales_5

execute as @a[tag=mg.flw] run function game:100_check
