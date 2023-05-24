from Rectangle import *
from texture import *

def keypress(key, x, y):
	global man_path,left_key,right_key

	""" moving ball to the left"""
	if G.squirrel.left > 0 and key == GLUT_KEY_LEFT:
		G.ball_dir_x = -1
		G.keystates[0] = True
		G.keystates[1] = False
		G.stand_left=True
		if G.increaseR:
			G.factor=1
		G.increaseR=False

	# """ moving ball to the right"""
	elif G.squirrel.right < 800 and key == GLUT_KEY_RIGHT:
		G.ball_dir_x = 1
		G.keystates[0] = False
		G.keystates[1] = True
		if not G.increaseR :
			G.factor=1
		G.stand_left=False
		G.increaseR=True

	# """ jumping """
	elif key == GLUT_KEY_UP:
		G.keystates[2] = True
		G.jumping = True
		G.on_plate=False

	# """ BEGIN"""
	elif key == b' ' and G.gamestart is False:
		G.gamestart = True
		G.gameover = False

	glutPostRedisplay()

def reset_keys(key,x,y):
	if  key == GLUT_KEY_LEFT:
		G.index=6
		G.keystates[0]=False
		
	if  key == GLUT_KEY_RIGHT:
		G.index=7
		G.keystates[1]=False
		G.increaseR = False

	if key == GLUT_KEY_UP:
		G.keystates[2]=False

	glutPostRedisplay() # to redraw the scene