# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:05:22 2019

@author: Vaibhav
"""
import pandas as pd
import matplotlib.pyplot as plt

def delta_ratio(vector_1, vector_2):
    """
    Returns a list that contains
    ratios of change of vector_1 w.r.t vector_2
    """
    if (len(vector_1) == 1):
        return vector_1[0] / vector_2[0]
    
    else:
        ratios = []
        vector_1 = delta(vector_1)
        vector_2 = delta(vector_2)
        for index in range(len(vector_1)):
            delta_1 = vector_1[index]
            delta_2 = vector_2[index]
            ratios.append(delta_1 / delta_2)
        return ratios
    
def delta(vector):
    """
    Calculates the difference b/w adjacent elements 
    in a vector and returns it as a list
    """
    if (len(vector) <= 1):
        return 0
    
    else:
        result_vector = []
        for index in range(len(vector)-1):
            result_vector.append(vector[index+1] - vector[index])
        return result_vector
    
def delta_perc(vector):
    """
    Calculates the percentage change in value w.r.t previous
    value for all the elements of a list
    """
    if (len(vector) <= 1):
        return 0
    
    else:
        result_vector = []
        for index in range(len(vector)-1):
            result_vector.append((vector[index+1] - vector[index]) / vector[index])
        return result_vector
    
def delta_ratio_perc(vector_1, vector_2):
    """
    Returns a list that contains
    ratios of change of vector_1 w.r.t vector_2
    """
    if (len(vector_1) == 1):
        return vector_1[0] / vector_2[0]
    
    else:
        ratios = []
        vector_1 = delta_perc(vector_1)
        vector_2 = delta_perc(vector_2)
        for index in range(len(vector_1)):
            delta_1 = vector_1[index]
            delta_2 = vector_2[index]
            ratios.append(delta_1 / delta_2)
        return ratios
    
def normalize_ratios(ratios):
    """
    This normalize each tuple in ratios by
    dividing each element in the tuple by last 
    last element in that tuple. This is in place.
    """
    tuple_len = len(ratios[0])
    for tup_index in range(len(ratios)):
        for ratio_index in range(tuple_len):
            ratios[tup_index][ratio_index] /= ratios[tup_index][-1]
            
    
def weighted_mean(vec):
    """
    Returns the weighted mean of a vector based on
    weights provided by delta_weightage_mapping
    """
    vector = vec.copy()#just copying this vector
    vector.reverse()#reverse the list
    wtd_mean = vector[0];
    rng = max(vector) - min(vector)
    for index in range(1, len(vector)):
        w1, w2 = delta_weightage_mapping(wtd_mean, vector[index], rng, index + 1)
        wtd_mean = (w1 * wtd_mean) + (w2 * vector[index])
    return wtd_mean

def delta_weightage_mapping(val_1, val_2, rng, data_pnt_cnt):
    """
    Calculate the necessary weights to find the mean
    of the parameters. Can be modified to accomodate 
    the volatility in the data. rng parameter takes
    the diff b/w max and min value. data_pts_cnt takes
    the number of data points seen till yet.
    """
    if (val_1 == 0):
        return (1, 1)
    percentage_diff = (val_2 - val_1) / val_1
    percentage_diff = abs(percentage_diff) / rng
    percentage_diff = min(1, percentage_diff)
    w1 = (data_pnt_cnt - 1) / data_pnt_cnt
    w2 = (1 / data_pnt_cnt) + (percentage_diff) / rng
    return (w1, w2)

def predict_next_without_contr(vector):
    """
    Predict the next value of the vector based on 
    delta_weightage_mapping and without taking into 
    consideration any factor
    """
    delta_vector = delta(vector)
    #Calculate mean value of change
    wtd_mean_change = weighted_mean(delta_vector)
    wtd_val = weighted_mean(vector)
    #add wtd_mean_change to last val of vector
    predicted_val = wtd_val + wtd_mean_change
    return predicted_val

def predict_contributions(ratios):
    """
    Predict the contribution of each factor based 
    on delta_weightage_mapping
    """
#    normalize_ratios(ratios)
    factors_count = len(ratios[0])
    factor_contributions = []
    for factor in range(factors_count):
        fact_contr_values = [ratio[factor] for ratio in ratios]
        fact_contr = predict_next_without_contr(fact_contr_values)
        factor_contributions.append(fact_contr)
    return factor_contributions

def predict_next(data, next_factor_values):
    """
    Predict next value based on all the factors
    Assume last value of each row is value to be predicted.
    And all other values are factors
    """
    factors = len(data[0]) - 1
    factor_values = []
    for factor_index in range(factors):
        factor_values.append([row[factor_index] for row in data])
    disease_count  = [row[-1] for row in data]
    delta_ratios_perc_val = []
    for factor in factor_values:
        delta_ratios_perc_val.append(delta_ratio_perc(disease_count, factor))
    delta_ratios_perc_val = [list(row) for row in zip(*delta_ratios_perc_val)]
#    print("delta_ratios_perc", delta_ratios_perc_val)
    factor_contributions = predict_contributions(delta_ratios_perc_val)
#    print("factor_contri", factor_contributions)
    disease_predicted = 0
    sum_factor_contr = sum([abs(elem) for elem in factor_contributions])
    for factor_index in range(len(factor_contributions)):
        perc_chng = (next_factor_values[factor_index] - factor_values[factor_index][-1]) / factor_values[factor_index][-1]
        disease_predicted += factor_contributions[factor_index] * perc_chng / sum_factor_contr
#    print("disease predicted", disease_predicted)
    plot_graph(delta_ratios_perc_val, disease_count, (disease_predicted + 1) * disease_count[-1])

    return ((disease_predicted + 1) * disease_count[-1], factor_contributions)

def plot_graph(ratios, disease_count,predicted_value):
    """
    plot the graph based on all the factors
    """
    factors_count = len(ratios[0])
    factor_contributions = []
    for factor in range(factors_count):
        fact_contr_values = [ratio[factor] for ratio in ratios]
        factor_contributions.append(fact_contr_values)
    fig = plt.figure(figsize=(12,6))
    plt.plot(factor_contributions[0], label="temp")
    plt.plot(factor_contributions[1], label="rainfall")
    plt.plot(factor_contributions[2], label="pop dens")
    plt.plot(disease_count, label="disease")
    plt.plot([len(disease_count)],[predicted_value], marker='o', markersize=4, color="black",label="predicted value")
    plt.legend(loc=2)
    # plt.show()
    fig.savefig("output.png")
    
def predict(city, temp, rf, popdens):
    data = pd.read_csv("./Simulated_datasets/" + city + ".csv")
    data = data.drop(columns=["YEAR"], axis=1)
    data = data.values
    return predict_next(data, [temp, rf, popdens])

