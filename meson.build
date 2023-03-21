project('lab1', 'cpp',  default_options : ['cpp_std=c++20'])

opengl_deps = [dependency('GLUT'), dependency('glfw3'), dependency('gl')]

executable('1', '1/main.cpp',
                   dependencies : opengl_deps,
                   override_options : ['cpp_std=c++20'])

executable('2', '2/main.cpp',
                   dependencies : opengl_deps,
                   override_options : ['cpp_std=c++20'])
