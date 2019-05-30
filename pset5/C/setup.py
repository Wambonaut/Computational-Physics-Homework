from distutils.core import setup, Extension

module1= Extension("num", sources= ["tred2.c"])
setup (name="num", version="0.0", description="test123", ext_modules= [module1])
