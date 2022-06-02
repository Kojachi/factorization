import random
import math
import itertools
from itertools import combinations_with_replacement
import numpy as np
from datetime import datetime
import time
import csv

def Euclid(a, b):
	q = a // b
	r = a - (b * q)
	if (r != 0):
		b = Euclid(b, r)
		return b
	else:
		return b

def prime_number(n):
	if(n==2):
		return True
	p=n-1
	s=1
	s0=0
	d=0
	#Miller
	while(p%2==0): #step 0
		p = p//2
		s=s*2
		s0=s0+1
	d = (n-1)//s
	counter = 0
	k=5

	while(counter<k):
		x = random.randint(2, n-1) #step 1
		if(Euclid(n, x)!=1):
			return False
		x_pow_d = pow(x, d, n)
		if(x_pow_d==1 or x_pow_d-n==-1): #step 2.1
			counter = counter+1
		else:
			for i in range(0, s0): #step 2.2
				x_pow_d2r = pow(x,d*pow(2,i),n)
				if(x_pow_d2r-n==-1):
					counter = counter+1
					break
				elif(x_pow_d2r==1):
					return False
				elif(i==s0-1): #step 2.3
					return False
	return True

def division_method(n):
	sqrt = pow(n,1/2)
	sqrt=int(sqrt)
	d=[]
	print("[n]=",sqrt)

	for i in range(2, 48):
		for j in range(2,int(pow(i,1/2))+1):
			if(i%j==0):
				break
		else:
			d.append(i)
	print("Prime numbers:", d)
	d_quant=len(d)
	for i in range (d_quant):
		if(n%d[i]==0):
			q=int(n/d[i])
			p=d[i]
			return (p,q)
	return (0,0)

def pollard(n):
	x0=2
	i=0
	j=0
	x_y_list=[]
	list_order=[]
	while(True):
		i=i+1
		if(list_order.count(i)>0): #для уникнення повторів обчислення
			x=x_y_list[list_order.index(i)]
		else:
			x=(pow(x0,2,n)+1)%n #якщо нове - то обчислюємо
			x_y_list.append(x)
			list_order.append(i)
		j=i
		k=i
		y=x
		while(k!=0):
			j=j+1
			if(list_order.count(j)>0):
				y=x_y_list[list_order.index(j)]
			else:
				y=pow(y,2,n)+1
				x_y_list.append(y)
				list_order.append(j)
			k=k-1
		x0=x
		print("(y",j,"x",i,")=(",y,",",x,")")
		subtr=y-x
		if(subtr<0):
			subtr=n+subtr
		if(subtr==0):
			subtr=x
		d=Euclid(n,subtr)
		print("GSD(",n,",",subtr,")=",d)
		if(d!=1):
			return d

def Lezhandr(a,p):
	if(a==1):
		return 1
	if(a%p==0):
		return 0
	if(a%2==0):
		return Lezhandr(a/2,p)*pow(-1,(pow(p,2)-1)/8)
	elif(a%2!=0 and a!=1):
		return Lezhandr(pow(int(p),1,int(a)),a)*pow(-1,((a-1)*(p-1))/4)

def factorize(B,B2,B_length,b2,s):
	if(b2<0):
		s.insert(0,-1)
		b2=b2*(-1)
	try:
		index = B.index(b2)
		s.append(b2)
		return s
	except ValueError:
		for i in range(B_length):
			if(b2%B[i+1]==0):
				p=B[i+1]
				s.append(p)
				q=int(b2/p)
				factorize(B,B2,B_length,q,s)
				break
			elif(b2%B[i+1]!=0 and i==B_length-1):
				s.append(b2)
		return s

def calculating(table_len, B_length, table, B2_length, new_i, b, B, M, n):
	X=[]
	X_vect=[]
	extra_list=[0]*B_length
	for i in range (new_i, table_len):
		vect=0
		break_point=0
		for j in range (len(table[i])):
			vect=vect+M[j]*table[i][j]
		for j in range (len(vect)):
			X.append(vect[j])
		for j in range (len(vect)):
			if(X[j]%2!=0 or X==extra_list):
				break_point=1
				X=[]
				break
		if(break_point==0):
			X_vect=table[i]
			break
	if(X==[]):
		return (0, 0, 0, X, X_vect)

	X_var=1
	X_var = np.array(X_var, dtype=np.float64)
	Y_var=1
	Y_var = np.array(Y_var, dtype=np.float64)
	for i in range (B2_length):
		X_var=(X_var*pow(b[i+2],X_vect[i]))%n
	for i in range (B_length):
		E=(pow(B[i],X[i]))%n
		Y_var=(Y_var*E)%n
	Y_var=int(math.sqrt(Y_var))
	new_i=table.index(X_vect)+1
	return (new_i, X_var, Y_var, X, X_vect)




def brilhart(n,l):
	B_set=[]
	alpha0 = pow(n,1/2)
	a0=int(alpha0)
	l=int(l)
	for i in range(2, l+1):
		for j in range(2,int(pow(i,1/2))+1):
			if(i%j==0):
				break
		else:
			if(Lezhandr(n,i)==1):
				B_set.append(i)
	if(B_set.count(2)==0):
		B_set.insert(0,2)
	B_set.insert(0,-1)
	print("B={",B_set,"}")
	k=len(B_set)
	if(alpha0==a0):
		if(B_set.count(a0)>0):
			return a0
	v0=1
	A=[]
	A.append(a0)
	u0=a0
	b=[0,1]
	b0=a0*b[-1]+b[-2]
	b.append(b0)
	B2=[]
	b_2=pow(b0,2,n)
	if((n-b_2)<b_2):
		b_2=b_2-n
	B2.append(b_2)
	while(k!=0):
		v0=(n-pow(u0,2))/v0
		alpha=(alpha0+u0)/v0
		a0=int(alpha)
		A.append(a0)
		u0=a0*v0-u0
		b0=a0*b[-1]+b[-2]
		b0=pow(b0,1,n)
		b.append(b0)
		b_2=pow(b0,2,n)
		if((n-b_2)<b_2):
			b_2=b_2-n
		B2.append(b_2)
		k=k-1
	print("b^2=",B2)
	print("b=",b)

	B_length=len(B_set)
	B2_length=len(B2)
	s_list=[]
	extra_list=[]
	for i in range (B2_length): #розклад на прості множники з B
		extra_list=(factorize(B_set,B2,B_length-1,B2[i],[]))
		if(B_set.count(extra_list[-1])==0):
			extra_list=[]
		s_list.append(extra_list)
	S=np.array(s_list)
	print("")
	print(S)

	zero_place=[]
	zero_number=[]
	empty_place=[]
	for i in range(len(s_list)):
		if(s_list[i]==[]): #empty vector
			empty_place.append(i) #запис місця, де знайшли порожній вектор
	for i in range(len(empty_place)-1,-1,-1): #зворотній проход циклу,
		#бо при прямому зламалася б структура під час видалення ел-нтів
		s_list.pop(empty_place[i]) #видалення порожніх векторів
		B2.pop(empty_place[i]) #відповідне видалення елементів
		#з яких робився розклад
		b.pop(empty_place[i]+2)
	B2_length=len(B2)
	to_check_numbs=0
	for i in range (len(s_list)): #цикл на знаходження векторів
		#з унікальним множником (для подальшого видалення)
		to_check_numbs=s_list[i][-1] #розглядаємо останній ел-нт вектора
		numb_counter=1
		for j in range(len(s_list)):
			if(j==i):
				numb_counter=s_list[j].count(to_check_numbs)
			else:
				try:
					extra_counter=s_list[j].index(to_check_numbs)
					#якщо знаходиться ще один вектор з таким самим множником
					numb_counter=numb_counter+1
					break #завершуємо підцикл
				except ValueError:
					numb_counter=1
		if(numb_counter==1): #вектор, що має унікальний множник
			zero_place.append(to_check_numbs)
			zero_number.append(i) #запам'ятовуємо номер вектору
				
	for i in range(len(zero_place)):
		B_set.remove(zero_place[i])
	print("")
	print("B={",B_set,"}")
	for i in range(len(zero_number)-1,-1,-1):
		B2.pop(zero_number[i])
		s_list.pop(zero_number[i])
		b.pop(zero_number[i]+2)
	if(B2==[]):
		return 0
	print("b^2=",B2)
	S=np.array(s_list)
	print("")
	print(S)
	print("b=",b)
	B_length=len(B_set)
	B2_length=len(B2)
	
	m=[]#вектори степенів
	for i in range (B2_length):
		extra_list=[0]*B_length #створюємо вектор з нулів
		#розмір якого відповідає розміру факторної бази
		for j in range(len(s_list[i])):
			index = B_set.index(s_list[i][j]) #знаходження індексу
			#кожного елементу вектора у факторній базі
			extra_list[index]=extra_list[index]+1 #формування вектору степенів
		m.append(extra_list)

	zero_place=[0]*B_length #створюємо вектор з нулів
	#розмір якого відповідає розміру факторної бази
	for i in range(len(m)):
		for j in range(len(m[i])):
			zero_place[j]=zero_place[j]+m[i][j] #по факту додавання рядків
	for i in range(len(zero_place)-1,-1,-1): #зворотній проход циклу,
		#бо при прямому зламалася б структура під час видалення ел-нтів
		if(zero_place[i]==0): #видаляємо множник з факторної бази
			B_set.pop(i) #який жодного разу не був задіяний
	print("")
	print("B={",B_set,"}")
	B_length=len(B_set)
	m=[]
	for i in range (B2_length):
		extra_list=[0]*B_length
		for j in range(len(s_list[i])):
			index = B_set.index(s_list[i][j])
			extra_list[index]=extra_list[index]+1
		m.append(extra_list)
	M=np.array(m)
	print(M)
	
	X=[]#знаходження при яких х рівняння =0mod2
	X_vect=[]
	extra_list=[0]*B_length #створюємо вектор з нулів
	#розмір якого відповідає розміру факторної бази
	table = list(itertools.product([0, 1], repeat=B2_length))
	table_len=len(table)
	for i in range (table_len):
		vect=0
		break_point=0
		for j in range (len(table[i])):
			vect=vect+M[j]*table[i][j]
		for j in range (len(vect)):
			X.append(vect[j])
		for j in range (len(vect)):
			if(X[j]%2!=0 or X==extra_list):
				break_point=1
				X=[]
				break
		if(break_point==0):
			X_vect=table[i]
			break
	print("")
	print("X=",X)
	if(X==[]):
		return 0
	print("X_vect=",X_vect)

	X_var=1
	X_var = np.array(X_var, dtype=np.float64)
	Y_var=1
	Y_var = np.array(Y_var, dtype=np.float64)
	for i in range (B2_length):
		X_var=(X_var*pow(b[i+2],X_vect[i]))%n
	for i in range (B_length):
		E=(pow(B_set[i],X[i]))%n
		Y_var=(Y_var*E)%n
	print("X=",X_var)
	Y_var=int(math.sqrt(Y_var))
	print("Y=",Y_var)
	new_i=table.index(X_vect)+1

	while(True):
		if(X_var==Y_var or X_var==n-Y_var): #випадок Х==У або Х==-Уmodn
			new_i, X_var, Y_var, X, X_vect = calculating(table_len, B_length, table, B2_length, new_i, b, B_set, M, n)
			if(new_i==0): #якщо більше не знайдено вектора, що дає відповідь
				return 0 #повертаємо 0 (показник того, що треба збільшити константу a)
		else:
			break

	sum_xy=(X_var+Y_var)%n
	d=Euclid(n, sum_xy)
	print("d=",d)
	while(True):
		if(d==1 or d==n): #випадок коли НСД дає тривіальний дільник(1 або n)
			new_i, X_var, Y_var, X, X_vect = calculating(table_len, B_length, table, B2_length, new_i, b, B_set, M, n)
			if(new_i==0):
				return 0
			if(X_var==Y_var or X_var==n-Y_var):
				new_i, X_var, Y_var, X, X_vect = calculating(table_len, B_length, table, B2_length, new_i, b, B_set, M, n)
				if(new_i==0): #якщо більше не знайдено вектора, що дає відповідь
					return 0 #повертаємо 0 (показник того, що треба збільшити константу a)
			sum_xy=(X_var+Y_var)%n
			d=Euclid(n, sum_xy)
		else:
			break
	print("")
	print("RESULT:")
	print(M)
	print("")
	print("X=",X)
	print("X_vect=",X_vect)
	print("X=",X_var)
	print("Y=",Y_var)
	print("d:",d)
	return int(d)




#start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def canon_decomp(n):

	#prime or complex
	decomposition=[]
	prime_p=False
	if(n%2==0 and n!=2):
		print(n,"is even!")
	else:
		print("Check number",n)
		prime_p=prime_number(n)
	if(prime_p==False):
		print("Number",n,"is complex!")
	else:
		print("Number",n,"is prime!")
		decomposition.append(n)
		return decomposition

	#trial division method
	print("To find divider of",n,":")
	p,q=division_method(n)
	if(p!=0):
		print(n,":{",p,"*",q,"}")
		decomposition.append(p)
	else:
		print("Number",n,"is prime!")
		decomposition.append(n)
		return decomposition
	prime_p=prime_number(q)
	if(prime_p==False):
		print("Number",q,"is complex!")
	else:
		print("Number",q,"is prime!")
		decomposition.append(q)
		return decomposition

	#Pollard method
	print("Check number by Pollard method:",q)
	p=pollard(q)
	print(q,":{",p,"*",int(q/p),"}")
	q=int(q/p)
	prime_p=prime_number(p)
	if(prime_p==False):
		print("Number",p,"is complex!")
		decomposition.append(canon_decomp(p))
	else:
		decomposition.append(p)
	prime_p=prime_number(q)
	if(prime_p==False):
		print("Number",q,"is complex!")
	else:
		print("Number",q,"is prime!")
		decomposition.append(q)
		return decomposition

	#Brilhart-Morris method
	print("Check number by Brilhart-Morris method:",q)
	alpha=1/(pow(2,1/2))
	L = math.exp(pow(math.log(q)*math.log(math.log(q)),1/2))
	l=pow(L,alpha)
	print("L=",l)
	p=brilhart(q,l)
	while(p==0):
		alpha=alpha+0.1
		l=pow(L,alpha)
		print("")
		print("L=",l)
		p=brilhart(q,l)
		print("p=",p)
	print(q,":{",p,"*",int(q/p),"}")
	q=int(q/p)
	prime_p=prime_number(p)
	if(prime_p==False):
		print("Number",p,"is complex!")
		decomposition.append(canon_decomp(p))
	else:
		decomposition.append(p)
	prime_p=prime_number(q)
	if(prime_p==False):
		print("Number",q,"is complex!")
		decomposition.append(canon_decomp(q))
		return decomposition
	else:
		print("Number",q,"is prime!")
		decomposition.append(q)
		return decomposition

def bm_border():
	n=int(input("Enter n:"))
	print("Check number by Brilhart-Morris method:",n)
	alpha=1/(pow(2,1/2))
	L = math.exp(pow(math.log(n)*math.log(math.log(n)),1/2))
	l=pow(L,alpha)
	print("L=",l)
	start_time = datetime.now()
	p=brilhart(n,l)
	print("Time is: "+str(datetime.now() - start_time))
	while(p==0):
		alpha=alpha+0.1
		l=pow(L,alpha)
		print("")
		print("L=",l)
		start_time = datetime.now()
		p=brilhart(n,l)
		print("Time is: "+str(datetime.now() - start_time))
		print("p=",p)
	q=int(n/p)
	print(n,":{",p,"*",q,"}")

def pollard_time():
	n=int(input("Enter n:"))
	print("Check number by Pollard method:",n)
	start_time = datetime.now()
	p=pollard(n)
	print("Time is: "+str(datetime.now() - start_time))
	q=int(n/p)
	print(n,":{",p,"*",q,"}")


def get_csv_number(name):
	with open(name) as f:
		reader=csv.reader(f)
		x=[]
		for row in reader:
			if(row[0]=="n"):
				continue
			x.append(int(row[0]))
	print("Numbers to factorize:",x)
	return x

def write_csv_numb(result):
	with open("cp_1_output.csv","w", newline='') as f:
		writer=csv.writer(f)
		for n in result:
			writer.writerow(n)

def start():
	while True:
		x=input("Do you want to use csv file to enter numbers or enter in program(1 - csv, 2 - in prog, 0 - exit):")
		if (x=="1"):
			print("csv")
			#list=get_csv (from test.py)
			name=input("Enter the way to your csv file:")
			numbers=get_csv_number(name)
			all_lists=[]
			for n in numbers:
				decomposition=[]
				decomposition=canon_decomp(n)
				print("Canonical decomposition of",n,":",decomposition)
				all_lists.append(decomposition)
			result=np.array(all_lists)
			write_csv_numb(result)
		elif (x=="2"):
			n=input("Enter n:")
			n=int(n)
			decomposition=[]
			decomposition=canon_decomp(n)
			print("Canonical decomposition of",n,":",decomposition)
		elif(x=="0"):
			print("Goodbye...")
			return 0
		else:
			print("Only option 1 or 2!!!")

	
#bm_border()
#pollard_time()
start()


