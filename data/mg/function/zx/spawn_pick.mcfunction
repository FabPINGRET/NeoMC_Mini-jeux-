# Un mob de la manche à cet enclos : zombie, zombie villageois, rapide (manche 3+), rampant (4+), brute (6+), chien (manche 5)
execute if score $zdog mg.st matches 1 run return run function mg:zx/spawn_dog with storage mg:zm
execute store result score $zx2 mg.st run random value 1..100
execute if score $zx2 mg.st matches 1..20 run return run function mg:zx/spawn_villager with storage mg:zm
execute if score $zr mg.st matches 3.. if score $zx2 mg.st matches 21..40 run return run function mg:zx/spawn_runner with storage mg:zm
execute if score $zr mg.st matches 4.. if score $zx2 mg.st matches 41..55 run return run function mg:zx/spawn_crawler with storage mg:zm
execute if score $zr mg.st matches 6.. if score $zx2 mg.st matches 56..65 run return run function mg:zx/spawn_brute with storage mg:zm
execute if score $zr mg.st matches 8.. if score $zx2 mg.st matches 66..72 run return run function mg:zx/spawn_brute with storage mg:zm
function mg:zm/spawn_one with storage mg:zm
