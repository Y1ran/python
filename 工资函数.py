
#用户的薪资输入水平>=0
#超出40小时的工时按1.5倍工资计算


def computepay():
    try: 
        pay1 = raw_input("Please Enter your Hours:")
        work_hours = float(pay1)
        pay2= raw_input("Please Enter your Rate:")
        work_salary = float(pay2)
    except:
        print "Error, please enter a numeric input"
        quit()
    #This is only for workers < 40hs
    if work_hours >= 40:
        overtime_pay = (work_hours - 40) * work_salary * 1.5
        total_pay = overtime_pay + work_salary * 40
        return total_pay
    else:
        only_pay = work_hours * work_salary
        return only_pay
print computepay()