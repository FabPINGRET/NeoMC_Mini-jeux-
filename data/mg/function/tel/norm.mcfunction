# mg:tel nsrc → nout : minuscules, sans accents, sans ponctuation, sans article au début, sans espaces, sans pluriel final en s/x
execute unless data storage mg:tel nm2 run function mg:tel/norm_maps
data modify storage mg:tel nc.map set value "nm1"
data modify storage mg:tel nout set value ""
data modify storage mg:tel nrest set from storage mg:tel nsrc
function mg:tel/norm_step
execute store result score #nl mg.st run data get storage mg:tel nout
execute if score #nl mg.st matches 5.. run data modify storage mg:tel pf set string storage mg:tel nout 0 4
execute if score #nl mg.st matches 5.. if data storage mg:tel {pf:"les "} run data modify storage mg:tel nout set string storage mg:tel nout 4
execute if score #nl mg.st matches 5.. run data modify storage mg:tel pf set string storage mg:tel nout 0 4
execute if score #nl mg.st matches 5.. if data storage mg:tel {pf:"une "} run data modify storage mg:tel nout set string storage mg:tel nout 4
execute if score #nl mg.st matches 5.. run data modify storage mg:tel pf set string storage mg:tel nout 0 4
execute if score #nl mg.st matches 5.. if data storage mg:tel {pf:"des "} run data modify storage mg:tel nout set string storage mg:tel nout 4
execute if score #nl mg.st matches 4.. run data modify storage mg:tel pf set string storage mg:tel nout 0 3
execute if score #nl mg.st matches 4.. if data storage mg:tel {pf:"le "} run data modify storage mg:tel nout set string storage mg:tel nout 3
execute if score #nl mg.st matches 4.. run data modify storage mg:tel pf set string storage mg:tel nout 0 3
execute if score #nl mg.st matches 4.. if data storage mg:tel {pf:"la "} run data modify storage mg:tel nout set string storage mg:tel nout 3
execute if score #nl mg.st matches 4.. run data modify storage mg:tel pf set string storage mg:tel nout 0 3
execute if score #nl mg.st matches 4.. if data storage mg:tel {pf:"un "} run data modify storage mg:tel nout set string storage mg:tel nout 3
execute if score #nl mg.st matches 4.. run data modify storage mg:tel pf set string storage mg:tel nout 0 3
execute if score #nl mg.st matches 4.. if data storage mg:tel {pf:"du "} run data modify storage mg:tel nout set string storage mg:tel nout 3
execute if score #nl mg.st matches 4.. run data modify storage mg:tel pf set string storage mg:tel nout 0 3
execute if score #nl mg.st matches 4.. if data storage mg:tel {pf:"de "} run data modify storage mg:tel nout set string storage mg:tel nout 3
execute if score #nl mg.st matches 3.. run data modify storage mg:tel pf set string storage mg:tel nout 0 2
execute if score #nl mg.st matches 3.. if data storage mg:tel {pf:"l "} run data modify storage mg:tel nout set string storage mg:tel nout 2
data modify storage mg:tel nc.map set value "nm2"
data modify storage mg:tel nrest set from storage mg:tel nout
data modify storage mg:tel nout set value ""
function mg:tel/norm_step
execute store result score #nl mg.st run data get storage mg:tel nout
execute if score #nl mg.st matches 4.. run data modify storage mg:tel pf set string storage mg:tel nout -1
execute if score #nl mg.st matches 4.. if data storage mg:tel {pf:"s"} run data modify storage mg:tel nout set string storage mg:tel nout 0 -1
execute if score #nl mg.st matches 4.. if data storage mg:tel {pf:"x"} run data modify storage mg:tel nout set string storage mg:tel nout 0 -1
