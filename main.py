# Importa las clases Turtle y Screen, y las funciones forward, onkeypress y setheading del módulo turtle
from turtle import Turtle, Screen

# Importa el módulo random para generar números aleatorios
import random



#TODO:random color
# Esta función cambia el color de una tortuga de forma aleatoria
def change_color(turtle):
    
    # Genera un número aleatorio entre 0 y 1 para la componente roja del color
    R=random.random()   
    
    # Genera un número aleatorio entre 0 y 1 para la componente azul del color
    B=random.random()
    
    # Genera un número aleatorio entre 0 y 1 para la componente verde del color
    G=random.random()
    
    # Asigna el color generado a la tortuga usando el método color
    turtle.color(R,G,B)
    

def move_forwards(turtle):
    for i in range(10):
        
        # Llama a la función change_color para cambiar el color de la tortuga
        change_color(turtle)
        
        # Deja una marca con la forma y el color de la tortuga en la posición actual
        turtle.stamp() 

        # Levanta el lápiz de la tortuga para que no deje trazo al moverse
        turtle.penup()

        # Avanza la tortuga 50 unidades
        turtle.forward(50)

        # Baja el lápiz de la tortuga para que deje trazo al moverse
        turtle.pendown()



# Crea un objeto de la clase Turtle
turtle=Turtle()

# Aumenta la velocidad de la tortuga a la máxima posible
turtle.speed("fastest")



# Cambia la forma de la tortuga a un círculo
turtle.shape("circle")



# Aumenta el grosor del trazo de la tortuga a 20 unidades
turtle.pensize(20)

for i in range(-250, 250, 50):
    
    print(i)
     
    # Levanta el lápiz de la tortuga para que no deje trazo al moverse
    turtle.penup()

    turtle.goto(-260, i)

    move_forwards(turtle)











# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Crea un objeto de la clase Screen
my_screen =Screen()


# Cierra la ventana al hacer click en la pantalla
my_screen.exitonclick()
