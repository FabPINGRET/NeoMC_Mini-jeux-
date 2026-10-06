# The Dropper — tick de jeu
execute if score $dph mg.st matches 1 run function mg:dropper/drop_tick
execute if score $dph mg.st matches 2 run function mg:dropper/inter_tick
execute if score $dph mg.st matches 3 run function mg:dropper/pre_tick

# Plus personne → égalité
execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw
