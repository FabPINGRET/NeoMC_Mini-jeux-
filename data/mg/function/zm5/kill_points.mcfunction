scoreboard players operation $zk mg.st = @s mg.zkl
scoreboard players set #60 mg.st 60
execute if score $zdp mg.st matches 1.. run scoreboard players set #60 mg.st 120
scoreboard players operation $zk mg.st *= #60 mg.st
scoreboard players operation @s mg.zpt += $zk mg.st
scoreboard players set #60 mg.st 60
scoreboard players reset @s mg.zkl
