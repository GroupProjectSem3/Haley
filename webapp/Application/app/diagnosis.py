from .models import Disease, Disease_symptom,Symptom_detail
from django.core.cache import cache
from .symptomEnum import symptomEnum

class Diagnosis:

    @staticmethod
    def symptomWithWeightExists(symptom_detail_List,sId,sWeight):
        isExists = False
        for symp_det in symptom_detail_List:
            #symp_det_data = symp_det.to_dict()
            if(symp_det['symptom_id'] == sId and symp_det['weight'] == sWeight):
                isExists = True
                
        return isExists 


# new one based on concatenation
    @staticmethod
    def getNextSymptom(request,disease_symptoms_list,sId,sWeight):
        if(request.session.has_key('completedSymp')):
            completedSymp = request.session['completedSymp']
        else:
            completedSymp = list()
        tempList = list()
        finishedSymp = dict()
        completedSymp.append(sId)

        # Change the sId and sWeight to previous symptom (which has weight not 0)
        for dis_symp in disease_symptoms_list:
                #if(Diagnosis.symptomWithWeightExists(dis_symp.symptom_details,sId,sWeight)):
                    #tempList.append(dis_symp)
            for symp_det in dis_symp.symptom_details:
                if(symp_det['symptom_id'] !=sId and symp_det['symptom_id'] not in completedSymp):
                    if(symp_det['symptom_id'] in finishedSymp):
                        finishedSymp[symp_det['symptom_id']] += symp_det['weight']
                    else:
                        finishedSymp[symp_det['symptom_id']] = symp_det['weight']
        
        request.session['completedSymp'] = completedSymp
            #request.session['previous_symptom_list'] = finishedSymp
            # if(tempList.__len__()>0):
            #     cache.set('disease_symptom_list',tempList)
        if(completedSymp.__len__()==5):
            return "SUBMITNOW"
        elif(finishedSymp.__len__()>0):
            nextSymptom = max(finishedSymp, key=finishedSymp.get)
            print(nextSymptom)
            max_value = max(finishedSymp.values())  # maximum value
            max_keys = [k for k, v in finishedSymp.items() if v == max_value]
            return max_keys[0]
        else:
            return "SUBMITNOW" 


    @staticmethod
    def saveUserDiagnosis():
        dis_sym = Disease_symptom()
        dis_sym.symptom_details=[]
        dis_sym.save()

    @staticmethod
    def clearCacheAndSession(request):
        # cache
        cache.delete('disease_symptom_list')
        # Session
        if(request.session.has_key('completedSymp')):
            del request.session['completedSymp']
        if(request.session.has_key('response_list')):
            del request.session['response_list']  
        # if(request.session.has_key('previous_symptom_list')):
        #     del request.session['previous_symptom_list']        


    @staticmethod
    def splitDescription(fullDesc):
        desc = list()
        count = len(fullDesc.split())
        part1 = fullDesc.rsplit(" ",count-15)[0]
        part2 = fullDesc[len(part1):]
        desc.append(part1)
        desc.append(part2)
        return desc
