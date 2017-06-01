# installs all required packages

import pip

def install(package):
    pip.main(['install', package])


packages = ['Pickle', ' Random', ' Datetime', ' Matplotlib.pyplot',
            ' Seaborn', ' Os', ' Progressbar', ' Math', ' Copy',
            ' Operator', ' Networkx', ' Counter', ' Numpy', ' Prettytable',
            ' Webbrowser ']

if __name__ == '__main__':
    for package in packages:
        install(package)
