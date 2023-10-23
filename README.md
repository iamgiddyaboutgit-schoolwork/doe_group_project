# Population Genetics Experiment Group Project

# Getting things set up
To run code in the src directory, there are some dependencies that need to
be installed.  These dependencies are specified in the environment.yml
file.  The last line in the environment.yml file may need to be adjusted 
to the prefix that you want for your conda/mamba environment.  The 
dependencies in the environment.yml file can be installed using the
following commands (assuming that you already have conda or mamba installed). 
The following line only needs to be run the first time you clone the repo. 
mamba can be used in place of conda except for activating/deactivating environments.

```
mamba env create -f ./environment.yml
```

Now, that you have the needed environment, you can just run the following
every time after fetching from the remote. This idea is from:
https://stackoverflow.com/a/43873901/8423001

```
conda activate doe_group_project
mamba env update --file ./environment.yml --prune --prefix /home/justin/bin/mambaforge/envs/doe_group_project
```

# Reproducible Code

If the code requires new dependencies, then they can be added to the
.yml file with the following command:

```
mamba env export | head -n -1 > ./environment.yml
```

Please remember to do this before making a pull request.
