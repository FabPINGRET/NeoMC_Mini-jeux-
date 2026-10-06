# Une enclume : une chance sur deux de viser un joueur au hasard, sinon position aléatoire
execute store result score $r mg.st run random value 0..1
execute if score $r mg.st matches 0 unless entity @a[tag=mg.play] run return 0
execute if score $r mg.st matches 0 at @r[tag=mg.play] run return run function mg:anvil/make
execute store result storage mg:an x int 1 run random value -9..9
execute store result storage mg:an z int 1 run random value 6691..6709
function mg:anvil/drop_at with storage mg:an
