execute if score simpletoid_force_winner Value matches 0 if score simpletoid_bet Value matches 1 run tag @n[tag=simpletoid,tag=1,distance=0..] add loser
execute if score simpletoid_force_winner Value matches 0 if score simpletoid_bet Value matches 2 run tag @n[tag=simpletoid,tag=2,distance=0..] add loser
execute if score simpletoid_force_winner Value matches 0 if score simpletoid_bet Value matches 3 run tag @n[tag=simpletoid,tag=3,distance=0..] add loser

execute if score simpletoid_force_winner Value matches 1 run tag @n[tag=simpletoid,tag=1,distance=0..] add winner
execute if score simpletoid_force_winner Value matches 2 run tag @n[tag=simpletoid,tag=2,distance=0..] add winner
execute if score simpletoid_force_winner Value matches 3 run tag @n[tag=simpletoid,tag=3,distance=0..] add winner

execute unless entity @e[tag=simpletoid,tag=loser,distance=0..] run tag @e[sort=random,limit=1,tag=simpletoid,tag=!winner,distance=0..] add loser
execute unless entity @e[tag=simpletoid,tag=winner,distance=0..] run tag @e[sort=random,limit=1,tag=simpletoid,tag=!loser,distance=0..] add winner
