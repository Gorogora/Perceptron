import csv, os

def get_file_path(file_name, folder=""):
    if folder == "":
        currentdirpath = os.getcwd()
    else:
        currentdirpath = os.getcwd() + "/" + folder

    file_path = os.path.join(currentdirpath, file_name)
    return file_path


def load_data(file_name):
    # get the path
    path = get_file_path(file_name)
    # open the file
    file = open(path)
    # read the file
    reader = csv.reader(file, delimiter=',')
    x = [list(map(float, line)) for line in reader]
    # load inputs
    temp_datax = [[-1.0] + elem[:-1] for elem in x]  # return [[2100.0, 3.0], [1600.0, 3.0], [..., ...]]
    # load outputs
    temp_datay = [elem[-1] for elem in x]  # return [400000.0, 330000.0, 369000.0, 232000.0, ... ,]
    # number of instances of the problem
    m = len(temp_datay)
    # numbers of variables + 1
    num_atribu = len(temp_datax[0])

    return temp_datax, temp_datay, m, num_atribu  # return a tuple, we could also write (tempDataX, tempDataY, ...)

def dot(w, x):
    return sum(w_i * x_i for w_i, x_i in zip(w, x))