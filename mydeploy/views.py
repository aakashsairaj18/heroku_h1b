from django.shortcuts import render
import joblib
import pickle
def page01(request):
    return render(request, "page01.html")

def page02(request):

    #cls = joblib.load('testing.sav')
    cls=pickle.load(open('Onetesting.sav', 'rb'))


    lis = []
    lis.append(float(request.GET['FULL_T']))
    lis.append(float(request.GET['TOTAL_WORKER_POSITIONS']))
    lis.append(float(request.GET['CHANGE_PREVIOUS_EMPLOYMENT']))
    lis.append(float(request.GET['NEW_CONCURRENT_EMPLOYMENT']))
    lis.append(float(request.GET['CHANGE_EMPLOYER']))
    lis.append(float(request.GET['AMENDED_PETITION']))
    lis.append(float(request.GET['AGENT_REPRESENTING_EMPLOYER']))
    lis.append(float(request.GET['H-1B_DEPENDENT']))
    lis.append(float(request.GET['WILLFUL_VIOLATOR']))

    sec_entity=["Secondary_Entity_1", "Secondary_Entity_2", "Secondary_Entity_3","Secondary_Entity_4","Secondary_Entity_5",
                "Secondary_Entity_6","Secondary_Entity_7","Secondary_Entity_8","Secondary_Entity_9","Secondary_Entity_10"]
    sum_sec=0
    for i in sec_entity:
        if '1'==request.GET[i]:
            sum_sec+=1
    lis.append(sum_sec)


    ans=cls.predict([lis])
    if ans==1:
        res="Higher"
    else:
        res="Lower"

    return render(request, "page02.html", {'res':res})