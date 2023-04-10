import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 5351182285 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    successes = np.array([x_success, y_success])
    samples = np.array([x_cnt, y_cnt])
    stat, p_value = proportions_ztest(count=successes, nobs=samples,  alternative='larger')
    Result = bool (p_value<=0.1)
    return Result # Ваш ответ, True или False
