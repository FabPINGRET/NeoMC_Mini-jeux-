data modify storage mg:ombre sv set value 627385376
scoreboard players set $olrl mg.st 0
execute in mg:ombrelune run function mg:ombre/door/catchup
tellraw @a[tag=mg.admin] {"text":"🌙 Ombrelune : PNJ et objets posés.","color":"light_purple"}
