# ✷ TNT Run glace : remise à neuf
fill -19 50 41681 19 95 41719 minecraft:air
execute if score $game mg.st matches 244 run function mg:tntice/build_s
execute if score $game mg.st matches 245 run function mg:tntice/build_b
