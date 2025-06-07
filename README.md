# thn - thumbnail creator

Create downsized versions of images - ideal to fit into size limits!

Usage:  
```
python thn.py -s {source directory} -d {destination directory} -f {output format} -h {output height} -i {interval}
```

**{source directory}** is the path to the directory where the images to be resized are, e.g.: `/mnt/c/Users/lakos/Documents/thn/folder1`.

**{destination directory}** is the path to the directory where the resized images should be saved, e.g.: `/mnt/c/Users/lakos/Documents/thn/folder2`.

**{output format}** is the format the output file should be. Must be either `jpg` or `png`.

**{output height}** is the height the output file should be. Must be positive, e.g. `1080`. The aspect ratio of the original image is kept intact.

**{interval}** is the time interval in hours in which the input files are to be considered. For example, if interval is set to `24`, then only the image files inside the source directory whose last modified time is within the last 24 hours will be considered.