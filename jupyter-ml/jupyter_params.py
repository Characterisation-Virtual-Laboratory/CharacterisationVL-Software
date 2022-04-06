#!/usr/bin/python3
import subprocess
import json
import time
import os
import re
import io
import errno

MAX_RETRY=20
runtime_dirs=["~/.local/share/jupyter/runtime"]

def parent_chain(pid):
    cmd = ['ps','--no-headers','o','ppid','-p','{}'.format(pid)]
    try:
        ppid = int(subprocess.check_output(cmd).decode())
        if ppid != 1:
            for pppid in parent_chain(ppid):
                yield pppid
        yield int(ppid)
    except subprocess.CalledProcessError:
        return


def possible_pids(jobid):
    #Yield a list of pids which have the the jobid either as the pid, or in the command
    #For slurm this list should include the pid
    #For pure batch, obiously the pid is the jobid
    #For PBS pro I don't know what will happen, but we can burn that bridge when we come to it.
    me = os.environ['USER']
    cmd = ['ps','o','pid,cmd','-u','root,{}'.format(me)]
    processes = subprocess.check_output(cmd).decode()
    for p in processes.splitlines():
        if jobid in p:
            (pid,cmd) = p.lstrip().split(" ",1)
            yield(int(pid))

def check_pid(pid,jobid):
    possible_job_pids = list(possible_pids(jobid))
    pidchain = list(parent_chain(pid))
    for p in pidchain:
        if p in possible_job_pids:
            return True
    return False

def check_jupyter(port,token):
    import urllib.request
    try:
        r=urllib.request.urlopen('http://localhost:{}/?token={}'.format(port,token))
        s = r.read().decode()
        if 'Password or token' in s:
            return False
    except urllib.request.URLError:
        return False
    return True


def list_servers():
    """ We could use jupyter --list-servers, but things get complicated when we have a shared home directory"""
    for d in runtime_dirs:
        runtime_dir = os.path.expanduser(d)

        for file_name in os.listdir(runtime_dir):
            if re.match('nbserver-(.+).json', file_name):
                with io.open(os.path.join(runtime_dir, file_name), encoding='utf-8') as f:
                    info = json.load(f)
                    yield(info)
            if re.match('jpserver-(.+).json', file_name):
                with io.open(os.path.join(runtime_dir, file_name), encoding='utf-8') as f:
                    info = json.load(f)
                    yield(info)

def check_servers(jobid):
    for info in list_servers():
        # Check that the pid for this nbserver is in the job, and that the server can be connected to
        if ('pid' in info) and check_pid(info['pid'],jobid) and check_jupyter(info['port'],info['token']):
            return info
    return None


import sys
import socket
jobid = sys.argv[1]
hostname = socket.gethostname()

data = check_servers(jobid)
retry = 0
while data is None and retry < MAX_RETRY:
    time.sleep(1)
    retry = retry + 1
    data = check_servers(jobid)

if data is not None:
    print(json.dumps(data))
else:
    error = {}
    error['hostname'] = hostname
    error['msg'] = "Couldn't find all the information to connect to your jupyter hub instance. Is it possible that jupyter hub has quit unexpectedly? This sometimes happens if you don't allocate enough RAM for it"
    print(json.dumps({'error':error}))


