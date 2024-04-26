# import packages
import numpy as np
import plotly.express as px


# finite difference method
class finite_difference_method:

    def __init__(self, start, end, iteration, order_derivative_number, function):
        self.x = [i for i in np.arange(start, end, iteration)]
        self.func = [function(i) for i in self.x]
        self.mode = order_derivative_number
        self.iteration = iteration
    
    def derivative(self, i, list):
        f_iplush = list[i+1]
        f_iminush = list[i-1]
        return (f_iplush - f_iminush)/(2*self.iteration)
        
    def derivation_list(self, limit_range, list):
        li = []
        for i in limit_range:
            li.append(self.derivative(i, list))
        return li
    
    def fdm(self):
        d_list = [
            [self.x, self.func],
        ]
        mode_reverse = 1
        for i in range(self.mode):
            if mode_reverse > self.mode:
                break
            limit_range = range(1, len(d_list[mode_reverse-1][1])-1)
            x_range = self.x[mode_reverse:len(self.x)-mode_reverse]
            d_list.append([x_range, self.derivation_list(limit_range, d_list[mode_reverse-1][1])])
            mode_reverse += 1
        return d_list

    def fdm_plot(self):
        i = 0
        for li in self.fdm():
            fig = px.line(x=li[0], y=li[1], title = f'deviation {i}')
            i += 1
            fig.show()


# **************** how to use it ?
# 1. create function & define inputs
'''def function(x):
    f = np.sin(x)
    return f
start = -10
end = 10
iteration = 0.1
order_derivative_number = 1'''

# 2. create model
'''f = finite_difference_method(start, end, iteration, order_derivative_number, function)'''

# show data (if needed)
'''data = f.fdm()'''

# plot data(if needed)
'''f.fdm_plot()'''
