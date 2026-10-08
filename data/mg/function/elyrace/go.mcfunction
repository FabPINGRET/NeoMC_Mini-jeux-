# Course d'élytres : départ
function mg:elyrace/gate_off
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute if score $xc mg.st matches 1 run function mg:elyrace/c1/go_text
