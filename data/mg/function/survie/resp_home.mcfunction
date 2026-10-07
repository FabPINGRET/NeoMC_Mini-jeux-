data modify storage mg:survie r set value {d:"mg:survie"}
$data modify storage mg:survie r.x set from storage mg:survie p.k$(id).home[0]
$data modify storage mg:survie r.y set from storage mg:survie p.k$(id).home[1]
$data modify storage mg:survie r.z set from storage mg:survie p.k$(id).home[2]
function mg:survie/resp_set with storage mg:survie r
