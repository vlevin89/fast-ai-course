__author__ = 'victor'

from glob import glob
from random import shuffle
import os, shutil


def checkdogsCats(cwd):
    dogspath=os.path.join(cwd, 'dogs')
    catspath=os.path.join(cwd, 'cats')

    if not os.path.exists(dogspath):
        print ('making' + dogspath)
        os.mkdir(dogspath)
    if not os.path.exists(catspath):
        print ('making' + catspath)
        os.mkdir(catspath)


def checkFolders(cwd):

    sample=os.path.join(cwd,'sample')
    trainpath=os.path.join(cwd,'train')
    validpath=os.path.join(cwd,'valid')
    strainpath=os.path.join(cwd,'sample','train')
    svalidpath=os.path.join(cwd,'sample','valid')

    pathlist = [sample, trainpath, validpath,strainpath,svalidpath]

    for pathname in pathlist:
        print (pathname)
        if not os.path.exists(pathname):
            print ('making ' + pathname)
            os.mkdir(pathname)
        if not pathname==sample:
            checkdogsCats(pathname)


def train_valid_split(path):


    return

def sample_folder(path, percent=0.975):
    train_path = os.path.join(path,'train')
    all_dog = glob(os.path.join(train_path,'dog.*'))
    all_cat = glob(os.path.join(train_path,'cat.*'))
    sample_path = os.path.join(path,'sample')
    if not os.path.exists(sample_path):
        os.mkdir(sample_path)
    _,sample_set_dog = get_split_set(all_dog,percent)
    _,sample_set_cat = get_split_set(all_cat,percent)
    for f in sample_set_dog:
        shutil.copy(f,sample_path)
    for f in sample_set_cat:
        shutil.copy(f,sample_path)

    samp_dog = glob(os.path.join(sample_path,'dog.*'))
    samp_cat = glob(os.path.join(sample_path,'cat.*'))
    train_set_cat,valid_set_cat = get_split_set(samp_cat,0.8)
    train_set_dog,valid_set_dog = get_split_set(samp_dog,0.8)

    for f in train_set_cat:
            shutil.move(f,os.path.join(sample_path,'train','cats'))
    for f in valid_set_cat:
            shutil.move(f,os.path.join(sample_path,'valid','cats'))
    for f in train_set_dog:
            shutil.move(f,os.path.join(sample_path,'train','dogs'))
    for f in valid_set_dog:
            shutil.move(f,os.path.join(sample_path,'valid','dogs'))

def main_folder(path):
    train_path = os.path.join(path,'train')
    all_dog = glob(os.path.join(train_path,'dog.*'))
    all_cat = glob(os.path.join(train_path,'cat.*'))

    train_set_cat,valid_set_cat = get_split_set(all_cat,0.8)
    train_set_dog,valid_set_dog = get_split_set(all_dog,0.8)

    for f in train_set_cat:
            shutil.move(f,os.path.join(path,'train','cats'))
    for f in valid_set_cat:
            shutil.move(f,os.path.join(path,'valid','cats'))
    for f in train_set_dog:
            shutil.move(f,os.path.join(path,'train','dogs'))
    for f in valid_set_dog:
            shutil.move(f,os.path.join(path,'valid','dogs'))



def get_split_set(all_train,per):
    shuffle(all_train)
    n = len(all_train)
    split_point = int(per*n)
    return all_train[:split_point],all_train[split_point:]

def main():
    cwd = os.getcwd()
    print (cwd)

    train_valid_split=0.9
    train_sample_split=0.95

    checkFolders(cwd)
    sample_folder(cwd,0.95)
    main_folder(cwd)



main()




