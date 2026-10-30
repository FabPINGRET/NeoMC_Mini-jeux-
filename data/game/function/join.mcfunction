tag @r[gamemode=adventure,tag=mg.flw] add anchorperson
tp @s @p[tag=anchorperson,tag=mg.flw]
execute if entity @p[tag=anchorperson,tag=dw,tag=mg.flw] run tag @s add dw
execute if entity @p[tag=anchorperson,tag=no_warp,tag=mg.flw] run tag @s add no_warp
execute if entity @p[tag=anchorperson,tag=cutscene,tag=mg.flw] run tag @s add cutscene
scoreboard players operation @s SoundtrackOverride = @p[tag=anchorperson,tag=mg.flw] SoundtrackOverride
gamemode adventure @s
particle minecraft:enchant 152 59.5 -12 0.3 0.3 0.3 0 300 normal
clear @s
give @s writable_book[custom_name='{"bold":true,"color":"aqua","text":"Adventure Notes"}',lore=['"For writing down"','"important information"','"along your journey!"'],writable_book_content={pages:[""]}]
give @s apple 5
execute as @a[tag=mg.flw] unless items entity @s container.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['18']}] run give @s carrot_on_a_stick[custom_name={"bold":true,"color":"white","italic":true,"text":"Ping"},lore=[{"color":"dark_purple","text":"Helps you locate your"},{"color":"dark_purple","text":"fellow adventurers by"},{"color":"dark_purple","text":"making them glow!"}],unbreakable={},tooltip_display={hidden_components:["unbreakable"]},custom_model_data={strings:["18"]}] 1
tag @a[tag=mg.flw] remove ready
tellraw @s {"text":"Set your spawn when you're able! Have a good adventure!"}

execute unless entity @a[tag=anchorperson,tag=mg.flw] run tp @s 152 58 -12 -90 0
spawnpoint @s 152 58 -12 -90 0

tag @a[tag=mg.flw] remove anchorperson
