execute if score $game mg.st matches 202 run function mg:uhc2/cleanup
execute if score $game mg.st matches 203 run function mg:hg2/cleanup
forceload remove -42 34358 42 34442
forceload remove -52 34548 52 34652
schedule clear mg:survival2/prepare_b
