"""
@Author: Swapnil Bhoyar
@Date: 2021-07-27
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-27
@Title : this program contains CLI command operations.
"""
import subprocess

def run_cmd(args_list):
    """
    Description:
        this function execute CLI commands
    """
    print('Running systrm command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err


(ret, out, err)= run_cmd(['hadoop', 'version'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-mkdir', '/myDataFlair'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-ls', '/newDataFlair'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-put', '/home/neo/Downloads/test1', '/myFileFromLocal'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-copyFromLocal', '/home/neo/Downloads/localfile1', '/myFileFromLocal'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-cat', '/myFileFromLocal/mytest1.txt'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-get', '/myFileFromLocal', '/home/neo/Downloads/myCopyFromHadoop'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-copyToLocal', '/myFileFromLocal/mytest1.txt', '/home/neo/Downloads/myCopyFromHadoop'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-mv', '/dataFlair', '/myDataFlair'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-cp', '/myFileFromLocal/mytest1.txt', '/tmp'])
print(ret, out, err)

(ret, out, err)= run_cmd(['hadoop', 'fs', '-rm', '-r', '/filefromlocal'])
print(ret, out, err)