calc = {
	'add': lambda x,y:x+y,
	'del': lambda x,y:y!=0 and x/y,
}

print( calc['add'](2,3) )
print( calc['del'](2,3) )