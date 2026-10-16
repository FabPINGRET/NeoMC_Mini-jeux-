# Session : entités du RPG (régions chargées)
execute unless score $tvw mg.st matches 1 run return 0
execute in mg:terranova run function mg:terra/rpg/setup
