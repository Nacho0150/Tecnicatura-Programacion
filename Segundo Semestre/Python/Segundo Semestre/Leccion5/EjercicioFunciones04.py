# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

def calImpuestos(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    print(f'Pago sin impuesto: {pago_sin_impuesto}')
    print(f'Monto del impuesto: {impuesto}%')
    print(f'Pago con impuesto: {pago_total}')


pago_sin_impuesto = int(input('Ingrese el monto a pagar de un impuesto sin el iva\n'))
impuesto = int(input('Ingrese el monto a pagar del iva\n'))
calImpuestos(pago_sin_impuesto, impuesto)