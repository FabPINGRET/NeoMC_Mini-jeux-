# Chaque seconde : déclenchement et suivi des boss
scoreboard players remove $trspc mg.st 1
scoreboard players remove $trvc mg.st 1
scoreboard players remove $trrc mg.st 1
execute if score $trspa mg.st matches 1 unless entity @e[tag=mg.tvspino] run function mg:terra/rpg/boss/spino_win
execute if score $trva mg.st matches 1 unless entity @e[tag=mg.trvarek] run function mg:terra/rpg/boss/varek_win
execute if score $trra mg.st matches 1 unless entity @e[tag=mg.tvrex] run function mg:terra/rpg/boss/rex_win
execute unless score $trspa mg.st matches 1 if score $trspc mg.st matches ..0 positioned 10 65 -196 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..22,scores={mg.trch=40..}] run function mg:terra/rpg/boss/spino_start
execute unless score $trva mg.st matches 1 if score $trvc mg.st matches ..0 positioned -200 65 4 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..30,scores={mg.trch=62..}] run function mg:terra/rpg/boss/varek_start
execute unless score $trra mg.st matches 1 if score $trrc mg.st matches ..0 positioned 0 99 186 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..14,scores={mg.trch=80..}] run function mg:terra/rpg/boss/rex_start
execute if score $trspa mg.st matches 1 run function mg:terra/rpg/boss/spino
execute if score $trva mg.st matches 1 run function mg:terra/rpg/boss/varek
execute if score $trra mg.st matches 1 run function mg:terra/rpg/boss/rex
