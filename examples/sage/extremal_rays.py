from __future__ import division
import cbbundle as cbd
import cbclient as cbc
import time
import sage.all as sage
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.geometry.cone import Cone
from sage.rings.rational_field import RationalField

def experiment():
    rank = 5
    level = 4
    num_points = 11

    client = cbc.CBClient()
    liealg = cbd.TypeALieAlgebra(rank, store_fusion=True, exact=True)
    rays = []
    wts = []
    ranks = []
    for wt in liealg.get_weights(level):
        if wt == tuple([0 for x in range(0, rank)]):
            continue
        cbb = cbd.SymmetricConformalBlocksBundle(client, liealg, wt, num_points, level)
        if cbb.get_rank() == 0:
            continue
        divisor = cbb.get_symmetrized_divisor()
        if divisor == [sage.Rational(0) for x in range(0, num_points // 2 - 1)]:
            continue
        rays = rays + [divisor]
        wts = wts + [wt]
        ranks = ranks + [cbb.get_rank()]
        #print(wt, cbb.get_rank(), divisor)

    p = Polyhedron(rays=rays, base_ring=RationalField(), backend="cdd")
    extremal_rays = [list(v.vector()) for v in p.Vrepresentation()]
    c = Cone(p)
    print("Extremal rays:")
    for i in range(0, len(rays)):
        ray = rays[i]
        wt = wts[i]
        rk = ranks[i]
        if ray in extremal_rays:
            print(rk, wt, ray)

if __name__ == '__main__':
    experiment()
