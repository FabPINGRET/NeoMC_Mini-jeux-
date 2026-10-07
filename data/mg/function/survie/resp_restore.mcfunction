# Point de réapparition de survie (lit, ancre) ; à défaut, le point de départ du joueur
$execute unless data storage mg:survie p.k$(id).resp.pos run return run function mg:survie/resp_home {id:$(id)}
data modify storage mg:survie r set value {d:"mg:survie"}
$data modify storage mg:survie r.x set from storage mg:survie p.k$(id).resp.pos[0]
$data modify storage mg:survie r.y set from storage mg:survie p.k$(id).resp.pos[1]
$data modify storage mg:survie r.z set from storage mg:survie p.k$(id).resp.pos[2]
$data modify storage mg:survie r.d set from storage mg:survie p.k$(id).resp.dimension
function mg:survie/resp_set with storage mg:survie r
