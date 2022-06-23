# brailler


## A simple tool to convert images to braille characters.

brailler converts images to braille characters by using different algorithms
to rescale the image and detect either edges or luminance, subsequently it maps
the result to the dots in the braille characters.


## An example

Let's say you want to turn the following image into braille.

![](https://github.com/victorcebarros/brailler/raw/master/example/hello.png)

You can accomplish by doing the following command:

```
python3 -m brailler hello.png
```

It will output the result to the terminal.

```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡄⠀⢠⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣆⠀⠀⠀⠀⠀⠀⠙⣵⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣹⠀⠀⣇⣇⠀⠀⠀⠀⠀⠀⠀⠀⡟⡇⢸⣹⠀⠀⠀⠀⠀⣀⡀⠀⠀⠸⣿⠀⠀⠀⠶⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⡟⡇⠀⢹⢸⠀⠀⡴⣺⣗⢦⡀⠀⣧⣇⠘⡿⡆⠀⢠⢾⠽⠟⢯⢳⠀⠀⡟⡇⠀⠀⢀⡀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣧⣳⠯⠽⡜⡇⢰⢃⣓⣾⡥⠇⠀⢹⢹⠀⣧⣇⠀⣿⡇⠀⠀⠈⡏⡇⠀⢷⣧⠀⠀⠘⠋⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⢳⢳⠘⣟⢦⣀⣠⢴⠄⠘⡞⡆⢸⣹⠀⠸⣽⢄⣀⡴⣣⠃⠀⠘⠚⠀⠀⠀⠀⠀⠀⠸⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠘⠾⠂⠈⠓⠒⠚⠉⠀⠀⠳⠇⠀⠛⠃⠀⠈⠙⠒⠋⠁⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢤⣴⡦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠛⠉⠁⢀⢧⠇⠀⠀⣀⣠⡤⢤⣶⣒⣒⣺⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠁⠀⠀⠀⠀⢾⣺⣖⣺⠭⠗⠚⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```

The defaults may not work for every single image, and, as of now, the program
doesn't automatically detect proper values for both the threshold or scaling
factor. You will probably want to check out the available options by passing
the `--help` flag to the program.


## Setting up

In order to use it, you will need to install some dependencies required to run
the application. You can do so by issuing the following command:

```
pip install -r requirements.txt
```

You can then run the program:

```
python -m brailler
```

Depending on which operating system you are in, you may need to use pip3
and python3. Please refer to your system's manual.

Also note that I haven't tested this on Windows, since I don't have a Windows
computer. Kindly file an issue and report any bugs that may happen there.


## TL;DR Usage

| Option            | Description                                                             |
| ----              | ----                                                                    |
| `-a, --algorithm` | Uses a specific algorithm to process the image. (default: sobel)        |
| `-s, --scale`     | Scales image up or down. (default: 0.5)                                 |
| `-t, --threshold` | Sets the value which tints a dot in the braille matrix. (default: 0.25) |

You can use these flags to change the behavior of the program.


## Contributing

Whether you found a bug in the code and wants to fix it or whether you want to add
new functionality to the program, feel free to send a PR!

As long as the code is properly formatted, and that the feature is desirable, I will
gladly merge them.


## License

This project is licensed under the BSD 2-Clause License. See LICENSE for more information.

This project uses a few third party libraries, [scikit-image](https://scikit-image.org/),
[numpy](https://numpy.org/).
