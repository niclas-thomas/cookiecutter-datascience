import os

# setup for poetry
os.system('poetry install')
os.system('poetry add numpy pandas matplotlib seaborn jupyter jupyterlab')

# import matplotlib

# # setup for matplotlib style
# rc_path = matplotlib.matplotlib_fname()
# os.system(
#     'curl -L https://raw.githubusercontent.com/ncthomas/configs/master/laura.mplstyle >> {}'.format(rc_path)
#     )
