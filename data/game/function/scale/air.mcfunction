give @s quartz[custom_model_data={strings:["8"]},custom_name={"bold":true,"color":"white","text":"Air Scales"},enchantment_glint_override=true,lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"white","italic":true,"text":"Zephyrous "},{"color":"aqua","text":"energy..."}]]] 1
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
execute at @s run particle dust{color:[0.500,0.950,1.000],scale:1} ~ ~1 ~ 0.3 0.6 0.3 0 100 normal
tag @s add air_scales
advancement grant @s only sidequest:scales_6

execute as @a[tag=mg.flw] run function game:100_check
