import h5py
import numpy as np
import json
import os


def open_file(path_to_file):
    if os.path.splitext(path_to_file)[1] == '.json':
        json_file = open(path_to_file)
        json_dic = json.load(json_file)
        return json_dic
    elif os.path.splitext(path_to_file)[1] == '.txt':
        txt_file = open(path_to_file, 'r')
        txt_file = txt_file.read()
        txt_file_list = txt_file.split('\n')
        return txt_file_list
    elif os.path.splitext(path_to_file)[1] == '.npy':
        np_dict = np.load(f'{path_to_file}', allow_pickle=True)
        return np_dict
    elif os.path.splitext(path_to_file)[1] == '.h5':
        h5py_file = h5py.File(f'{path_to_file}', 'r')
        return h5py_file
