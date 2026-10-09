scoreboard players operation $zk mg.st = @s mg.zk
scoreboard players set #60 mg.st 60
scoreboard players operation $zk mg.st *= #60 mg.st
scoreboard players operation @s mg.zpt += $zk mg.st
scoreboard players reset @s mg.zk
