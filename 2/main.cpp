#include <iostream>
#include <cmath>

#include <GLFW/glfw3.h>

void error_callback(int error, const char* description)
{
    std::clog << "Error: " << description << '\n';
}

static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose(window, GLFW_TRUE);
}

float deg_y = 0;

void drawCube() {
  glBegin(GL_QUADS);
  // face in xy plane
  glColor3f(0.82, 0.41,
            0.12); // this the color with which complete cube is drawn.
  glVertex3f(0, 0, 0);
  glVertex3f(1, 0, 0);
  glVertex3f(1, 1, 0);
  glVertex3f(0, 1, 0);

  // // face in yz plane
  // glColor3f(1, 0, 0);
  // glVertex3f(0, 0, 0);
  // glVertex3f(0, 0, 1);
  // glVertex3f(0, 1, 0);
  // glVertex3f(0, 1, 1);

  // // face in zx plance
  // glColor3f(0, 1, 0);
  // glVertex3f(0, 0, 0);
  // glVertex3f(0, 0, 1);
  // glVertex3f(1, 0, 1);
  // glVertex3f(1, 0, 0);

  // //|| to xy plane.
  // glColor3f(0, 0, 1);
  // glVertex3f(0, 0, 1);
  // glVertex3f(1, 0, 1);
  // glVertex3f(1, 1, 1);
  // glVertex3f(0, 1, 1);

  // //|| to yz plane
  // glColor3f(0.73, 0.58, 0.58);
  // glVertex3f(0, 0, 1);
  // glVertex3f(1, 0, 1);
  // glVertex3f(1, 1, 1);
  // glVertex3f(0, 1, 1);

  // //|| to zx plane
  // glVertex3f(0.58, 0, 0.82);
  // glVertex3f(0, 1, 0);
  // glVertex3f(0, 1, 1);
  // glVertex3f(1, 1, 1);
  // glVertex3f(1, 1, 0);
  glEnd();
}

void display() {
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  // GLfloat model[4][4] = {
  //     {cosf(0.2f), 0, sinf(0.2f), 0},
  //     {0, 1, 0, 0},
  //     {-sinf(0.2f), 0, cosf(0.2f), 0},
  //     {0, 0, 0, 1},
  // };

  // glMultMatrixf(&model[0][0]);
  glTranslatef(-0.5, -0.5, 0);
  // glRotatef(30, 0, 0, 1);
  drawCube();


  // glPopMatrix();
}

int main(void) {
  GLFWwindow *window;

  glfwSetErrorCallback(error_callback);

  /* Initialize the library */
  if (!glfwInit())
    return -1;

  /* Create a windowed mode window and its OpenGL context */
  window = glfwCreateWindow(1920, 1080, "Lab2", NULL, NULL);
  if (!window) {
    glfwTerminate();
    return -1;
  }

  glfwSetKeyCallback(window, key_callback);

  /* Make the window's context current */
  glfwMakeContextCurrent(window);

  glfwSwapInterval(1);

  // Enable depth test
  glEnable(GL_DEPTH_TEST);
  // Accept fragment if it closer to the camera than the former one
  glDepthFunc(GL_LESS);

  glViewport(0, 0, 1920, 1080);

  /* Loop until the user closes the window */
  while (!glfwWindowShouldClose(window)) {
    display();

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0, 1920, 0, 1080, -1.0, 1.0);

    /* Swap front and back buffers */
    glfwSwapBuffers(window);

    /* Poll for and process events */
    glfwPollEvents();
  }

  glfwTerminate();
  return 0;
}
