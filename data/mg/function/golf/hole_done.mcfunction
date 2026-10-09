# Tout le monde a fini le trou : pause de 4 s
scoreboard players set $gfw mg.st 80
tellraw @a[tag=mg.play] [{"text":"⛳ Trou ","color":"green"},{"score":{"name":"$gfh","objective":"mg.st"},"color":"yellow"},{"text":" terminé. ","color":"green"},{"text":"Trou suivant dans 4 s…","color":"gray"}]
