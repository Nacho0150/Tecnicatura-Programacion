import math
from decimal import Decimal

# manejo de valores infinitos
infinito_positivo = float('inf')
print(f'Infinito positivos: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'Infinito negativos: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# Módulo math
infinito_positivo = math.inf
print(f'Infinito positivos: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'Infinito negativos: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# Módulo Decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivos: {infinito_positivo}')
print(f'Es infinito?: {infinito_positivo.is_infinite()}')

infinito_negativo = Decimal('-Infinity')
print(f'Infinito negativos: {infinito_negativo}')
print(f'Es infinito?: {infinito_negativo.is_infinite()}')