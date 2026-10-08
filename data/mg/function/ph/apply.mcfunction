# @s (cacheur) : met l'apparence de son objet ($php) sur son block_display
scoreboard players operation $pid mg.st = @s mg.pid
scoreboard players operation $pp mg.st = @s mg.php
execute if score $pp mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:barrel"}
execute if score $pp mg.st matches 2 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:crafting_table"}
execute if score $pp mg.st matches 3 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:bookshelf"}
execute if score $pp mg.st matches 4 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:hay_block"}
execute if score $pp mg.st matches 5 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:pumpkin"}
execute if score $pp mg.st matches 6 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:carved_pumpkin"}
execute if score $pp mg.st matches 7 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:melon"}
execute if score $pp mg.st matches 8 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:composter"}
execute if score $pp mg.st matches 9 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:cauldron"}
execute if score $pp mg.st matches 10 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:lantern"}
execute if score $pp mg.st matches 11 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:anvil"}
execute if score $pp mg.st matches 12 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:furnace"}
execute if score $pp mg.st matches 13 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:smoker"}
execute if score $pp mg.st matches 14 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:loom"}
execute if score $pp mg.st matches 15 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:fletching_table"}
execute if score $pp mg.st matches 16 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:smithing_table"}
execute if score $pp mg.st matches 17 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:cartography_table"}
execute if score $pp mg.st matches 18 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:beehive"}
execute if score $pp mg.st matches 19 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:jukebox"}
execute if score $pp mg.st matches 20 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:note_block"}
execute if score $pp mg.st matches 21 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:cake"}
execute if score $pp mg.st matches 22 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:brewing_stand"}
execute if score $pp mg.st matches 23 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:grindstone"}
execute if score $pp mg.st matches 24 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:stonecutter"}
execute if score $pp mg.st matches 25 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:potted_red_tulip"}
execute if score $pp mg.st matches 26 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:oak_leaves",Properties:{persistent:"true"}}
execute if score $pp mg.st matches 27 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:cobweb"}
execute if score $pp mg.st matches 28 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:target"}
execute if score $pp mg.st matches 29 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:lectern"}
execute if score $pp mg.st matches 30 as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {Name:"minecraft:blast_furnace"}
execute if score $pp mg.st matches 1 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.barrel","color":"yellow","bold":true}]
execute if score $pp mg.st matches 2 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.crafting_table","color":"yellow","bold":true}]
execute if score $pp mg.st matches 3 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.bookshelf","color":"yellow","bold":true}]
execute if score $pp mg.st matches 4 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.hay_block","color":"yellow","bold":true}]
execute if score $pp mg.st matches 5 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.pumpkin","color":"yellow","bold":true}]
execute if score $pp mg.st matches 6 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.carved_pumpkin","color":"yellow","bold":true}]
execute if score $pp mg.st matches 7 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.melon","color":"yellow","bold":true}]
execute if score $pp mg.st matches 8 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.composter","color":"yellow","bold":true}]
execute if score $pp mg.st matches 9 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.cauldron","color":"yellow","bold":true}]
execute if score $pp mg.st matches 10 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.lantern","color":"yellow","bold":true}]
execute if score $pp mg.st matches 11 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.anvil","color":"yellow","bold":true}]
execute if score $pp mg.st matches 12 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.furnace","color":"yellow","bold":true}]
execute if score $pp mg.st matches 13 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.smoker","color":"yellow","bold":true}]
execute if score $pp mg.st matches 14 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.loom","color":"yellow","bold":true}]
execute if score $pp mg.st matches 15 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.fletching_table","color":"yellow","bold":true}]
execute if score $pp mg.st matches 16 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.smithing_table","color":"yellow","bold":true}]
execute if score $pp mg.st matches 17 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.cartography_table","color":"yellow","bold":true}]
execute if score $pp mg.st matches 18 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.beehive","color":"yellow","bold":true}]
execute if score $pp mg.st matches 19 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.jukebox","color":"yellow","bold":true}]
execute if score $pp mg.st matches 20 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.note_block","color":"yellow","bold":true}]
execute if score $pp mg.st matches 21 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.cake","color":"yellow","bold":true}]
execute if score $pp mg.st matches 22 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.brewing_stand","color":"yellow","bold":true}]
execute if score $pp mg.st matches 23 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.grindstone","color":"yellow","bold":true}]
execute if score $pp mg.st matches 24 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.stonecutter","color":"yellow","bold":true}]
execute if score $pp mg.st matches 25 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.potted_red_tulip","color":"yellow","bold":true}]
execute if score $pp mg.st matches 26 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.oak_leaves","color":"yellow","bold":true}]
execute if score $pp mg.st matches 27 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.cobweb","color":"yellow","bold":true}]
execute if score $pp mg.st matches 28 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.target","color":"yellow","bold":true}]
execute if score $pp mg.st matches 29 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.lectern","color":"yellow","bold":true}]
execute if score $pp mg.st matches 30 run title @s actionbar [{"text":"🎭 Tu es : ","color":"gold"},{"translate":"block.minecraft.blast_furnace","color":"yellow","bold":true}]
