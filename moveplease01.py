
import shutil
import os

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_Storage/')
xname=input("What is the new name for kerrigan.obj?")
shutil.move('ceph_Storage/kerrigan.obj', 'ceph_Storage/' + xname)
