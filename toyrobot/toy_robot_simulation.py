from toyrobot.position import Position


def in_front_of(position: Position) -> Position:
    return Position(
        orientation=position.orientation,
        x=position.x + position.orientation.forward_x,
        y=position.y + position.orientation.forward_y
    )


DEFAULT_TABLE_SIZE = 5


class ToyRobotSimulation:

    def __init__(self, table_size_x: int = DEFAULT_TABLE_SIZE, table_size_y: int = DEFAULT_TABLE_SIZE):
        self.table_size_x = table_size_x
        self.table_size_y = table_size_y
        self.robot: Position = None

    def is_position_valid(self, position: Position) -> bool:  #b/w 0,0 to 5,5 valid 
        return position.x >= 0 and \
               position.x < self.table_size_x and \
               position.y >= 0 and \
               position.y < self.table_size_y

    def place_robot(self, position: Position):  ### self.robot is position object if valid position 
        if self.is_position_valid(position):
            self.robot = position

    def move_robot(self):    # if robot placed then oriententation same move x,y and if valid then update 
        if self.robot is not None:
            new_pos = in_front_of(self.robot)
            if self.is_position_valid(new_pos):
                self.robot = new_pos

    def turn_robot_left(self): # if robot placed x,y coordinate same and rotate left and update robot 
        if self.robot is not None:
            self.robot = Position(
                orientation=self.robot.orientation.left(),
                x=self.robot.x,
                y=self.robot.y
            )

    def turn_robot_right(self): # if robot placed x,y coordinate same and rotate right and update robot
        if self.robot is not None:
            self.robot = Position(
                orientation=self.robot.orientation.right(),
                x=self.robot.x,
                y=self.robot.y
            )
