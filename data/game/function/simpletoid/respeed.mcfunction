execute as @e[tag=simpletoid,tag=!winner,tag=!loser,distance=0..] store result score @s Value run random value 2..4
execute as @e[tag=simpletoid,tag=winner,distance=0..] store result score @s Value run random value 4..5
execute as @e[tag=simpletoid,tag=loser,distance=0..] store result score @s Value run random value 1..2
