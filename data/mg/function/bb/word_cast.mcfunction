# @s = joueur ayant utilisé /trigger mg.bw
execute unless score $state mg.st matches 2 run return run scoreboard players reset @s mg.bw
execute unless score $game mg.st matches 58 run return run scoreboard players reset @s mg.bw
execute unless entity @s[tag=mg.bm] run return run function mg:bb/word_deny
execute unless score $bbp mg.st matches 0 run return run scoreboard players reset @s mg.bw
execute if score @s mg.bw matches 1 run function mg:bb/word_book
execute if score @s mg.bw matches 2 run function mg:bb/word_random
execute if score @s mg.bw matches 3 run function mg:bb/word_more
execute if score @s mg.bw matches 11..18 run function mg:bb/word_sug
scoreboard players reset @s mg.bw
