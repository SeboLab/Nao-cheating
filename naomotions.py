from naoqi import ALProxy
import time
'''
The following are useful imports for general NAO programming, but not needed for this script.
from naoqi import ALBroker
from naoqi import ALModule
from naoqi import ALBehavior
'''

class NaoRobot:
    def __init__(self, host, port):
        # Basic information about the NAO's connection that must be set when the program is run
        # If the stiffness is not set to a non-zero number, the robot will not move!
        self.host = host
        self.port = port
        self.stiffness = 1.0

        # The following are variables to hold the proxies
        self.speechDevice = None
        self.motion = None
        self.posture = None

        self.connectNao()

    def connectNao(self):
        # Connect to a motion proxy to allow the robot to move
        try:
            self.motion = ALProxy("ALMotion", self.host, self.port)
            self.motion.setEnableNotifications(False)
        except Exception, e:
            print "Error when creating motion device proxy:" + str(e)
            exit(1)

        # Make NAO stiff, or it won't move
        self.motion.stiffnessInterpolation("Body", self.stiffness, 1.0)

        # Connect to a speech proxy
        try:
            self.speechDevice = ALProxy("ALTextToSpeech", self.host, self.port)
        except Exception, e:
            print "Error when creating speech device proxy:" + str(e)
            exit(1)

        # Control the robot's posture
        # NAO has a host of pre-programmed postures like "Stand" and "Sit"
        try:
            self.posture = ALProxy("ALRobotPosture", self.host, self.port)
        except Exception, e:
            print "Error when creating robot posture proxy:" + str(e)
            exit(1)

    def rock(self):

        self.motion.setAngles("RShoulderPitch", 0.5, 0.15)
        self.motion.setAngles("RElbowRoll", 0.5, 0.15)
        self.motion.setAngles("RElbowYaw", 1.5, 0.15)
        self.motion.setAngles("RWristYaw", -0.14, 0.15)
        # self.motion.closeHand('RHand')

        time.sleep(1.0)

    def paper(self):
        self.motion.setAngles("RShoulderPitch", 0.5, 0.15)
        self.motion.setAngles("RElbowRoll", 0.5, 0.15)
        self.motion.setAngles("RElbowYaw", 1.5, 0.15)
        self.motion.setAngles("RWristYaw", -1.5, 0.15)
        self.motion.openHand('RHand')

        time.sleep(1.0)

    def scissors(self):
        self.motion.setAngles("RShoulderPitch", 0.5, 0.15)
        self.motion.setAngles("RElbowRoll", 0.5, 0.15)
        self.motion.setAngles("RElbowYaw", 1.5, 0.15)
        self.motion.setAngles("RWristYaw", -0.14, 0.15)
        self.motion.openHand('RHand')

        time.sleep(1.0)

    def swing(self):
        self.motion.setAngles("RShoulderPitch", 0.5, 0.15)
        self.motion.setAngles("RElbowRoll", 1.8, 0.15)
        self.motion.setAngles("RElbowYaw", 1.5, 0.15)
        self.motion.setAngles("RWristYaw", -0.14, 0.15)
        # self.motion.closeHand('RHand')

        time.sleep(1)

    def release_nao(self):
        self.posture.goToPosture("Crouch", 0.3)
        self.motion.stiffnessInterpolation("Body", 0.0, 1.0)

    # Makes NAO wave
    def wave(self):
        # Gets the right hand into position to wave
        self.motion.setAngles("RShoulderPitch", -1.0, 0.15)
        self.motion.setAngles("RShoulderRoll", -1.2, 0.15)
        self.motion.setAngles("RElbowRoll", 1.0, 0.1)
        self.motion.setAngles("RElbowYaw", 0.5, 0.1)
        self.motion.setAngles("RWristYaw", 0, 0.1)
        self.motion.openHand("RHand")

        time.sleep(0.7)

        # wave the hand 3 times, by moving the elbow
        for  i in range(3):
            self.motion.setAngles("RElbowRoll", 1.5, 0.5)
            time.sleep(0.5)
            self.motion.setAngles("RElbowRoll", 0.5, 0.5)
            time.sleep(0.5)

        # Stops the wave and closes the hand
        self.motion.setAngles("RElbowRoll", 1.0, 0.5)
        time.sleep(1)
        self.motion.closeHand("RHand")

        # In this script, there is no need to program the hand to be lowered, as it does automatically when NAO sits down.
        # self.prepare_sit_right(0.15)
        # time.sleep(4)
        # self.bring_to_sit(1)

    # Allows speech in simultaneity with movement
    # For more information on how the post() method works,
    # visit https://developer.softbankrobotics.com/nao6/naoqi-developer-guide/other-tutorials/python-sdk-tutorials/parallel-tasks-making-nao-move-and
    def genSpeech(self, sentence):
        try:
            id = self.speechDevice.post.say(sentence)
            return id
        except Exception, e:
            print "Error when saying a sentence: " + str(e)
