aluno={'nome':(str(input('Nome:'))), 'media':(float(input('Media:')))}
if aluno['media'] <= 6.0:
    aluno['status']='reprovado'
else:
    aluno['status']='aprovado'
print(f'O aluno {aluno["nome"]} tem média {aluno["media"]} e está {aluno["status"]}')

