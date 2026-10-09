# Un pas (0,2 bloc) du regard du cacheur
execute if block ~ ~ ~ #mg:ray_pass run scoreboard players remove $phr mg.st 1
execute if block ~ ~ ~ #mg:ray_pass if score $phr mg.st matches 1.. positioned ^ ^ ^0.2 run return run function mg:ph/copy_ray
execute if block ~ ~ ~ minecraft:barrel run return run function mg:ph/got {p:1}
execute if block ~ ~ ~ minecraft:crafting_table run return run function mg:ph/got {p:2}
execute if block ~ ~ ~ minecraft:bookshelf run return run function mg:ph/got {p:3}
execute if block ~ ~ ~ minecraft:hay_block run return run function mg:ph/got {p:4}
execute if block ~ ~ ~ minecraft:pumpkin run return run function mg:ph/got {p:5}
execute if block ~ ~ ~ minecraft:carved_pumpkin run return run function mg:ph/got {p:6}
execute if block ~ ~ ~ minecraft:melon run return run function mg:ph/got {p:7}
execute if block ~ ~ ~ minecraft:composter run return run function mg:ph/got {p:8}
execute if block ~ ~ ~ minecraft:cauldron run return run function mg:ph/got {p:9}
execute if block ~ ~ ~ minecraft:lantern run return run function mg:ph/got {p:10}
execute if block ~ ~ ~ minecraft:anvil run return run function mg:ph/got {p:11}
execute if block ~ ~ ~ minecraft:furnace run return run function mg:ph/got {p:12}
execute if block ~ ~ ~ minecraft:smoker run return run function mg:ph/got {p:13}
execute if block ~ ~ ~ minecraft:loom run return run function mg:ph/got {p:14}
execute if block ~ ~ ~ minecraft:fletching_table run return run function mg:ph/got {p:15}
execute if block ~ ~ ~ minecraft:smithing_table run return run function mg:ph/got {p:16}
execute if block ~ ~ ~ minecraft:cartography_table run return run function mg:ph/got {p:17}
execute if block ~ ~ ~ minecraft:beehive run return run function mg:ph/got {p:18}
execute if block ~ ~ ~ minecraft:jukebox run return run function mg:ph/got {p:19}
execute if block ~ ~ ~ minecraft:note_block run return run function mg:ph/got {p:20}
execute if block ~ ~ ~ minecraft:cake run return run function mg:ph/got {p:21}
execute if block ~ ~ ~ minecraft:brewing_stand run return run function mg:ph/got {p:22}
execute if block ~ ~ ~ minecraft:grindstone run return run function mg:ph/got {p:23}
execute if block ~ ~ ~ minecraft:stonecutter run return run function mg:ph/got {p:24}
execute if block ~ ~ ~ minecraft:potted_red_tulip run return run function mg:ph/got {p:25}
execute if block ~ ~ ~ minecraft:oak_leaves run return run function mg:ph/got {p:26}
execute if block ~ ~ ~ minecraft:cobweb run return run function mg:ph/got {p:27}
execute if block ~ ~ ~ minecraft:target run return run function mg:ph/got {p:28}
execute if block ~ ~ ~ minecraft:lectern run return run function mg:ph/got {p:29}
execute if block ~ ~ ~ minecraft:blast_furnace run return run function mg:ph/got {p:30}
