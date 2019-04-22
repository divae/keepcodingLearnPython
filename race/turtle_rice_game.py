import turtle
import random

class Game():
    __runners = []
    __post_start_y = (-30,-10,10,30)
    __color_turtle = ('purple', 'pink', 'purple', 'pink')
    __num_players = 4
        
    def __init__(self,width, height):       
        self.__create(width,height)
        self.__add_runners(self.__num_players)
        
    def play(self):
        winner = False
        while not winner:
            for runner in self.__runners:
                position = self.__move(runner)
                if self.__are_at_the_end(position,runner):                    
                    self.__position_and_show_winner(runner)
                    winner = True
                    return
    
    def __str__(self):
        return "Turtle Rice : {} players".format(self.__num_players)
                    
    def __are_at_the_end(self,position,runner):
        return position >= self.__finish_line
    
    def __position_and_show_winner(self, runner):
        runner.setx(self.__finish_line)
        runner.write("Winner", True, align="center",font = ('',9,''))
            
    def __rolling_dice(self):
        return random.randint(1,878)
    
    def __move(self, runner):
        position = runner.ycor()
        rolling = self.__rolling_dice()
        runner.forward(+rolling)
        return runner.xcor()
        
    def __create(self,width,height):
        self.__init()
        self.__size(width,height)
        self.__color()
        
        self.__calculate_modifier(width)
        self.__calculate_start_line(width)
        self.__calculate_finish_line(width)
        
    def __init(self):
        self.__screen = turtle.Screen()
        
    def __size(self,width,height):
        self.__screen.setup(width,height)
        
    def __color(self):
        self.__screen.bgcolor('lightgray')
    
    def __add_runners(self, numbers):
        for number in range(numbers):
            runner = self.__create_runner(number)          
            self.__add_runner(runner)
            
    def __create_runner(self, number):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__color_turtle[number])
            new_turtle.shape('turtle')
            new_turtle.penup()
            position = self.__post_start_y[number]
            new_turtle.setpos(self.__start_line,position)
            return new_turtle
        
    def __add_runner(self, runner):
        self.__runners.append(runner)
            
    def __calculate_start_line(self,width):
        self.__start_line = ( -width / 2 ) + self.__modifier
   
    def __calculate_finish_line(self,width):
        self.__finish_line = ( width / 2 ) - self.__modifier
        
    def __calculate_modifier(self, width):
        self.__modifier = (width * 7 / 100)
            


if __name__ == '__main__':
    c = Game(640,480)
    print(c)
    c.play()
    