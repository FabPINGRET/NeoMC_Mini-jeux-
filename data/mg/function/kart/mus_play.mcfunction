$execute as @a[tag=mg.play,tag=!mg.kfin] unless score @s mg.kst matches 1.. at @s run function mg:kart/mus/t$(t)_$(s)
$execute as @a[tag=mg.play,tag=!mg.kfin,scores={mg.kst=1..}] at @s run function mg:kart/mus/star_$(s)
