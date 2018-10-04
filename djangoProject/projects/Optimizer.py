import numpy as np              
import cvxpy as cvx
import pandas as pd

def norm_var(variable, min_value=1, max_value=5):
    return (variable - min_value)/(max_value - min_value)


def def_avail(xVector, avail, weeks_required, weight):
    """
    Inputs: 
    xVector is a 1D cvx vector variable object of boolean variables. Size is equal to number of associates.
    avail is a 2D array containing associate availability over n subsequent weeks. 
    
    Outputs:
    
    """
    #Check vector sizes
    if xVector.shape[0] != avail.shape[0]:
        print('Error: xVector length not equal to number of associate records')
        return None

    #Check partnerRs type - If series (1 partner)
    if type(avail) == pd.core.series.Series:
        #First check ptnr_w has only 1 entry
        if weeks_required != 1:
            print('Error: Multiple weeks required but only 1 week record found')
            return None
        #Then change to dataframe
        else:
            avail = pd.DataFrame(avail, columns = ['Week1'])
    
    
    #Initiate results
    variables = {}
    constraints = []
    
    for i in range(weeks_required):
        col = 'avail_wk' + str(i+1)
        #Get a single avail week vector
        singleAw = avail[col]
        
        #Create variable
        variables[col] = cvx.Variable()
        #Define variable
        
            
        constraints.extend([weight * xVector.T * norm_var(np.array([5 for i in range(len(singleAw))]) - np.array(singleAw)) == variables[col]])
    
    return variables, constraints 

def def_clientR(xVector, clientRs, client_w):   #CHANGED!!!!!!###############################################
    """
    Inputs:
    xVector is a 1D cvx vector variable object of boolean variables. Size is equal to number of associates.
    clientRs is a 1D array or Series containing client relationships of each associate.
    
    Outputs:
    Returns a cvx variable list and a cvx constraint list (an equality defining the variable)
    """

    #Check client type - If series (1 client)
    if type(clientRs) == pd.core.series.Series:
        #First check ptnr_w has only 1 entry
        if len(client_w) != 1:
            print('Error: Multiple weights given but only 1 partner record found')
            return None
        #Then change to dataframe
        else:
            clientRs = pd.DataFrame(clientRs, columns = list(client_w.keys()))
    
    
    #Initiate results
    variables = {}
    constraints = []
    
    for client in client_w.keys():
        #Get a single partner column
        singleRs = clientRs[client]
        
        #Create single partner variable and append
        variables[client] = cvx.Variable()
        #Create definition constraint for single partner and append
        constraints.extend([client_w[client] * xVector.T * norm_var(np.array([5 for i in range(len(singleRs))]) - np.array(singleRs)) == variables[client]])
    
    return variables, constraints


def def_partnerR(xVector, partnerRs, ptnr_w):
    """
    Inputs:
        xVector is a 1D cvx vector variable object of boolean variables. Size is equal to number of associates.
        partnerRs is a Series or DataFrame containing partner-associate relations. Rows are associates, columns are partners. 
        ptnr_w is a dictionary indicating weights for partners
    
    Outputs:
        Returns a list cvx variables and a list of cvx constraints (equalities defining the variables)
    """

    #Check partnerRs type - If series (1 partner)
    if type(partnerRs) == pd.core.series.Series:
        #First check ptnr_w has only 1 entry
        if len(ptnr_w) != 1:
            print('Error: Multiple weights given but only 1 partner record found')
            return None
        #Then change to dataframe
        else:
            partnerRs = pd.DataFrame(partnerRs, columns = list(ptnr_w.keys()))
    
    
    #Initiate results
    variables = {}
    constraints = []
    
    for partner in ptnr_w.keys():
        #Get a single partner column
        singleRs = partnerRs[partner]
        
        #Create single partner variable and append
        variables[partner] = cvx.Variable()
        #Create definition constraint for single partner and append
        constraints.extend([ptnr_w[partner] * xVector.T * norm_var(np.array([5 for i in range(len(singleRs))]) - np.array(singleRs)) == variables[partner]])
    
    return variables, constraints


def def_skills(xVector, skills, skill_w):
    """
    Inputs:
        xVector is a 1D cvx vector variable object of boolean variables. Size is equal to number of associates.
        skills is a Series or DataFrame containing associate skill levels. Rows are associates, columns are skills. 
        skill_w is a dictionary indicating weights for each skill
    
    Outputs:
    Returns a list cvx variables and a list of cvx constraints (equalities defining the variables)
    """
    #Check vector sizes


    #Check skills table type - If series (1 partner)
    if type(skills) == pd.core.series.Series:
        #First check ptnr_w has only 1 entry
        if len(skill_w) != 1:
            print('Error: Multiple weights given but only 1 skill record found')
            return None
        #Then change to dataframe
        else:
            skills = pd.DataFrame(skills, columns = list(skill_w.keys()))
    
    
    #Initiate results
    variables = {}
    constraints = []
    
    for sk in skill_w.keys():
        #Get a single skill column
        singlesk = skills[sk]
        
        #Create single skill variable and append
        variables[sk] = cvx.Variable()
        #Create definition constraint for single partner and append
        constraints.extend([skill_w[sk] * xVector.T * norm_var(np.array([5 for i in range(len(singlesk))]) - np.array(singlesk)) == variables[sk]])
    
    return variables, constraints


def calc_weights(weights_dict):     #CHANGED!!!!!!###############################################
    """"
    weights_dict has 4 types of keys; values are importance:
        availability
        client
        partner_X
        skill_X
    """
    #Get total weight / importances
    tot_w = sum(abs(w) for w in weights_dict.values())
    
    #Initiate results
    avail = weights_dict['availability']/tot_w
    client = {}
    partners = {}
    skills = {}
    
    for k,v in weights_dict.items():
        if 'partner_' in k:
            partners[k] = v/tot_w
        elif 'skill_' in k:
            skills[k] = v/tot_w
        elif 'client_' in k:
            skills[k] = v/tot_w
    
    return avail, client, partners, skills


def compile_objectives(obj_dict):
    #Initiate final objective list
    finalObj_list = []
    
    #Add key items to finalObjlist
    for var in obj_dict.values():
        finalObj_list.append(var)
        
    return cvx.Minimize(sum(finalObj_list))


def add_variable_absHC(xVector, data_table, limits):
    """
    Inputs:
        xVector as above
        partnerR as above
        ptnr_limits is a dictionary of dictionaries, keys being partner names, subdict taking the form {'min': x, 'max': x}
    """
    #Check vectors
    if xVector.shape[0] != data_table.shape[0]:
        print('Error: xVector length not equal to number of associate records')
        return None

    #Check partnerRs type - If series (1 partner)
    if type(data_table) == pd.core.series.Series:
        #First check ptnr_w has only 1 entry
        if len(limits) != 1:
            print('Error: Multiple weights given but only 1 variable found')
            return None
        #Then change to dataframe
        else:
            data_table = pd.DataFrame(data_table, columns = list(limits.keys()))    
    
    
    #Initiate results
    auxVars = []
    HClist = []

    #Add min max for each partner
    for var in limits.keys():
        #Get single partner vector
        single_var = data_table[var]
                    
        try:
            #Get max variable level
            varmax = limits[var]['max']
            #Add max skill constraints for each person
            for x, V in zip(xVector, single_var):
                HClist.append(V*x <= varmax)
        except KeyError:
            pass

        try:
            #Get min variable level
            varmin = limits[var]['min']
            for x, V in zip(xVector, single_var):
                #Create auxillary variable
                auxVars.append(cvx.Variable(boolean=True))
                #Make 0 or at least min_sk
                HClist.extend([V*x <= 0 + 500*auxVars[-1],
                               V*x >= varmin - 500*auxVars[-1]])
        except KeyError:
            pass
            
    return auxVars, HClist


