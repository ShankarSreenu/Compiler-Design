#Grammer updated
#E' -> E
#E -> E + T  r1 
#E -> T      r2 
#T -> T * F  r3
#T -> F      r4
#F -> F ^ G  r5 
#F -> G      r6
#G -> - G    r7 
#G -> ( E )  r8
#G -> a      r9

def ShowActions(stack,action,input):
    for val in stack:
        print(val,end=" ")
    print("|",end=" ")
    print(action+"|",end="")
    print("input:",input)

head={'+':0,'*':1,'^':2,'-':3,'(':4,')':5,'a':6,'$':7,"E'":8,'E':9,'T':10,'F':11,'G':12}
prod={1:'E',2:'E',3:'T',4:'T',5:'F',6:'F',7:'G',8:'G',9:'G'}#reductions
prod_len={1:6,2:2,3:6,4:2,5:6,6:2,7:4,8:6,9:2} #len of productions stored 

#parse table stored in list
parse_table =   [
                        ['e', 	'e' ,	'e' ,	's5',	's6',	'e', 	's7',	'e', 	 'e',	1,	2,	3,	4],
                        ['s8',	'e',	'e', 	'e', 	'e', 	'e', 	'e', 	'acc', 'e',	'e',   'e',	'e', 	'e', ],	 
                        ['r2',	's9',	'e', 	'e', 	'e', 	'e', 	'e', 	'r2',	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['r4',	'r4',	's10','e', 	'e', 	'e', 	'e', 	'r4',	 'e',	'e',	'e',	'e', 	'e'], 
                        ['r6',	'r6',	'r6',	'e', 	'e', 	'e', 	'e', 	'r6',	 'e',	'e', 	'e', 	'e',	'e'], 
                        [ 'e',	 'e',	'e', 	's5',	's6',	'e', 	's7',	'e', 	 'e',	'e', 	'e',	'e', 	11],
                        ['e',	 'e',	'e', 	's16','s17',	'e', 	's18', 'e', 'e',	12	,13	,14	,15],
                        ['r9',	'r9',	'r9',	'e', 	'e', 	'e', 	'e', 	'r9',	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['e',	 'e',	'e', 	's5',	's6',	'e', 	's7',	'e' ,	 'e',	'e', 	19,	3,4],
                        ['e',	 'e',	'e',	's5',	's6',	'e', 	's7',	'e' ,	 'e',	'e', 	'e' ,	20,	4],
                        ['e',	 'e',	'e', 	's5',	's6',	'e', 	's7',	'e', 	 'e',	'e' ,	'e',	'e', 	21],
                        ['r7',	'r7',	'r7',	'e', 	'e', 	'e',	'e',	'r7', 	 'e',	'e', 	'e', 	'e',  'e'], 
                        ['s23',  'e',    'e' ,  'e',    'e' ,   's22',	'e', 	'e', 	 'e',	'e', 	'e',	'e', 	'e'], 
                        ['r2', 's24',	'e', 	'e', 	'e', 	'r2',	'e',	'e', 	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['r4',	'r4',	's25',	'e', 	'e', 	'r4',	'e', 	'e', 	 'e',	'e' ,	'e', 	'e', 	'e'], 
                        ['r6',	'r6',	'r6',	'e',	'e', 	'r6',	'e', 	'e', 	 'e',	'e', 	'e' ,	'e', 	'e'], 
                        ['e',	 'e',	'e', 	's16','s17','e', 	's18','e',	 'e',	'e', 	'e', 	'e', 	26],
                        ['e',	 'e',	'e', 	's16','s17','e', 	's18','e', 	 'e',	27,	13,	14,	15],
                        ['r9',	'r9',	'r9',	'e', 	'e', 	'r9',	'e', 	'e', 	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['r1',	's9',	'e', 	'e', 	'e', 	'e', 	'e', 	'r1',	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['r3',	'r3',	's10','e', 	'e', 	'e', 	'e', 	'r3',	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['r5',	'r5',	'r5',	'e', 	'e', 	'e', 	'e', 	'r5',	 'e',	'e',	'e', 	'e', 	'e'], 
                        ['r8',	'r8',	'r8',	'e', 	'e', 	'e', 	'e', 	'r8',	 'e',	'e', 	'e', 	'e',	'e'], 
                        [ 'e',	 'e',	'e', 	's16','s17','e', 	's18','e', 	 'e',	'e', 	28,	14,	15],
                        ['e',	 'e',	'e', 	's16','s17','e', 	's18','e', 	 'e',	'e', 	'e', 	29,	15],
                        ['e',	 'e',	'e', 	's16','s17','e', 	's18','e', 	 'e',	'e', 	'e', 	'e', 	30],
                        ['r7',	'r7',	'r7',	'e', 	 'e',	'r7',	'e', 	'e', 	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['s23','e','e', 	'e', 	 'e',	's31','e', 	'e', 	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['r1','s24',	'e', 	'e',	 'e',	'r1',	'e',	'e', 	 'e',	'e',	'e', 	'e', 	'e'], 
                        ['r3',	'r3',	's25','e', 	 'e',	'r3',	'e',	'e', 	 'e',	'e', 	'e', 	'e', 	'e'], 
                        ['r5',	'r5',	'r5',	'e',	 'e',	'r5',	'e', 	'e', 	 'e',	'e' ,	'e', 	'e', 	'e'], 
                        ['r8',	'r8',	'r8',	'e', 	 'e',	'r8',	'e', 	'e', 	 'e',	'e', 	'e', 	'e' ,	'e'],
                ]

stack=[]   #performs stack operations
print("enter string to parse")
input_string=input() #dont give spaces ex:- (2+-3)^2$
semantic_actions=[]  #performs semantic  operations
stack.append(0)
top=-1
i=0



#x,y row,col of parse table
#parse_table[x][y] gives action

while stack!=[] and i<len(input_string):
    x=stack[-1]
    s=input_string[i]
    if s not in ['+','*','-','(',')','^','$']:
        s=int(s)
    if type(s)==int:
        y=6 #if int go to 6 row
    else:
        y=head.get(s)

    if parse_table[x][y]=='e':
        print('error')
        break
    elif parse_table[x][y]=='acc':
        print('Parsing is success')
        break
    elif parse_table[x][y] in ['s'+str(j) for j in range(1,33)]:#if ex 's1'... shift on to stack
        val=parse_table[x][y]
        action=val
        stack.append(s)
        stack.append(int(val[1:]))
        semantic_actions.append(s)
        i=i+1
    elif parse_table[x][y] in ['r'+str(j) for j in range(1,20)]:#if ex 'r1'... reduce on to stack
        val=parse_table[x][y]
        action=val
        st=prod.get(int(val[1:]))
        n=prod_len.get(int(val[1:]))
        for z in range(0,n):
            stack.pop(top)

        if int(val[1:])==1:
            semantic_actions[top-2]=semantic_actions[top]+semantic_actions[top-2]
            semantic_actions.pop(top)
            semantic_actions.pop(top)
        if int(val[1:])==3:
            semantic_actions[top-2]=semantic_actions[top]*semantic_actions[top-2]
            semantic_actions.pop(top)
            semantic_actions.pop(top)
        if int(val[1:])==5:
            semantic_actions[top-2]=semantic_actions[top-2]**semantic_actions[top]
            semantic_actions.pop(top)
            semantic_actions.pop(top)
        if int(val[1:])==7:
            semantic_actions[top-1]=-semantic_actions[top]
            semantic_actions.pop(top)
        
        if int(val[1:])==8:
            semantic_actions[top-2]=semantic_actions[top-1]
            semantic_actions.pop(top)
            semantic_actions.pop(top)

        stack.append(st)
        n=len(stack)
        x=stack[n-2]
        y=head.get(st)
        stack.append(parse_table[x][y])
    ShowActions(stack,action,input_string[i:])
print("caluculated value=",semantic_actions[-1])
