# gromacs-visualizer
Tool for visualizing Gromacs generated xvg files

## Installation
- Clone main repository to ```<PATHNAME>```
- Add ```alias plot="python3 <PATHNAME>/main.py"``` to .bashrc

## Usage
- To generate a plot of first column from multiple files, use ```plot <filnames>```
- To generate plots of all columns of multiple files (one plot per file), use ```plot <filenames> -nx```

Here ```<filenames>``` can be multiple space separated ```xvg``` files
