from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class SimpleSimulator:
    def __init__(self):
        self.window = 0
        self.width = 640
        self.height = 480

        self.init_gl()
        self.reset()

    def reset(self):
        print("Simulation reset")
        self.color_red = False

    def apply_spacebar_action(self):
        self.color_red = not self.color_red

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(0, 0, 4, 0, 0, 0, 0, 1, 0)

        glEnable(GL_POINT_SMOOTH)
        glPointSize(100)
        glBegin(GL_POINTS)
        glColor3f(1.0 * int(self.color_red), 0.0 * int(self.color_red), 0.5 * int(self.color_red))
        glVertex2f(0, 0)
        glEnd()

        glutSwapBuffers()

    def inner_loop(self):
        self.render()

    def key_pressed(self, key, x, y):
        ch = key.decode("utf-8")
        if ch == ' ':
            self.apply_spacebar_action()

    def init_gl(self):
        # set up GLUT
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(0, 0)
        window = glutCreateWindow(b"Demo Env")
        glutIdleFunc(self.inner_loop)  # callback function, repeatedly called when idle
        glutKeyboardFunc(self.key_pressed)  # callback for keystrokes
        glutDisplayFunc(self.render)  # callback to render

        # init GL
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_LINE_SMOOTH)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()  # Reset The Projection Matrix
        gluPerspective(45.0, float(640) / float(480), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def close(self):
        self.__del__()

    def __del__(self):
        if bool(glutMainLoopEvent):
            glutMainLoopEvent()
