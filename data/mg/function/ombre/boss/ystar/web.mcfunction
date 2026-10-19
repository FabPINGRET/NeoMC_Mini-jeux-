# Ysh'tar, la reine-araignée : web
playsound minecraft:entity.spider.ambient hostile @a ~ ~ ~ 2 0.5
execute as @a[tag=mg.olw,gamemode=adventure,distance=..18] at @s run function mg:ombre/m/web_at
