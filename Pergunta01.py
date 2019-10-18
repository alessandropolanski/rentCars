class Calculadora (object):
  def Adicionar(num1, num2):
    resultado = num1 + num2
    return resultado
  
  def Subtrair(num1,num2):
    resultado = num1 - num2
    return resultado
  
  def Multiplicar(num1,num2):
    resultado = num1 * num2
    return resultado
  
  def Dividir(num1,num2):
    resultado = num1/num2
    return resultado

resultado = Calculadora.Adicionar(2,3)
print(resultado)