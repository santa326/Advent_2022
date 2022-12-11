with open("A2.txt") as file:
    lines = [line.rstrip() for line in file]

#print(lines)

steps = []
for step in lines:
    steps.append(step.split(' '))

cycle = 0
X = 1
report = []
for i in steps:
    #print(i)
    if i[0] == 'noop':
        cycle = cycle + 1
        report.append([cycle,X])
    if i[0] == 'addx':
        cycle = cycle + 1
        report.append([cycle,X])
        cycle = cycle + 1
        X = X+int(i[1])
        report.append([cycle,X])
    


#for j in report:
    #print(j)

Input = [20,60,100,140,180,220]\

Q1 = 0

for k in range(0,len(Input)):
    current_cycle = Input[k]
    #we are getting last cycles value by subtracting 2 from index
    Q1 = Q1 + (report[current_cycle-2][1]*current_cycle)
    #print(current_cycle,'-',report[current_cycle-1][1])

print(Q1)

string = ''

sprite_posi = 0
sprite_posi_three = [sprite_posi-1,sprite_posi,sprite_posi+1]
current_pixel = 0



def draw(report,F,T):
    string = ''

    sprite_posi = 0
    sprite_posi_three = [sprite_posi-1,sprite_posi,sprite_posi+1]
    current_pixel = 0

    chop_report = report[int(F):int(T)]
    for l2 in range(0,40):
        if l2 in sprite_posi_three:
            string = string + '#'
        #print(l2+1,' spirit in position #' , sprite_posi)
        else:
            string = string + '.'
        #print(l2+1,' spirit in position .' , sprite_posi)
        sprite_posi = chop_report[l2][1]
        sprite_posi_three = [sprite_posi-1,sprite_posi,sprite_posi+1]
    #print(sprite_posi,)

    print(len(string),string)

draw(report,0,80)
draw(report,40,80)
draw(report,80,120)
draw(report,120,160)
draw(report,160,200)
draw(report,200,240)