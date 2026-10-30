give @s quartz[custom_model_data={strings:["3"]},custom_name={"bold":true,"color":"blue","text":"Water Scales"},enchantment_glint_override=true,lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"blue","italic":true,"text":"Aqueous "},{"color":"aqua","text":"energy..."}]]] 1
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
execute at @s run particle dust{color:[0.200,0.300,0.700],scale:1} ~ ~1 ~ 0.3 0.6 0.3 0 100 normal
tag @s add water_scales
advancement grant @s only sidequest:scales_4

execute as @a[tag=mg.flw] run function game:100_check
