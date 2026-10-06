# Notation : 18 s (360 ticks) par construction
scoreboard players add $bbt mg.st 1
scoreboard players operation $bbq mg.st = $bbt mg.st
scoreboard players operation $bbq mg.st %= $bbc20 mg.st
execute if score $bbq mg.st matches 0 run function mg:bb/vote_leash
execute if score $bbt mg.st matches 240 run function mg:bb/rate_prompt
execute if score $bbt mg.st matches 360.. run function mg:bb/vote_end
