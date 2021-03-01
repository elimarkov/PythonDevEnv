from setuptools import setup
from Cython.Build import cythonize
from Cython.Compiler import Options
from distutils.extension import Extension

calc_pi_ext = Extension("src.Maths.Matrix",
            language="c++",
            sources=["src/Maths/Matrix.py"],
            # extra_compile_args=["-Ox", "-Zi"], # disabling all optimizations, generate full debug information
            # extra_link_args=["-debug:full"], # produce the PDB file
            # define_macros=[('CYTHON_TRACE', '1')]
            )


ext_modules = cythonize(calc_pi_ext,
                        language_level=3,
                        annotate = True,
                        compiler_directives={
                            'embedsignature': True,
                            # 'linetrace': True,
                            'annotation_typing': True,
                            'emit_code_comments': True
                        },
                        # emit_linenums=True, # adds “#line” directives to the  C/C++ code which instruct MSVC to generate a source map back to the original Cython file.
                        # gdb_debug=True
                        )



setup(
    name ='calc_pi',
    ext_modules = ext_modules,
    zip_safe=False
)
