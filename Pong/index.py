#Módulos
import turtle

#JANELA
#Criar uma janela
wn = turtle.Screen()
#Atribuição de um nome
wn.title("Pong")
#Cor de fundo
wn.bgcolor("black")
#Tamanho da janela
wn.setup(width=800, height=600)
#Impede que a janela atualize automáticamente
wn.tracer(0)

#SCORE
score_a = 0
score_b = 0

#PADDLE A
paddle_a = turtle.Turtle()
#Velocidade de animação
paddle_a.speed(0)
#Forma
paddle_a.shape("square")
#Cor
paddle_a.color("#0000FF")
#Esticar a forma 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#Impedir que deseje uma linha enquanto o Paddle se move
paddle_a.penup()
#Ponto de inicio
paddle_a.goto(-350, 0)

#PADDLE B
paddle_b = turtle.Turtle()
#Velocidade de animação
paddle_b.speed(0)
#Forma
paddle_b.shape("square")
#Cor
paddle_b.color("#FF0040")
#Esticar a forma 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
#Impedir que deseje uma linha enquanto o Paddle se move
paddle_b.penup()
#Ponto de inicio
paddle_b.goto(350, 0)

#BALL
ball = turtle.Turtle()
#Velocidade de animação
ball.speed(0)
#Forma
ball.shape("circle")
#Cor
ball.color("#00FF00")
#Impedir que desenhe uma linha enquanto a bola se move
ball.penup()
#Ponto de inicio
ball.goto(0, 0)
#Movimentação da bola
ball.dx = 0.1
ball.dy = -0.1

#PEN PONTUAÇÂO
pen = turtle.Turtle()
#Velocidade de animação
pen.speed(0)
#Cor
pen.color("#FFFFFF")
#Impedir que desenhe uma linha enquanto a pontuação é alterada
pen.penup()
#Esconder o "turtle"
pen.hideturtle()
#Coordenadas
pen.goto(0, 260)
#Jogadores
pen.write("Blue: 0 Vs Pink: 0",align="center", font=("Courier", 24, "normal"))

#Movimentação das barras para cima
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#Movimentação das barras para baixo
def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)   

#Ligação ao teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Loop principal
while True:
    wn.update()

    #Movimento da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Margens/Limites y
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Margens/Limites x e pontuação
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        #Limpar o número anteriro
        pen.clear()
        pen.write("Blue: {} Vs Pink: {}".format(score_a, score_b),align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        #Limpar o número anteriro
        pen.clear()
        pen.write("Blue: {} Vs Pink: {}".format(score_a, score_b),align="center", font=("Courier", 24, "normal"))

    #Paddle A and ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.dx *= -1
    #Paddle B and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.dx *= -1