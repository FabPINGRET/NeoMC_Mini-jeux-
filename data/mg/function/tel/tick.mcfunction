# 📞 Téléphone — tick (état 2)
execute unless entity @a[tag=mg.play] run return run function mg:core/draw
execute if score $tp mg.st matches 5 run return run function mg:tel/reveal_tick
scoreboard players add $tt mg.st 1
execute if score $tp mg.st matches 1 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/confine
execute if score $tp mg.st matches 3 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/confine
execute if score $tp mg.st matches 2 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/confine
execute if score $tp mg.st matches 4 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/confine
scoreboard players operation $tq mg.st = $tt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $tq mg.st %= #20 mg.st
execute if score $tq mg.st matches 0 run function mg:tel/hud
execute store result score $tna mg.st if entity @a[tag=mg.play,scores={mg.ti=0..}]
execute store result score $tnd mg.st if entity @a[tag=mg.play,tag=mg.tdone,scores={mg.ti=0..}]
execute unless score $tp mg.st matches 1 unless score $tp mg.st matches 3 if score $tna mg.st matches 1.. if score $tnd mg.st = $tna mg.st run return run function mg:tel/phase_end
execute if score $tt mg.st >= $tlim mg.st run function mg:tel/phase_end
