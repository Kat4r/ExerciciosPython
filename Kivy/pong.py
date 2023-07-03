from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
from random import randint

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y

        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))


    def update(self, dt):
        self.ball.move()

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if self.ball.y < self.y or self.ball.top > self.top:
            self.ball.velocity_y *= 1

        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball()

        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball()

class PongBall(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_y,velocity_x)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self,ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1*vx,vy)
            velo = bounced * 1.1
            ball.velocity = velo.x, velo.y + offset

PongApp().run()