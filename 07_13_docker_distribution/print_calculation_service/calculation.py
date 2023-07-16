import pandas as pd
import numpy as np
import time
class CalculationService():
    def __init__(self, input_path = None, output_path = None):
        self.input_path = input_path
        self.output_path = output_path
        self.data = None
    def load_data(self):
        self.data = pd.read_csv(self.input_path)
    def generate_data(self, samples):
        a = np.array(range(samples))
        np.random.shuffle(a)
        b = np.array(range(samples))
        np.random.shuffle(b)
        result = pd.DataFrame({'0': a, '1':b})
        result.to_csv(self.input_path, index=False)
        print (result.head())
    def process_data(self):
        self.a = self.data.iloc[:, 0]
        self.b = self.data.iloc[:, 1]
        add_result = self.add(self.a, self.b)
        mul_result = self.mul(self.a, self.b)
        div_result = self.div(self.a, self.b)

        result = pd.concat([self.a, self.b, add_result, mul_result, div_result], axis = 1)
        result.columns = ['a', 'b', 'add', 'mul', 'div']
        print (result.shape)
        result.to_csv(self.output_path, index= False)

        return result
    def add(self, a, b):
        result = a+b
        #print(result)
        return result
    def mul(self, a,b):
        result = a*b
        #print (result)
        return result
    def div(self, a,b):
        result = a/b

        #print (result)
        return result
    
if __name__ == "__main__":
    input_pa= "data/input.txt"
    output_pa = "share_dir/output.txt"
    cal = CalculationService(input_path=input_pa, output_path= output_pa)
    while True:
        cal.load_data()
        cal.process_data()
        time.sleep(1)