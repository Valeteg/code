class Empleado: 
    #aqui va el codigo

    '''------------------
    #Atributos
    ------------------'''

    nombre=''
    apellidos=''
    '''-----------------
    # 1 = Masculino y 2 = Femenino
    -----------------'''
    sexo=0
    salario=0
    
    '''----------------------------
    # Metodos
    ----------------------------'''
    
    def CambiarSalaraio(self, nSalario):
        #Aquí va el codigo
        self.salario = nSalario
        return  'su nuevo salario es: '+self.salario       
    
    def ConsultarSalario(self):
        #Aquí va el codigo
        return self.salario
    
    def AumentoSalarial(self):
        #Aquí va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return  'su nuevo salario es: '+self.salario
     