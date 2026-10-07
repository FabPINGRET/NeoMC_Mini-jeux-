# Bataille : un peu de musique d'ambiance pour les 30 dernières secondes
execute if score $ktime mg.st matches 3000 run function mg:kart/final_lap
execute if score $ktime mg.st matches 3000 run tellraw @a[tag=mg.play] [{"text":"⏱ 30 secondes !","color":"gold","bold":true}]
execute if score $ktime mg.st matches 3000 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.2
