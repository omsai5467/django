from django.shortcuts import render

def back(request):
    return render(request,'home.html')







# reate your views here.
def home(request):
    return render(request,'home.html')


def search(request):
    rollnumber=request.POST['ht']
    if rollnumber=='179m1a0201':
        return render(request,'re.html',{'rollnumber':rollnumber,
                                            
                                          'studentname':'Bhargavi',
                                          'ELECTRICAL_MEASUREMENTS_marks':'39',
                                          'total_marks_ELECTRICAL_MEASUREMENTS':'64',
                                          'result_ELECTRICAL_MEASUREMENTS':'P',
                                          'credits_ELECTRICAL_MEASUREMENTS':'3',
                                          'grade_ELECTRICAL_MEASUREMENTS':'C',
                                          'ELECTRICAL_POWER_TRANSMISSION_SYSTEMS_marks':'33',
                                          'total_marks_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'61',
                                          'result_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'p',
                                          'credits_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'3',
                                          'grade_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'C',
                                          'marks_POWER_ELECTRONICS':'25',
                                          'total_marks_POWER_ELECTRONICS':'53',
                                          'result_POWER_ELECTRONICS':'P',
                                          'credits_POWER_ELECTRONICS':'3',
                                          'grade_POWER_ELECTRONICS':'D',
                                          'marks_ELECTRICAL_MACHINES':'10',
                                          'total_marks_ELECTRICAL_MACHINES':'35',
                                          'result_ELECTRICAL_MACHINES':'P',
                                          'credits_ELECTRICAL_MACHINES':'3',
                                          'grade_ELECTRICAL_MACHINES':'F',
                                          'marks_LINEAR_DIGITAL_IC_APPLICATIONS':'40',
                                          'total_marks_LINEAR_DIGITAL_IC_APPLICATIONS':'65',
                                          'result_LINEAR_DIGITAL_IC_APPLICATIONS':'Q',
                                          'credits_LINEAR_DIGITAL_IC_APPLICATIONS':'5',
                                          'grade_LINEAR_DIGITAL_IC_APPLICATIONS':'A',
                                          'marks_DIGITAL_CIRCUITS_SYSTEMS':'55',
                                          'total_marks_DIGITAL_CIRCUITS_SYSTEMS':'100',
                                          'result_marks_DIGITAL_CIRCUITS_SYSTEMS':'Q',
                                          'credits_marks_DIGITAL_CIRCUITS_SYSTEMS':'5',
                                          'grade_marks_DIGITAL_CIRCUITS_SYSTEMS':'A'
                                            })
    elif rollnumber == '179m1a0202' :
        return render(request,'re.html',{'rollnumber':rollnumber,
                                            
                                          'studentname':'Ganesh',
                                          'ELECTRICAL_MEASUREMENTS_marks':'39',
                                          'total_marks_ELECTRICAL_MEASUREMENTS':'64',
                                          'result_ELECTRICAL_MEASUREMENTS':'P',
                                          'credits_ELECTRICAL_MEASUREMENTS':'3',
                                          'grade_ELECTRICAL_MEASUREMENTS':'C',
                                          'ELECTRICAL_POWER_TRANSMISSION_SYSTEMS_marks':'33',
                                          'total_marks_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'61',
                                          'result_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'p',
                                          'credits_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'3',
                                          'grade_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'C',
                                          'marks_POWER_ELECTRONICS':'25',
                                          'total_marks_POWER_ELECTRONICS':'53',
                                          'result_POWER_ELECTRONICS':'P',
                                          'credits_POWER_ELECTRONICS':'3',
                                          'grade_POWER_ELECTRONICS':'D',
                                          'marks_ELECTRICAL_MACHINES':'10',
                                          'total_marks_ELECTRICAL_MACHINES':'35',
                                          'result_ELECTRICAL_MACHINES':'P',
                                          'credits_ELECTRICAL_MACHINES':'3',
                                          'grade_ELECTRICAL_MACHINES':'A',
                                          'marks_LINEAR_DIGITAL_IC_APPLICATIONS':'40',
                                          'total_marks_LINEAR_DIGITAL_IC_APPLICATIONS':'65',
                                          'result_LINEAR_DIGITAL_IC_APPLICATIONS':'Q',
                                          'credits_LINEAR_DIGITAL_IC_APPLICATIONS':'5',
                                          'grade_LINEAR_DIGITAL_IC_APPLICATIONS':'A',
                                          'marks_DIGITAL_CIRCUITS_SYSTEMS':'55',
                                          'total_marks_DIGITAL_CIRCUITS_SYSTEMS':'100',
                                          'result_marks_DIGITAL_CIRCUITS_SYSTEMS':'Q',
                                          'credits_marks_DIGITAL_CIRCUITS_SYSTEMS':'5',
                                          'grade_marks_DIGITAL_CIRCUITS_SYSTEMS':'A'
                                            })
    elif rollnumber == '179m1a0204':
        return render(request,'re.html',{'rollnumber':rollnumber,
                                            
                                          'studentname':'Omsai',
                                          'ELECTRICAL_MEASUREMENTS_marks':'39',
                                          'total_marks_ELECTRICAL_MEASUREMENTS':'64',
                                          'result_ELECTRICAL_MEASUREMENTS':'P',
                                          'credits_ELECTRICAL_MEASUREMENTS':'3',
                                          'grade_ELECTRICAL_MEASUREMENTS':'C',
                                          'ELECTRICAL_POWER_TRANSMISSION_SYSTEMS_marks':'33',
                                          'total_marks_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'61',
                                          'result_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'p',
                                          'credits_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'3',
                                          'grade_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'C',
                                          'marks_POWER_ELECTRONICS':'25',
                                          'total_marks_POWER_ELECTRONICS':'53',
                                          'result_POWER_ELECTRONICS':'P',
                                          'credits_POWER_ELECTRONICS':'3',
                                          'grade_POWER_ELECTRONICS':'D',
                                          'marks_ELECTRICAL_MACHINES':'10',
                                          'total_marks_ELECTRICAL_MACHINES':'35',
                                          'result_ELECTRICAL_MACHINES':'P',
                                          'credits_ELECTRICAL_MACHINES':'3',
                                          'grade_ELECTRICAL_MACHINES':'A',
                                          'marks_LINEAR_DIGITAL_IC_APPLICATIONS':'40',
                                          'total_marks_LINEAR_DIGITAL_IC_APPLICATIONS':'65',
                                          'result_LINEAR_DIGITAL_IC_APPLICATIONS':'Q',
                                          'credits_LINEAR_DIGITAL_IC_APPLICATIONS':'5',
                                          'grade_LINEAR_DIGITAL_IC_APPLICATIONS':'A',
                                          'marks_DIGITAL_CIRCUITS_SYSTEMS':'55',
                                          'total_marks_DIGITAL_CIRCUITS_SYSTEMS':'100',
                                          'result_marks_DIGITAL_CIRCUITS_SYSTEMS':'Q',
                                          'credits_marks_DIGITAL_CIRCUITS_SYSTEMS':'5',
                                          'grade_marks_DIGITAL_CIRCUITS_SYSTEMS':'A'
                                            })
    elif rollnumber == '179m1a0205':
        return render(request,'re.html',{'rollnumber':rollnumber,
                                            
                                          'studentname':'Chukka sathish',
                                          'ELECTRICAL_MEASUREMENTS_marks':'39',
                                          'total_marks_ELECTRICAL_MEASUREMENTS':'64',
                                          'result_ELECTRICAL_MEASUREMENTS':'P',
                                          'credits_ELECTRICAL_MEASUREMENTS':'3',
                                          'grade_ELECTRICAL_MEASUREMENTS':'C',
                                          'ELECTRICAL_POWER_TRANSMISSION_SYSTEMS_marks':'33',
                                          'total_marks_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'61',
                                          'result_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'p',
                                          'credits_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'3',
                                          'grade_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'C',
                                          'marks_POWER_ELECTRONICS':'25',
                                          'total_marks_POWER_ELECTRONICS':'53',
                                          'result_POWER_ELECTRONICS':'P',
                                          'credits_POWER_ELECTRONICS':'3',
                                          'grade_POWER_ELECTRONICS':'D',
                                          'marks_ELECTRICAL_MACHINES':'10',
                                          'total_marks_ELECTRICAL_MACHINES':'35',
                                          'result_ELECTRICAL_MACHINES':'P',
                                          'credits_ELECTRICAL_MACHINES':'3',
                                          'grade_ELECTRICAL_MACHINES':'A',
                                          'marks_LINEAR_DIGITAL_IC_APPLICATIONS':'40',
                                          'total_marks_LINEAR_DIGITAL_IC_APPLICATIONS':'65',
                                          'result_LINEAR_DIGITAL_IC_APPLICATIONS':'Q',
                                          'credits_LINEAR_DIGITAL_IC_APPLICATIONS':'5',
                                          'grade_LINEAR_DIGITAL_IC_APPLICATIONS':'A',
                                          'marks_DIGITAL_CIRCUITS_SYSTEMS':'55',
                                          'total_marks_DIGITAL_CIRCUITS_SYSTEMS':'100',
                                          'result_marks_DIGITAL_CIRCUITS_SYSTEMS':'Q',
                                          'credits_marks_DIGITAL_CIRCUITS_SYSTEMS':'5',
                                          'grade_marks_DIGITAL_CIRCUITS_SYSTEMS':'A'
                                            })
    elif rollnumber == '179m1a0206':
      return render(request,'re.html',{'rollnumber':rollnumber,
                                            
                                          'studentname':'Thippineni Thirupal',
                                          'ELECTRICAL_MEASUREMENTS_marks':'39',
                                          'total_marks_ELECTRICAL_MEASUREMENTS':'64',
                                          'result_ELECTRICAL_MEASUREMENTS':'P',
                                          'credits_ELECTRICAL_MEASUREMENTS':'3',
                                          'grade_ELECTRICAL_MEASUREMENTS':'C',
                                          'ELECTRICAL_POWER_TRANSMISSION_SYSTEMS_marks':'33',
                                          'total_marks_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'61',
                                          'result_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'p',
                                          'credits_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'3',
                                          'grade_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'C',
                                          'marks_POWER_ELECTRONICS':'25',
                                          'total_marks_POWER_ELECTRONICS':'53',
                                          'result_POWER_ELECTRONICS':'P',
                                          'credits_POWER_ELECTRONICS':'3',
                                          'grade_POWER_ELECTRONICS':'D',
                                          'marks_ELECTRICAL_MACHINES':'10',
                                          'total_marks_ELECTRICAL_MACHINES':'35',
                                          'result_ELECTRICAL_MACHINES':'P',
                                          'credits_ELECTRICAL_MACHINES':'3',
                                          'grade_ELECTRICAL_MACHINES':'A',
                                          'marks_LINEAR_DIGITAL_IC_APPLICATIONS':'40',
                                          'total_marks_LINEAR_DIGITAL_IC_APPLICATIONS':'65',
                                          'result_LINEAR_DIGITAL_IC_APPLICATIONS':'Q',
                                          'credits_LINEAR_DIGITAL_IC_APPLICATIONS':'5',
                                          'grade_LINEAR_DIGITAL_IC_APPLICATIONS':'A',
                                          'marks_DIGITAL_CIRCUITS_SYSTEMS':'55',
                                          'total_marks_DIGITAL_CIRCUITS_SYSTEMS':'100',
                                          'result_marks_DIGITAL_CIRCUITS_SYSTEMS':'Q',
                                          'credits_marks_DIGITAL_CIRCUITS_SYSTEMS':'5',
                                          'grade_marks_DIGITAL_CIRCUITS_SYSTEMS':'A'
                                            })
    elif rollnumber == '179m1a0208':
      return render(request,'re.html',{'rollnumber':rollnumber,
                                            
                                          'studentname':'Laxmi devi',
                                          'ELECTRICAL_MEASUREMENTS_marks':'39',
                                          'total_marks_ELECTRICAL_MEASUREMENTS':'64',
                                          'result_ELECTRICAL_MEASUREMENTS':'P',
                                          'credits_ELECTRICAL_MEASUREMENTS':'3',
                                          'grade_ELECTRICAL_MEASUREMENTS':'C',
                                          'ELECTRICAL_POWER_TRANSMISSION_SYSTEMS_marks':'33',
                                          'total_marks_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'61',
                                          'result_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'p',
                                          'credits_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'3',
                                          'grade_ELECTRICAL_POWER_TRANSMISSION_SYSTEMS':'C',
                                          'marks_POWER_ELECTRONICS':'25',
                                          'total_marks_POWER_ELECTRONICS':'53',
                                          'result_POWER_ELECTRONICS':'P',
                                          'credits_POWER_ELECTRONICS':'3',
                                          'grade_POWER_ELECTRONICS':'D',
                                          'marks_ELECTRICAL_MACHINES':'10',
                                          'total_marks_ELECTRICAL_MACHINES':'35',
                                          'result_ELECTRICAL_MACHINES':'P',
                                          'credits_ELECTRICAL_MACHINES':'3',
                                          'grade_ELECTRICAL_MACHINES':'A',
                                          'marks_LINEAR_DIGITAL_IC_APPLICATIONS':'40',
                                          'total_marks_LINEAR_DIGITAL_IC_APPLICATIONS':'65',
                                          'result_LINEAR_DIGITAL_IC_APPLICATIONS':'Q',
                                          'credits_LINEAR_DIGITAL_IC_APPLICATIONS':'5',
                                          'grade_LINEAR_DIGITAL_IC_APPLICATIONS':'A',
                                          'marks_DIGITAL_CIRCUITS_SYSTEMS':'55',
                                          'total_marks_DIGITAL_CIRCUITS_SYSTEMS':'100',
                                          'result_marks_DIGITAL_CIRCUITS_SYSTEMS':'Q',
                                          'credits_marks_DIGITAL_CIRCUITS_SYSTEMS':'5',
                                          'grade_marks_DIGITAL_CIRCUITS_SYSTEMS':'A'
                                            })
    else :
      return render(request,'home.html',{'hall_ticket':'invalid hallticket number'})
      
      

        
        
   
                                           
       
        



  
       