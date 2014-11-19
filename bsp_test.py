#!/usr/bin/env python

import BSPgen

bsp = BSPgen.BSPgen(133, 66, 6, 20)
bsp.iterate(2)
bsp.render()
