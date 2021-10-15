import pandas as pd
import matplotlib.pyplot as plt
import uuid
import os


class logic_graphics(object):
    def __init__(self):
        self.data = "";
        
    def graphyc_scatter(self, value_x, value_y, title):
        path_img = self.get_path_img()
        fig, ax1 = plt.subplots(1, 1, figsize=(10,5))

        ax1.scatter(value_x, value_y)
        ax1.set_title(title)
        
        fig.savefig(path_img, format='png')
        return f'{os.getcwd()}\{path_img}'
        

    def graphyc_matshow(self, plot_data):
        path_img = self.get_path_img()
        corr = plot_data.corr()
        
        fig = plt.figure(figsize=(10,8))
        plt.matshow(corr, fignum=fig.number)
        plt.xticks(range(len(plot_data.columns)), plot_data.columns)
        plt.yticks(range(len(plot_data.columns)), plot_data.columns)
        plt.colorbar()
        plt.ylim([5.5, -0.5])
        
        fig.savefig(path_img, format='png')
        return f'{os.getcwd()}\{path_img}'
        
    def graphyc_ylabel(self, data, title_y):
        path_img = self.get_path_img()
        fig = plt.figure(figsize=(10,8))        
        plt.plot(data)
        plt.ylabel('some numbers')
        plt.show()
        fig.savefig(path_img, format='png')
        return f'{os.getcwd()}\{path_img}'
    
    def get_guid(self):
        return uuid.uuid4()
    
    def get_path_img(self):
        return f'images\{self.get_guid()}.png'
    
    def prueba(self):                
        ruta = ""
        ruta = "files\\hour.csv"
        file_data = pd.read_csv(ruta)
        
        #self.graphyc_ylabel(file_data['casual'], 'prueba')
        
        ##Example 1
        #cols = ["temp", "atemp", "hum", "windspeed", "registered", "casual"]
        #plot_data = file_data[cols]
        #self.graphyc_matshow(plot_data)
        
        ##Example 2
        #self.graphyc_scatter(file_data['casual'], file_data['season'], 'asdasdasd')
    

#logic_graphics().prueba()
