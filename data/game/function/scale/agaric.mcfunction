give @s quartz[custom_model_data={strings:["1"]},custom_name={"bold":true,"color":"light_purple","text":"Agaric Scales"},enchantment_glint_override=true,lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"light_purple","italic":true,"text":"Fungal "},{"color":"aqua","text":"energy..."}]]] 1
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
execute at @s run particle dust{color:[1.000,0.600,1.000],scale:1} ~ ~1 ~ 0.3 0.6 0.3 0 100 normal
tag @s add agaric_scales
advancement grant @s only sidequest:scales_1

execute as @a[tag=mg.flw] run function game:100_check
