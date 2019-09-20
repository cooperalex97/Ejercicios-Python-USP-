segundos_str=input("Por favor,entre com o número de segundos que deseja converter:\n")

total_segs=int(segundos_str)

#numero de dias
dias= total_segs//(24*3600)
seg_rest=total_segs%(24*3600)

#numero de horas
horas= seg_rest//3600
seg_restantes=total_segs%3600

#numero de minutos
minutos=seg_restantes//60

#numero de segundos
segs_restantes_final=seg_restantes%60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")


