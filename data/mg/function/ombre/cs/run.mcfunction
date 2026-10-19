# @s (en cinématique) : tick suivant
scoreboard players add @s mg.olctk 1
scoreboard players operation $own mg.st = @s mg.olpid
execute if score @s mg.olcs matches 1 run return run function mg:ombre/cs/intro/t
execute if score @s mg.olcs matches 10 run return run function mg:ombre/cs/open_w/t
execute if score @s mg.olcs matches 11 run return run function mg:ombre/cs/open_nw/t
execute if score @s mg.olcs matches 12 run return run function mg:ombre/cs/open_n/t
execute if score @s mg.olcs matches 13 run return run function mg:ombre/cs/open_ne/t
execute if score @s mg.olcs matches 14 run return run function mg:ombre/cs/open_e/t
execute if score @s mg.olcs matches 15 run return run function mg:ombre/cs/open_se/t
execute if score @s mg.olcs matches 16 run return run function mg:ombre/cs/open_s/t
execute if score @s mg.olcs matches 17 run return run function mg:ombre/cs/open_sw/t
execute if score @s mg.olcs matches 30 run return run function mg:ombre/cs/boss_brennic/t
execute if score @s mg.olcs matches 31 run return run function mg:ombre/cs/boss_ystar/t
execute if score @s mg.olcs matches 32 run return run function mg:ombre/cs/boss_hrimgar/t
execute if score @s mg.olcs matches 33 run return run function mg:ombre/cs/boss_morvaine/t
execute if score @s mg.olcs matches 34 run return run function mg:ombre/cs/boss_sethkar/t
execute if score @s mg.olcs matches 35 run return run function mg:ombre/cs/boss_ignarok/t
execute if score @s mg.olcs matches 36 run return run function mg:ombre/cs/boss_colosse/t
execute if score @s mg.olcs matches 37 run return run function mg:ombre/cs/boss_malveth/t
execute if score @s mg.olcs matches 38 run return run function mg:ombre/cs/boss_nyxar/t
execute if score @s mg.olcs matches 50 run return run function mg:ombre/cs/finale/t
