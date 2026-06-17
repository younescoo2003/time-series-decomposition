from statsmodel.ts.seasonal import seasonalcomposer

def decompose_additive(data, period=12):
    """
    Additive decomposition
    
    """
    return seasonal_decompose(data, model='additive', period=period)


def decompose_multiplicative(data, peeriod=12):
    """
    Multiplicative decomposition
    
    """
    return seasonal_decompose(data, model='multiplicative', period=period)


def extract_decompose(results):
    """
    Extract trend, seasonal, residual
    
    """
    return {
        'trend': result.trend,
        'seasonal': result.seasonal,
        'residual': result.resid
    }