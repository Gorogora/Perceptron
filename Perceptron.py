from Functions import *
import  random as rnd

def main():
    file_name = "or.txt"
    training_x, training_y, m, num_atrib = load_data(file_name)
    mu = 0.1
    num_iterations = 50

    umbral = lambda x: 0.0 if x < 0.0 else 1.0

    # pesos iniciales aleatorios
    rnd.seed(1000)
    #w = [random.uniform(-1,1) for i in range(num_atrib)]
    w = [rnd.random()] * num_atrib

    #repetir hasta que se cumpla la condición de fin
    for i in range(num_iterations):
        # para cada x,y del conjunto de entrenamiento
        for x, y in zip(training_x, training_y):
            # calcular o
            product = dot(w,x)
            o = umbral(product)
            # para cada peso w_i hacer: w_i ← w_i + η(y − o)x_i
            for j in range(num_atrib):
                w[j] += mu * (y - o) * x[j]

    print("Los pesos son:", w)

    x = [-1.0,0.0,0.0]
    product = dot(w,x)
    output = umbral(product)
    print("Para la entrada ", x," la salida es ", output)


if __name__ == '__main__':
    main()