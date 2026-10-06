# Build Battle — tick de jeu (état 2)
execute unless entity @a[tag=mg.play] run return run function mg:core/draw
execute if score $bbp mg.st matches 0 run function mg:bb/tick_word
execute if score $bbp mg.st matches 1 run function mg:bb/tick_build
execute if score $bbp mg.st matches 2 run function mg:bb/tick_vote
