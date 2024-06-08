#!/usr/bin/env python
# coding: utf-8

# # Estimating Causal Effect of Graduate Education on Income - Propensity Score-based Methods
# Code authored by: Shawhin Talebi <br />
# DoWhy Library: https://py-why.github.io/dowhy/v0.8/ <br />
# Data from: https://archive.ics.uci.edu/ml/datasets/census+income

# ### Import libraries

# In[1]:

import pickle

import dowhy
from dowhy import CausalModel
import numpy as np


# ### Load data

# In[2]:


df = pickle.load( open( "df_propensity_score.p", "rb" ) )


# In[3]:


print(df.head())
print("\n")


# ### Estimating Causal Effects with DoWhy

# #### Define causal model

# In[4]:


model=CausalModel(
        data = df,
        treatment= "hasGraduateDegree",
        outcome= "greaterThan50k",
        common_causes="age",
        )


# In[5]:


# # View model
# model.view_model()


# #### Generate estimand i.e. recipe for calculating causal effect

# In[6]:


identified_estimand= model.identify_effect(proceed_when_unidentifiable=True)
print(identified_estimand)
print("\n")


# #### Compute causal effect using 3 different propensity score-based approaches

# In[7]:


identified_estimand_experiment = model.identify_effect(proceed_when_unidentifiable=True)

# create list of names of the propensity score methods we want to use
ps_method_name_list = ["matching", "stratification", "weighting"]
# initalize dictionary to store estiamtes from each method and list to store ATEs
ps_estimate_dict = {}
ps_estimate_val_list = []

for ps_method_name in ps_method_name_list:
    ps_estimate = model.estimate_effect(identified_estimand_experiment,
                                    method_name="backdoor.propensity_score_" + ps_method_name,
                                    confidence_intervals=False,
                                    method_params={})
    # add estimate to dict and ATE to list
    ps_estimate_dict[ps_method_name] = ps_estimate
    ps_estimate_val_list.append(ps_estimate.value)

    print(ps_estimate)
    print("\n")


# ### Compute mean effect across methods

# In[8]:

print("Mean effect across methods:")
print(np.mean(ps_estimate_val_list))
