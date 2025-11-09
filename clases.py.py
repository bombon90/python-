class lenguaje:
    def __init__(self, nombre , año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):
        print('%s fue creado en %s' %(self.nombre, self.año))

python = lenguaje('python',1991)
python.descripcion()
JavaScript = lenguaje('JavaScript', 1995)
JavaScript.descripcion()
Html = lenguaje('Html', 1993)
Html.descripcion()
Css = lenguaje('Css', 1996)
Css.descripcion()