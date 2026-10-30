give @s quartz[custom_model_data={strings:["4"]},custom_name={"bold":true,"color":"yellow","text":"Light Scales"},enchantment_glint_override=true,lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"yellow","italic":true,"text":"Radiant "},{"color":"aqua","text":"energy..."}]]] 1
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
execute at @s run particle dust{color:[1.000,1.000,0.500],scale:1} ~ ~1 ~ 0.3 0.6 0.3 0 100 normal
tag @s add light_scales
advancement grant @s only sidequest:scales_7

execute as @a[tag=mg.flw] run function game:100_check
