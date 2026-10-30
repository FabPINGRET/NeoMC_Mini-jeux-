give @s quartz[custom_model_data={strings:["5"]},custom_name={"bold":true,"color":"dark_purple","text":"Dark Scales"},enchantment_glint_override=true,lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"dark_purple","italic":true,"text":"Odious "},{"color":"aqua","text":"energy..."}]]] 1
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
execute at @s run particle dust{color:[0.235,0.000,0.388],scale:1} ~ ~1 ~ 0.3 0.6 0.3 0 100 normal
tag @s add dark_scales
advancement grant @s only sidequest:scales_8

execute as @a[tag=mg.flw] run function game:100_check
