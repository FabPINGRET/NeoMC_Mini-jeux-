# 90 s sans gagnant : manche annulée, nouveau niveau
tellraw @a[tag=mg.play] [{"text":"⏱ Personne n'a réussi : on change de niveau !","color":"gold"}]
scoreboard players set $dcph mg.st 2
scoreboard players set $dct mg.st 40
