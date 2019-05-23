import math,array,sys
class iter:
	def __init__(self,n) : self.i=0; self.n=n;
	def __next__(self) :
		if self.i>self.n-1 : raise StopIteration
		else : self.i+=1; return self.i-1


class vector (object) :

	def __init__ (self,n,t:type='d') :
		if(type(n) is int):
			self.size=n
			self.stride=1
			self.start=0
			self.data=array.array(t,[0.0]*n)
		if(type(n) is list):
			self.size=len(n)
			self.stride=1
			self.start=0
			self.data=array.array(t,[0.0]*len(n))
			for i in range(len(n)): self[i]=n[i]

	def get (self,i) : return self.data[self.start+self.stride*i]
	def set (self,i,x) : self.data[self.start+self.stride*i]=x
	def __getitem__ (self,i)   : return self.data[self.start+self.stride*i]
	def __setitem__ (self,i,x) : self.data[self.start+self.stride*i]=x

	def __iter__(self) : return iter(self.size)

	def __neg__(self) :
		v = vector(self.size)
		for i in range(v.size) : v[i]=-self[i]
		return v

	def copy (self):
		v=vector(self.size)
		for i in self: v[i]=self[i]
		return v

	def dot (self,other) :
		s = 0
		for i in self : s += self[i]*other[i]
		return s

	def outer (self,other) :
		M = matrix(self.size,other.size)
		for i in range(self.size) :
			for j in range(other.size) :
				M[i,j]=self[i]*other[j]
		return M


	def norm (self) :
		return math.sqrt(self.dot(self))

	def __add__ (self,other) :
		v = vector(self.size)
		for i in range(v.size) : v[i]=self[i]+other[i]
		return v

	def __sub__ (self,other) :
		v = vector(self.size)
		for i in range(v.size) : v[i]=self[i]-other[i]
		return v

	def __mul__ (self,other) :
		v = vector(self.size)
		for i in range(v.size) : v[i]=self[i]*other
		return v

	def __truediv__ (self,other) :
		return self*(1.0/other)

	def __rmul__ (self,other) :
		v = vector(self.size)
		for i in range(v.size) : v[i]=self[i]*other
		return v

	def set_basis(self,k) :
		for i in range(self.size) : self.set(i,0)
		self.set(k,1)

	def print(self,s="") :
		print(s,end="")
		for i in range(self.size) : print("{:10.4g} ".format(self[i]),end="")
		print()

import array
class matrix(object) :
	def __init__ (self,n:int,m:int,t:type='d') :
		self.size1=n
		self.size2=m
		self.data=array.array(t,[0.0]*(n*m))
	def set(self, i:int, j:int, x) :        self.data[i+self.size1*j] = x
	def get(self, i:int, j:int)    : return self.data[i+self.size1*j]

	def __getitem__ (self,k)   :
		if( type(k) is tuple ) :
			i,j=k;
			if type(i) is int   : return self.get(i,j)
			if type(i) is slice : return self[j]
		if type(k) is int :
			v=vector(0)
			v.size=self.size1
			v.data=self.data
			v.start=self.size1*k
			v.stride=1
			return v

	def set_col(self, k:int, v:vector):
			for i in range(self.size1) : self.set(i,k,v[i])

	def __setitem__ (self,k,v) :
		if( type(k) is tuple ) :
			i,j=k;
			if type(i) is int   : self.set(i,j,v)
			if type(i) is slice : self.set_col(j,v)
		if( type(k) is int ) : self.set_col(k,v)

	def copy(self) :
		A = matrix(self.size1,self.size2)
		for i in range(A.size1) :
			for j in range(A.size2) :
				A[i,j]=self[i,j]
		return A

	def __add__(self,other) :
		assert self.size1 == other.size1 and self.size2 == other.size2
		M = matrix(self.size1,self.size2)
		for i in range(self.size1) :
			for j in range(self.size2) :
				M.set(i,j, self.get(i,j)+other.get(i,j))
		return M

	def __mul__ (self,other) :
		if( type(other) is matrix ) :
			assert self.size2 == other.size1
			a = matrix(self.size1,other.size2)
			for i in range(a.size1) :
				for j in range(a.size2) :
					sum = 0
					for k in range(self.size2) : sum+=self.get(i,k)*other.get(k,j)
					a.set(i,j,sum)
			return a
		if( type(other) is vector ):
			assert self.size2==other.size
			x = vector(self.size1)
			for i in range(self.size1):
				s=0
				for k in range(self.size2):s+=self[i,k]*other[k]
				x[i]=s
			return x
		if( type(other) is float or int or complex ):
			a = matrix(self.size1,self.size2)
			for i in range(a.size1) :
				for j in range(a.size2) :
					a.set(i,j,self.get(i,j)*other)
			return a

	def __truediv__(self,other):
		return self*(1.0/other);

	def T(self) :
		a=matrix(self.size2,self.size1)
		for i in range(a.size1) :
			for j in range(a.size2) :
				a.set(i,j,self.get(j,i))
		return a

	def print(self,s="",stream=sys.stdout) :
		print(s,file=stream)
		for i in range(self.size1) :
			for j in range(self.size2) :
				print("{:10.3f} ".format(self.get(i,j)),end="",file=stream)
			print("",file=stream)

	def __eq__ (self,other) :
		if( self.size1 != other.size1 ) : return False
		if( self.size2 != other.size2 ) : return False
		def equal(a:float,b:float) :
			tiny=1e-6
			if abs(a-b) < tiny : return True
			if abs(a-b)/(abs(a)+abs(b)) < tiny : return True
			return False
		for i in range(self.size1) :
			for j in range(self.size2) :
				if( not equal(self.get(i,j),other.get(i,j)) ) : return False
		return True

	def id_matrix(n:int):
		a = matrix(n,n)
		a.set_identity()
		return a

	def unit_matrix(n:int):
		a = matrix(n,n)
		a.set_identity()
		return a

	def set_identity(self) :
		for i in range(self.size1) :
			self.set(i,i,1)
			for j in range(i+1,self.size2) :
				self.set(i,j,0)
				self.set(j,i,0)

	def back_substitute(self,b):
		if (type(b) is vector):
			assert self.size2==b.size
			x=vector(b.size)
			for i in reversed(range(self.size2)):
				s=0
				for k in range(i+1,x.size) : s+=self[i,k]*x[k]
				x[i]=(b[i]-s)/self[i,i]
			return x
		if (type(b) is matrix):
			x=matrix(b.size1,b.size2)
			for i in range(x.size2): x[i]=self.back_substitute(b[i])
			return x