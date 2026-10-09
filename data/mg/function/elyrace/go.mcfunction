# Course d'élytres : départ
function mg:elyrace/gate_off
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
# texte du départ : go_text parle à @s (le solo l'appelle pour son seul joueur)
execute if score $xc mg.st matches 1 as @a[tag=mg.play] run function mg:elyrace/c1/go_text
execute if score $xc mg.st matches 2 as @a[tag=mg.play] run function mg:elyrace/c2/go_text
# gravité de course de chaque participant (selon son parcours, mg.xcr) ; le solo l'appelle pour son seul joueur
execute as @a[tag=mg.play] run function mg:elyrace/grav_on
