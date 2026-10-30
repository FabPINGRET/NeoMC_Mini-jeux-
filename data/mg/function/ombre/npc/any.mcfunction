# @s parle au PNJ n° $npc (mg.oltalk : les choix des fenêtres de PNJ ne valent que près d'un PNJ, cf. tk et second)
tag @s add mg.oltalk
execute if score $npc mg.st matches 1 run return run function mg:ombre/npc/liora
execute if score $npc mg.st matches 2 run return run function mg:ombre/npc/liora_t
execute if score $npc mg.st matches 3 run return run function mg:ombre/npc/orren
execute if score $npc mg.st matches 4 run return run function mg:ombre/npc/aldric
execute if score $npc mg.st matches 5 run return run function mg:ombre/npc/isolde
execute if score $npc mg.st matches 6 run return run function mg:ombre/npc/bram
execute if score $npc mg.st matches 7 run return run function mg:ombre/npc/elsa
execute if score $npc mg.st matches 8 run return run function mg:ombre/npc/fenna
execute if score $npc mg.st matches 9 run return run function mg:ombre/npc/joss
execute if score $npc mg.st matches 10 run return run function mg:ombre/npc/marthe
execute if score $npc mg.st matches 11 run return run function mg:ombre/npc/tessa
execute if score $npc mg.st matches 12 run return run function mg:ombre/npc/gaspard
execute if score $npc mg.st matches 13 run return run function mg:ombre/npc/elyndra
execute if score $npc mg.st matches 14 run return run function mg:ombre/npc/thalion
execute if score $npc mg.st matches 15 run return run function mg:ombre/npc/bjorn
execute if score $npc mg.st matches 16 run return run function mg:ombre/npc/sigrun
execute if score $npc mg.st matches 17 run return run function mg:ombre/npc/maelle
execute if score $npc mg.st matches 18 run return run function mg:ombre/npc/odo
execute if score $npc mg.st matches 19 run return run function mg:ombre/npc/kassim
execute if score $npc mg.st matches 20 run return run function mg:ombre/npc/zahra
execute if score $npc mg.st matches 21 run return run function mg:ombre/npc/durgan
execute if score $npc mg.st matches 22 run return run function mg:ombre/npc/thrain
execute if score $npc mg.st matches 23 run return run function mg:ombre/npc/aldric_sw
