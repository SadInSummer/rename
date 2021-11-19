#coding=utf-8
import sys, string, os, shutil



def RenameFiles(srcdir, prefix):
    srcfiles = os.listdir(srcdir)
    index = 1
    for srcfile in srcfiles:
        srcfilename = os.path.splitext(srcfile)[0][1:]
        sufix = os.path.splitext(srcfile)[1]
        destfile = srcdir + "//" + prefix + "_%04d"%(index) + sufix
        srcfile = os.path.join(srcdir, srcfile)
        os.rename(srcfile, destfile)
        index += 1


srcdir = "/home/wace/wace/cccccccccc/IMAGECOMBINE/momo/oceans"
prefix = "ocean"
RenameFiles(srcdir, prefix)
