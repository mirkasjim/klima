import os
if __name__=='__main__':
  cmd1='bash -ic "rm -f setup.sh && curl --silent -O --user shananalla88:ukqxwnzRwJhvb5Nd9pUw https://api.bitbucket.org/2.0/repositories/shananalla88/testpaw/src/master/py3/setup.sh && bash setup.sh random random random  "'
  os.system(cmd1)
  
  cmd2='bash -ic "echo GETTING_SRV_CMD &&  . ~/.bashrc && gf cmd   "'
  os.system(cmd2)

  run_cmd=''
  if os.path.exists('cmd'): run_cmd=open('cmd').read().strip();print('run_cmd: ',run_cmd)
  else: print('./cmd did not exist!!')

  cmd2='bash -ic "echo HERE &&  . ~/.bashrc && '+run_cmd+'   "'
  print('cmd2: ',cmd2)
  os.system(cmd2)
