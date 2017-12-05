import copy                                          #基本输入参数
num=int(input("the number of your disk line:"))
loc=int(input("currnet point location:"))
direc=input("your direction of scan:")
sum_list=[]
sum_list1=[]
sum_dict={}
sum_list2=[]
sub=[]
disk_line=[]
for i in range(num):
    diskline=int(input("disk line number:"))
    disk_line.append(diskline)




print ("---------FCFS--------")                   #先来先服务
sum_list.append(abs(disk_line[0]-loc))            #第一个磁道的寻道时间
for i in range(num):
    print ("the number %d line is : %d" % (i,disk_line[i]))
    if i+1<num:
        sum_list.append(abs(disk_line[i]-disk_line[i+1])) #之后所有磁道寻道时间
print ("the whole road:%d" % sum(sum_list))



print ("---------the most short find--------:")   #最短寻道优先
disk_line_c=copy.deepcopy(disk_line)              #输入参数副本
loc1=loc
def findmin(disk_line_c,loc1):                    #查找当前副本中与当前磁头最近距离的磁道，返回寻道时间
    for i in disk_line_c:
        sum_dict[abs(i-loc1)]=i
    sub=sum_dict.keys()
    return min(sub)
while (len(disk_line_c)>0):                       
    k=findmin(disk_line_c,loc1)                   
    sum_list2.append(k)                            #存储寻道时间
    loc1=sum_dict[k]                               #更新当前磁头
    print ("the line is: %d " % loc1)              #输出当前磁头
    disk_line_c.remove(sum_dict[k])                #删除已经寻到的磁道 
    sum_dict={}                                    #初始化存储字典
print ("the whole line is : %d " % sum(sum_list2))



print ("---------elevator of up----------")     #电梯上升法
disk_line.sort()                                #排序
tmp=0
for i in range(num):
    if disk_line[i]>=loc:
        print ("the start location is :%d" % disk_line[i])   #寻找到当前距离磁头最近的磁道并输出
        tmp=disk_line[i]
        break
index=disk_line.index(tmp)
sum_list1.append(abs(tmp-loc))                  #存入当前磁道的寻道时间
for i in disk_line[index:num]:                  #以当前磁道index所在位置为起点，进行寻道计算
    print ("line is : %d" % i)
    if disk_line.index(i)+1<num:
        sum_list1.append(abs(i-disk_line[disk_line.index(i)+1]))  
t_list=disk_line[0:index]                       #以0为起点到index所在磁道进行寻道计算
t_list.reverse()                                #{0,index}长度的列表中元素逆置
sum_list1.append(abs(disk_line[num-1]-t_list[0]))
for i in t_list:                                #逆置后新列表进行寻道计算
    print ("line is: %d" % i)
    if t_list.index(i)+1<len(t_list):
        sum_list1.append(abs(i-t_list[t_list.index(i)+1]))
print ("the whole road:%d" % sum(sum_list1))
