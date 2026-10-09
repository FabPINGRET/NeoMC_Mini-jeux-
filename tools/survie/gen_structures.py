"""Survie : structures ~2,5 à 3 fois plus nombreuses (remplace les structure_set vanilla).

    python3 tools/survie/gen_structures.py <dossier des structure_set vanilla extraits du jar serveur 26.2> [facteur]

Les structure_set vanilla (data/minecraft/worldgen/structure_set/*.json du jar serveur) sont recopiés dans
data/minecraft/worldgen/structure_set/ avec un espacement réduit : spacing × F, separation × F (F = 0,6 par défaut,
densité ≈ 1 / F² ≈ 2,8). Pour les ensembles à espacement 1 (mines, trésors), la fréquence est multipliée par 2,5.
Strongholds (anneaux concentriques) et fossiles du Nether (déjà très denses) inchangés.
Ne concerne que les dimensions générées normalement : le monde des mini-jeux (plat, vide) et la ville GTA n'ont pas de structures.
"""
import json, os, sys

SRC = sys.argv[1]
F = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'minecraft', 'worldgen', 'structure_set')
SKIP = {'strongholds', 'nether_fossils'}
os.makedirs(OUT, exist_ok=True)
for f in sorted(os.listdir(SRC)):
    k = f[:-5]
    d = json.load(open(os.path.join(SRC, f)))
    p = d['placement']
    if k in SKIP or p.get('type') != 'minecraft:random_spread':
        continue
    old = (p['spacing'], p['separation'], p.get('frequency'))
    if p['spacing'] > 1:
        p['spacing'] = max(2, round(p['spacing'] * F))
        p['separation'] = min(max(0, round(p['separation'] * F)), p['spacing'] - 1)
    if 'frequency' in p and old[0] == 1:   # seulement mines et trésors (les avant-postes gardent leur fréquence)
        p['frequency'] = round(min(1.0, p['frequency'] * 2.5), 4)
    json.dump(d, open(os.path.join(OUT, f), 'w'), indent=2)
    print(f'{k:20} spacing/separation/frequency {old} -> {(p["spacing"], p["separation"], p.get("frequency"))}')
