# @s (accroupi, mission 1) : ramassage de sa caisse (3 s, 12 × 5 ticks)
scoreboard players operation $own mg.st = @s mg.tvpid
scoreboard players set $tvf mg.st 0
execute as @e[type=minecraft:marker,tag=mg.tvcrm,distance=..2.5] if score @s mg.tvo = $own mg.st run scoreboard players set $tvf mg.st 1
execute if score $tvf mg.st matches 0 run return run scoreboard players set @s mg.tvmp 0
scoreboard players add @s mg.tvmp 1
scoreboard players set @s mg.tval 10
execute if score @s mg.tvmp matches 1 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮","color":"green"},{"text":"▮▮▮▮▮▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 2 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮","color":"green"},{"text":"▮▮▮▮▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 3 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮","color":"green"},{"text":"▮▮▮▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 4 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮","color":"green"},{"text":"▮▮▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 5 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮","color":"green"},{"text":"▮▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 6 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮▮","color":"green"},{"text":"▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 7 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮▮▮","color":"green"},{"text":"▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 8 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮▮▮▮","color":"green"},{"text":"▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 9 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮▮▮▮▮","color":"green"},{"text":"▮▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 10 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮▮▮▮▮▮","color":"green"},{"text":"▮▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 11 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮▮▮▮▮▮▮","color":"green"},{"text":"▮","color":"dark_gray"}]
execute if score @s mg.tvmp matches 12 run title @s actionbar [{"text":"📦 Ramassage ","color":"yellow"},{"text":"▮▮▮▮▮▮▮▮▮▮▮▮","color":"green"},{"text":"","color":"dark_gray"}]
execute if score @s mg.tvmp matches 12.. run function mg:terra/crate_pick
