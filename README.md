# Alfred password generator

## Index
1. [What is](#What-is)
2. [Warning](#Warning)
3. [Dependencies](#Dependencies)
4. [Commands](#Commands)
5. [Download](#Download)


### What is
Alfred workflow for generating random passwords.

### Warning
Randomly generating a password is a great strategy to protect your online accounts and offline devices.  

But keep in mind generating a password involves not only the random element but also [entropy](https://www.omnicalculator.com/other/password-entropy). There're complex techniques on which to generate a password that respects the minimum bases of entropy to be considered an excellent password.

This script uses only the random concept, but not entropy.

### Dependencies
You need [Alfred](https://www.alfredapp.com) for MacOS.  
Python. 

You can use [Homebrew](https://docs.brew.sh/Homebrew-and-Python#python-3y) with the command below or download and install the latest version on [site](https://www.python.org/downloads/macos/).

```shell
brew install python
```

### Commands
- *pw n*: where n is an integer representing the length of the password

![Example](https://user-images.githubusercontent.com/22590804/229761866-8a9eed72-28bb-4bd8-ad06-bb1257e4d5ea.png)

The password will be copied to the clipboard.

### Download
Latest release: [here](https://github.com/simonemargio/PyAlfredPasswordGenerator/releases/tag/v.1.0.0)