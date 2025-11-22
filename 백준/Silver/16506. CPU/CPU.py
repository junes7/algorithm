import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
opcode_machine = {'ADD':'0000', 'SUB':'0001', 'MOV':'0010', 'AND':'0011','OR':'0100',
                   'NOT':'0101','MULT':'0110', 'LSFTL':'0111', 'LSFTR':'1000',
                   'ASFTR':'1001','RL':'1010','RR':'1011'}
for i in range(n):
    input_data = input().split()
    machine_code = ''
    opcode = input_data[0]
    rd = input_data[1]
    ra = input_data[2]
    rb = input_data[3]
    if opcode[-1]=='C':
        machine_code += opcode_machine.get(opcode[:-1])
        machine_code += '1'
    else:
        machine_code += opcode_machine.get(opcode)
        machine_code += '0'
    machine_code += '0'
    machine_code+=str(bin(int(rd)))[2:].zfill(3)
    machine_code+=str(bin(int(ra)))[2:].zfill(3)
    if machine_code[4]=='0':
        machine_code+=str(bin(int(rb)))[2:].zfill(3)
        machine_code+='0'
    else:
        machine_code+=str(bin(int(rb)))[2:].zfill(4)  
    print(machine_code)