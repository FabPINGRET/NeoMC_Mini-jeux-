execute unless score $evk mg.st matches 1..3 store result score $evk mg.st run random value 1..3
bossbar add mg:ev ""
bossbar set mg:ev max 60
bossbar set mg:ev style notched_10
execute if score $evk mg.st matches 1 run function mg:lobby/ev/ann_1
execute if score $evk mg.st matches 2 run function mg:lobby/ev/ann_2
execute if score $evk mg.st matches 3 run function mg:lobby/ev/ann_3
