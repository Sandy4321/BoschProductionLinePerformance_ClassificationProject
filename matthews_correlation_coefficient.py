# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:31:35 2016

@author: Larry
"""
import math

# INPUTS
#   TP := the number of true positives
#   TN := the number of true negatives
#   FP := the number of false positives
#   FN := the number of false negative
#
# OUTPUTS
#   matthews := the matthews correlation coefficient


def matthews_correlation_coefficient(TP, TN, FP, FN):
    numerator = TP*TN - FP*FN
    denominator = math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
    matthews = numerator / denominator
    return matthews
