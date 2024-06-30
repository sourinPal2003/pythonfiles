class father:
    name=""
    address=""

    def farmer(self):
        print('happy to be a farmer')



class son(father):
    dgree=""
    def developer(self):
        print('happy to be a developer')



a=father()
a.name='dilip'
a.address='amral'
print(a.name,"\n",a.address)
a.farmer()

###son can access father's all variable and function
b=son()
b.name='Sourin'
b.address='gpur'
b.dgree="b Tech"
print(b.name,"\n",b.address,"\n",b.dgree)
b.farmer()
b.developer()

