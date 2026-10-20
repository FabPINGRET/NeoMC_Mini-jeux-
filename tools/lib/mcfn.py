"""Écriture des .mcfunction et crochets idempotents partagés par les générateurs autonomes.

    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
    import mcfn
    _fn = mcfn.Fn(F)                      # F = <racine>/data/mg/function
    w, patch, go_range = _fn.write, _fn.patch, _fn.go_range

Aucun état de module : le dossier des fonctions est porté par l'instance (un générateur relancé par runpy
depuis un autre ne partage donc rien). Stdlib uniquement.
"""
import json
import os
import re


def js(o):
    """JSON compact (texte JSON des tellraw / dialog)."""
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


class Fn:
    def __init__(self, fdir):
        self.fdir = fdir

    def path(self, rel):
        return os.path.join(self.fdir, rel + '.mcfunction')

    def write(self, rel, lines):
        p = self.path(rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines) + '\n')

    def lines_of(self, rel):
        with open(self.path(rel), encoding='utf-8') as f:
            return f.read().split('\n')

    def patch(self, rel, anchor, new_lines, where='after'):
        """Insère new_lines avant/après l'unique ligne == anchor (rien ne change si elles y sont déjà)."""
        if where not in ('after', 'before'):
            raise ValueError(where)
        p = self.path(rel)
        with open(p, encoding='utf-8') as f:
            lines = f.read().split('\n')
        if all(l in lines for l in new_lines):
            return
        idx = [i for i, l in enumerate(lines) if l == anchor]
        if len(idx) != 1:
            raise SystemExit(f'{rel} : ancre {anchor!r} trouvée {len(idx)} fois')
        i = idx[0] + (1 if where == 'after' else 0)
        lines[i:i] = new_lines
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines))

    def replace(self, rel, old, new):
        """Remplace l'unique occurrence de old par new (rien ne change si new y est déjà)."""
        p = self.path(rel)
        with open(p, encoding='utf-8') as f:
            t = f.read()
        if new in t:
            return
        n = t.count(old)
        if n != 1:
            raise SystemExit(f'{rel} : {old!r} trouvé {n} fois')
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(t.replace(old, new))

    def drop_lines(self, rel, lines):
        """Retire d'une fonction les lignes exactes données (rien ne change si elles n'y sont plus)."""
        p = self.path(rel)
        with open(p, encoding='utf-8') as f:
            txt = f.read().split('\n')
        kept = [l for l in txt if l not in lines]
        if len(kept) == len(txt):
            return
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(kept))

    def go_range(self, gid):
        """Élargit la plage d'ids acceptés par core/go (1..N) si elle est plus étroite que gid (jamais l'inverse)."""
        p = self.path('core/go')
        with open(p, encoding='utf-8') as f:
            t = f.read()
        m = re.search(r'unless score @s mg\.go matches 1\.\.(\d+) unless', t)
        if not m:
            raise SystemExit('core/go : plage « unless score @s mg.go matches 1..N unless » introuvable')
        if int(m.group(1)) < gid:
            with open(p, 'w', encoding='utf-8', newline='\n') as f:
                f.write(t.replace(m.group(0), f'unless score @s mg.go matches 1..{gid} unless'))
