# Set of steps followed my character
def steps(self):

    # Defines timer for each animation, when to begin, and when to end.
    # It´s set to 181 instead of 180 so when resetting variables such as self.once, it only does it once.
    # If in need of more animations, repeat exactly this just changing the variable, limit if needed, and setting elif
    #   at the end.
    if self.timer[0] < 181:
        self.timer[0] += 1
    if self.timer[1] < 181 and self.timer[0] > 180:
        self.timer[1] += 1
    if self.timer[2] < 181 and self.timer[1] > 180:
        self.timer[2] += 1
    elif self.timer[3] < 91 and self.timer[2] > 90:
        self.timer[3] += 1

    # Because we began animationNum[0] in main.py, it just begins running.
    # You set a limit of where to move, and at which speed, in this case, normal velx.
    if self.animationNum[0] is True and self.player.x < 700:
        self.player.x += self.velx

    # Once set time for animationNum[0] is done, it ends first animation and begins second
    if self.timer[0] == 180:
        self.animationNum[0] = False
        self.animationNum[1] = True

    # Same as first animation, but going left and stopping at px200
    if self.animationNum[1] is True and self.player.x > 200:
        self.player.x -= self.velx

    # Once set time for animationNum[1] is done, it ends second animation and begins third
    if self.timer[1] == 180:
        self.animationNum[1] = False
        self.animationNum[2] = True

    # Jumps. It only does it once because of self.once variable
    if self.animationNum[2] is True:
        self.jump = True

    # Ends third animation and begins fourth once set time is done.
    # It resets self.once so character can jump again.
    if self.timer[2] == 180:
        self.animationNum[2] = False
        self.animationNum[3] = True
        self.once = False

    # Jumps again
    if self.animationNum[3] is True:
        self.jump = True

    # Ends fourth animation and begins fifth when set time is done
    if self.timer[3] == 90:
        self.animationNum[3] = False
        self.animationNum[4] = True

    # Moves to the right until px 600 at half the speed
    if self.animationNum[4] is True and self.player.x < 600:
        self.player.x += self.velx/2

    # Defines jump motion
    # Inherits from character
    # Once done it sets self.once to True, so it can only jump once.
    def jump_motion(Inherit):
        if Inherit.jump is True and Inherit.once is False:
            Inherit.player.y -= Inherit.mod_yvel * 3
            Inherit.mod_yvel -= 1
        if Inherit.mod_yvel < -Inherit.yvel:
            Inherit.jump = False
            Inherit.once = True
            Inherit.mod_yvel = Inherit.yvel
    jump_motion(self)
