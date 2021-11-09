#8.15
import models

models.print_models('1', '2', '3', '4', '5', '6')

print()

#8.16
import shirts
from shirts import make_shirt
from shirts import make_shirt as ms
import shirts as sht
from shirts import *

shirts.make_shirt('L', 'Random text')
make_shirt('M', 'Classes incoming!')
ms('M', 'Too shirt')
sht.make_shirt('XL', '404')
make_shirt('XXXL', 'Mmmm mayyyooo')