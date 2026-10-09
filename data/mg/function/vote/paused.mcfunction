# @s = joueur en pause ou en survie qui tente de voter : refus (mg.vote remis à zéro, sinon core/tick relance vote/cast)
execute if entity @s[tag=mg.spectate] run tellraw @s [{"text":"⏸ Tu es en pause : désactive la pause pour voter. ","color":"gray"},{"text":"[▶ Reprendre]","color":"green","click_event":{"action":"run_command","command":"trigger mg.opt set 1"}}]
execute if entity @s[tag=!mg.spectate,tag=mg.surv] run tellraw @s [{"text":"🌲 Tu es en survie : reviens au lobby pour voter.","color":"gray"}]
scoreboard players reset @s mg.vote
